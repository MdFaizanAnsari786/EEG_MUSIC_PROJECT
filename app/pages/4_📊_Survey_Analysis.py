import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
import os
import sys

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Behavioral Survey Analysis",
    page_icon="📊",
    layout="wide"
)

# Import and apply theme with session state
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sky_blue_theme import DARK_MODE_CSS
st.markdown(DARK_MODE_CSS, unsafe_allow_html=True)

# ================= CUSTOM CSS =================
st.markdown("""
<style>
.main .block-container { padding-top: 1.5rem; max-width: 1400px; }

.page-header {
    background: linear-gradient(135deg, #1a1f2e, #0E1117);
    border-radius: 16px;
    padding: 2rem;
    margin-bottom: 2rem;
    border: 1px solid rgba(124, 58, 237, 0.3);
    text-align: center;
}



.page-subtitle {
    color: #9CA3AF;
    font-size: 1.1rem;
}

.section-header {
    background: linear-gradient(90deg, rgba(124,58,237,0.2), transparent);
    border-left: 4px solid #7C3AED;
    padding: 1rem 1.5rem;
    margin: 2rem 0 1.5rem 0;
    border-radius: 0 12px 12px 0;
}

.section-title {
    font-size: 1.4rem;
    font-weight: 700;
    color: #FFFFFF;
}

.section-desc {
    color: #9CA3AF;
    font-size: 0.9rem;
}

.graph-container {
    background: rgba(255,255,255,0.02);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 12px;
    padding: 1rem;
    margin-bottom: 1.5rem;
}
</style>
""", unsafe_allow_html=True)

# ================= BULLETPROOF PATH DETECTION =================
CURRENT_FILE = Path(__file__).resolve()

PROJECT_DIR = None
for parent in CURRENT_FILE.parents:
    if (parent / "data").exists():
        PROJECT_DIR = parent
        break

if PROJECT_DIR is None:
    st.error("❌ Could not locate project root containing 'data' folder")
    st.stop()

DATA_DIR = PROJECT_DIR / "data"
SURVEY_PATH = DATA_DIR / "Study vs Phone Usage Behavioral Survey.csv"

# ================= DEBUG (SAFE TO REMOVE LATER) =================
st.sidebar.markdown("### 🔧 Path Debug")
st.sidebar.caption(f"Project Dir: {PROJECT_DIR}")
st.sidebar.caption(f"Data Dir Exists: {DATA_DIR.exists()}")
st.sidebar.caption(f"Survey Exists: {SURVEY_PATH.exists()}")

# ================= LOAD & CLEAN DATA =================
def parse_time_to_hours(val):
    """Convert time string 'HH:MM:SS' to decimal hours"""
    if pd.isna(val):
        return np.nan
    val_str = str(val).strip()
    if ':' in val_str:
        parts = val_str.split(':')
        try:
            hours = float(parts[0])
            minutes = float(parts[1]) if len(parts) > 1 else 0
            seconds = float(parts[2]) if len(parts) > 2 else 0
            return hours + minutes/60 + seconds/3600
        except:
            return np.nan
    try:
        return float(val_str)
    except:
        return np.nan

@st.cache_data
def load_and_clean_survey(path: Path):
    df_raw = pd.read_csv(path)

    df = df_raw.rename(columns={
        'How many hours did you study yesterday?': 'study_hours',
        'Rate your focus level while studying': 'focus_level',
        'Rate your understanding/clarity while studying': 'clarity_level',
        'How many hours did you use your phone for entertainment yesterday?': 'phone_hours',
        'Rate your level of distraction during the day': 'distraction_level',
        'How stressed were you yesterday?': 'stress_level',
        'How many hours did you sleep last night?': 'sleep_hours',
        'What was your overall mood today?': 'mood',
        'Which statement describes you best?': 'behavior_label'
    })

    # Time-formatted columns (HH:MM:SS) -> decimal hours
    time_cols = ['study_hours', 'phone_hours', 'sleep_hours']
    for col in time_cols:
        if col in df.columns:
            df[col] = df[col].apply(parse_time_to_hours)
    
    # Rating columns (already numeric 1-10)
    rating_cols = ['focus_level', 'clarity_level', 'distraction_level', 'stress_level']
    for col in rating_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # Create labels
    df['label'] = df['behavior_label'].apply(
        lambda x: 1 if 'study' in str(x).lower() else 0
    )

    df['group'] = df['label'].map({
        1: 'Study/Focused',
        0: 'Phone/Distracted'
    })

    # Only drop rows where critical columns are missing
    critical_cols = ['focus_level', 'distraction_level', 'label']
    df = df.dropna(subset=[c for c in critical_cols if c in df.columns])

    return df_raw, df

# ================= FILE CHECK =================
if not SURVEY_PATH.exists():
    st.error(f"❌ Survey file not found:\n{SURVEY_PATH}")
    st.stop()

df_raw, df = load_and_clean_survey(SURVEY_PATH)

# ================= HEADER =================
st.markdown("""
<div class="page-header">
    <div class="page-title">📊 Behavioral Survey Analysis</div>
    <div class="page-subtitle">
        Study vs Phone Usage – Complete Visual Analysis with Key Insights
    </div>
</div>
""", unsafe_allow_html=True)

# ================= METRICS =================
study_group = df[df['label'] == 1]
phone_group = df[df['label'] == 0]

c1, c2, c3, c4 = st.columns(4)
c1.metric("📋 Total Responses", len(df))
c2.metric("📚 Study / Focused", len(study_group))
c3.metric("📱 Phone / Distracted", len(phone_group))
c4.metric("📉 Distraction ↔ Focus",
          f"{df['distraction_level'].corr(df['focus_level']):.3f}")

# =====================================================================
# SECTION 1: KEY RELATIONSHIPS (Graphs 1, 2, 3)
# =====================================================================
st.markdown("""
<div class="section-header">
    <div class="section-title">📈 Section 1: Key Relationships</div>
    <div class="section-desc">Scatter plots showing relationships between variables</div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

# GRAPH 1: Distraction vs Focus (Static Image + Interactive)
with col1:
    st.markdown("#### 1️⃣ Distraction vs Focus ⭐ KEY")
    
    # Static image from notebook
    distraction_focus_img = PROJECT_DIR / "outputs" / "distraction_vs_focus.png"
    if distraction_focus_img.exists():
        st.image(str(distraction_focus_img), use_container_width=True)
    
    st.caption("⚠️ KEY INSIGHT: Higher distraction levels strongly reduce focus")
    
    # Expandable interactive chart
    with st.expander("📊 Click to View Interactive Chart"):
        fig = px.scatter(
            df, x='distraction_level', y='focus_level',
            color='group', 
            color_discrete_map={'Study/Focused':'#2ecc71', 'Phone/Distracted':'#e74c3c'},
            template='plotly_dark', opacity=0.7
        )
        fig.update_traces(marker=dict(size=12))
        fig.update_layout(
            xaxis_title="Distraction Level (1-10)", 
            yaxis_title="Focus Level (1-10)",
            height=280
        )
        st.plotly_chart(fig, use_container_width=True, key="interactive_distraction_focus")

# GRAPH 2: Phone Usage vs Focus (Static Image + Interactive)
with col2:
    st.markdown("#### 2️⃣ Phone Usage vs Focus")
    
    # Static image from notebook
    phone_focus_img = PROJECT_DIR / "outputs" / "phone_usage_vs_focus.png"
    if phone_focus_img.exists():
        st.image(str(phone_focus_img), use_container_width=True)
    
    st.caption("📊 Shows trend between daily phone usage and reported focus levels")
    
    # Expandable interactive chart
    with st.expander("📊 Click to View Interactive Chart"):
        fig = px.scatter(
            df, x='phone_hours', y='focus_level',
            color='group',
            color_discrete_map={'Study/Focused':'#2ecc71', 'Phone/Distracted':'#e74c3c'},
            template='plotly_dark', opacity=0.7
        )
        fig.update_traces(marker=dict(size=12))
        fig.update_layout(
            xaxis_title="Phone Usage (Hours)", 
            yaxis_title="Focus Level (1-10)",
            height=280
        )
        st.plotly_chart(fig, use_container_width=True, key="interactive_phone_focus")

# GRAPH 3: Multi-Variable Pair Plot (Static Image + Interactive)
st.markdown("#### 3️⃣ Multi-Variable Relationships by Cognitive State (Pair Plot)")

# Static image from notebook
pairplot_img = PROJECT_DIR / "outputs" / "pairplot_multi_variable.png"
if pairplot_img.exists():
    st.image(str(pairplot_img), use_container_width=True)

st.caption("🔍 Comprehensive view of relationships between behavioral and psychological variables")

# Expandable interactive chart
with st.expander("📊 Click to View Interactive Chart"):
    vars_plot = ['sleep_hours', 'phone_hours', 'focus_level', 'stress_level']
    fig = px.scatter_matrix(
        df, dimensions=vars_plot, color='group',
        color_discrete_map={'Study/Focused':'#2ecc71', 'Phone/Distracted':'#e74c3c'},
        template='plotly_dark', opacity=0.6
    )
    fig.update_traces(diagonal_visible=False, marker=dict(size=4))
    fig.update_layout(height=350)
    st.plotly_chart(fig, use_container_width=True, key="interactive_pairplot")

# =====================================================================
# SECTION 2: FEATURE DISTRIBUTIONS (Graphs 5, 6, 10)
# =====================================================================
st.markdown("""
<div class="section-header">
    <div class="section-title">📊 Section 2: Feature Distributions</div>
    <div class="section-desc">Box plots and histograms showing data distribution patterns</div>
</div>
""", unsafe_allow_html=True)

# GRAPH 5: Feature Distributions Box Plot
st.markdown("#### 5️⃣ Psychological & Behavioral Feature Distributions")
features = ['study_hours', 'phone_hours', 'sleep_hours', 'focus_level', 'clarity_level', 'distraction_level', 'stress_level']
colors = ['#3498db', '#9b59b6', '#2ecc71', '#f39c12', '#e74c3c', '#1abc9c', '#e67e22']

fig = go.Figure()
for i, f in enumerate(features):
    fig.add_trace(go.Box(y=df[f], name=f.replace('_', ' ').title(), marker_color=colors[i], boxmean='sd'))
fig.update_layout(template='plotly_dark', height=300, yaxis_title="Score / Hours", showlegend=False)
st.plotly_chart(fig, use_container_width=True)
st.caption("📈 Shows distribution, median, quartiles, and outliers for all key features")

# GRAPH: Mood Distribution by Cognitive State

st.markdown("#### 📊 Mood Distribution by Cognitive State")
state_counts = df['group'].value_counts().reset_index()
state_counts.columns = ['group', 'count']
fig = px.bar(
    state_counts, x='group', y='count', color='group',
    color_discrete_map={'Study/Focused':'#2ecc71', 'Phone/Distracted':'#e74c3c'},
    template='plotly_dark', text='count'
)
fig.update_traces(textposition='outside')
fig.update_layout(showlegend=False, height=280)
st.plotly_chart(fig, use_container_width=True)

# =====================================================================
# SECTION 3: DEMOGRAPHIC DISTRIBUTIONS (Phone Usage, Age, Sleep)
# =====================================================================
st.markdown("""
<div class="section-header">
    <div class="section-title">📈 Section 3: Demographic Distributions</div>
    <div class="section-desc">Phone usage patterns, age distribution, and sleep hour analysis from survey</div>
</div>
""", unsafe_allow_html=True)

with st.expander("📊 Click to View All 3 Distribution Charts", expanded=True):
    
    col1, col2, col3 = st.columns(3)
    
    # Phone Usage Distribution
    with col1:
        st.markdown("#### 📱 Phone Usage Distribution")
        fig_phone = px.histogram(
            df, x='phone_hours', nbins=15, 
            template='plotly_dark', 
            color_discrete_sequence=['#e74c3c']
        )
        fig_phone.update_layout(
            xaxis_title="Phone Usage (Hours)", 
            yaxis_title="Frequency", 
            height=280
        )
        st.plotly_chart(fig_phone, use_container_width=True, key="demo_phone_dist")
        
        # Insight
        avg_phone = df['phone_hours'].mean()
        max_phone = df['phone_hours'].max()
        st.caption(f"📊 Average: {avg_phone:.1f}h | Max: {max_phone:.1f}h")
    
    # Age Distribution
    with col2:
        st.markdown("#### 👥 Age Distribution")
        if 'Age' in df.columns:
            fig_age = px.histogram(
                df, x='Age', nbins=10, 
                template='plotly_dark', 
                color_discrete_sequence=['#9b59b6']
            )
            fig_age.update_layout(
                xaxis_title="Age (Years)", 
                yaxis_title="Count", 
                height=350
            )
            st.plotly_chart(fig_age, use_container_width=True, key="demo_age_dist")
            
            avg_age = df['Age'].mean()
            min_age = df['Age'].min()
            max_age = df['Age'].max()
            st.caption(f"📊 Range: {min_age:.0f}-{max_age:.0f} | Average: {avg_age:.1f} years")
        else:
            st.info("Age column not available in dataset")
    
    # Sleep Hours Distribution (Detailed)
    with col3:
        st.markdown("#### 😴 Sleep Hours Distribution")
        # Filter out NaN values for sleep_hours
        sleep_data = df['sleep_hours'].dropna()
        fig_sleep = px.histogram(
            x=sleep_data, nbins=12, 
            template='plotly_dark', 
            color_discrete_sequence=['#3498db']
        )
        fig_sleep.update_layout(
            xaxis_title="Sleep Hours", 
            yaxis_title="Frequency", 
            height=350
        )
        st.plotly_chart(fig_sleep, use_container_width=True, key="demo_sleep_dist")
        
        avg_sleep = sleep_data.mean()
        min_sleep = sleep_data.min()
        max_sleep = sleep_data.max()
        st.caption(f"📊 Average: {avg_sleep:.1f}h | Range: {min_sleep:.1f}-{max_sleep:.1f}h")
    
    # Insights Summary Box
    st.info(f"""
    **📊 Distribution Insights:**
    - 📱 **Phone Usage**: Average {df['phone_hours'].mean():.1f} hours/day - {'High usage pattern' if df['phone_hours'].mean() > 4 else 'Moderate usage pattern'}
    - 😴 **Sleep**: Average {df['sleep_hours'].mean():.1f} hours/night - {'Below recommended' if df['sleep_hours'].mean() < 7 else 'Within healthy range'}
    - 👥 **Cognitive State Split**: {len(study_group)} Study-focused vs {len(phone_group)} Phone-distracted ({len(study_group)/len(df)*100:.1f}% vs {len(phone_group)/len(df)*100:.1f}%)
    """)

# =====================================================================
# SECTION 4: COGNITIVE STATE COMPARISONS (Graphs 7, 8, 9)
# =====================================================================
st.markdown("""
<div class="section-header">
    <div class="section-title">👥 Section 4: Cognitive State Comparisons</div>
    <div class="section-desc">Comparing Study/Focused vs Phone/Distracted groups</div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

# GRAPH 7: Sleep Hours vs Cognitive State
with col1:
    st.markdown("#### 7️⃣ Sleep Hours by Cognitive State")
    fig = px.box(
        df, x='group', y='sleep_hours', color='group',
        color_discrete_map={'Study/Focused':'#2ecc71', 'Phone/Distracted':'#e74c3c'},
        template='plotly_dark'
    )
    fig.update_layout(showlegend=False, height=280, xaxis_title="Cognitive State", yaxis_title="Sleep Hours")
    st.plotly_chart(fig, use_container_width=True)

# GRAPH 8: Phone Usage Across Cognitive States
with col2:
    st.markdown("#### 8️⃣ Phone Usage by Cognitive State")
    fig = px.box(
        df, x='group', y='phone_hours', color='group',
        color_discrete_map={'Study/Focused':'#2ecc71', 'Phone/Distracted':'#e74c3c'},
        template='plotly_dark'
    )
    fig.update_layout(showlegend=False, height=280, xaxis_title="Cognitive State", yaxis_title="Phone Hours")
    st.plotly_chart(fig, use_container_width=True)

# GRAPH 9: Average Focus Level by Cognitive State
st.markdown("#### 9️⃣ Average Focus Level: Study vs Phone")
avg_focus = df.groupby('group')['focus_level'].agg(['mean', 'std']).reset_index()
avg_focus.columns = ['group', 'mean', 'std']

fig = go.Figure()
colors_map = {'Study/Focused': '#2ecc71', 'Phone/Distracted': '#e74c3c'}
for _, row in avg_focus.iterrows():
    fig.add_trace(go.Bar(
        x=[row['group']], y=[row['mean']], name=row['group'],
        marker_color=colors_map[row['group']], 
        text=f"{row['mean']:.2f}",
        textposition='outside',
        error_y=dict(type='data', array=[row['std']], visible=True)
    ))
fig.update_layout(template='plotly_dark', showlegend=False, height=280, yaxis_title="Average Focus Level")
st.plotly_chart(fig, use_container_width=True)
st.caption("📊 Clear difference in average focus levels between groups (with standard deviation error bars)")

# Key Insights Box
st.info(f"""
**📊 Group Statistics:**
- **Study/Focused Group**: Avg Focus = **{study_group['focus_level'].mean():.2f}** | Avg Phone = **{study_group['phone_hours'].mean():.2f}h** | Avg Sleep = **{study_group['sleep_hours'].mean():.2f}h**
- **Phone/Distracted Group**: Avg Focus = **{phone_group['focus_level'].mean():.2f}** | Avg Phone = **{phone_group['phone_hours'].mean():.2f}h** | Avg Sleep = **{phone_group['sleep_hours'].mean():.2f}h**
""")

# =====================================================================
# SECTION 5: CORRELATION ANALYSIS (Graph 4)
# =====================================================================
st.markdown("""
<div class="section-header">
    <div class="section-title">🔗 Section 5: Correlation Analysis</div>
    <div class="section-desc">Heatmap showing strength and direction of all variable relationships</div>
</div>
""", unsafe_allow_html=True)

# GRAPH 4: Correlation Matrix Heatmap
st.markdown("#### 4️⃣ Survey Feature Correlation Matrix")
numeric_df = df.select_dtypes(include=[np.number]).drop(columns=['label'], errors='ignore')
corr_matrix = numeric_df.corr()

fig = px.imshow(
    corr_matrix, text_auto='.2f', 
    color_continuous_scale='RdBu_r',
    template='plotly_dark', aspect='auto', 
    zmin=-1, zmax=1
)
fig.update_layout(height=350)
st.plotly_chart(fig, use_container_width=True)
st.caption("🎨 Color scheme: Blue = Negative correlation, Red = Positive correlation")

# Key Correlations
corr_df = df['distraction_level'].corr(df['focus_level'])
corr_pf = df['phone_hours'].corr(df['focus_level'])
corr_sf = df['sleep_hours'].corr(df['focus_level'])

col1, col2, col3 = st.columns(3)
col1.metric("Distraction ↔ Focus", f"{corr_df:.3f}", "Negative" if corr_df < 0 else "Positive")
col2.metric("Phone ↔ Focus", f"{corr_pf:.3f}", "Negative" if corr_pf < 0 else "Positive")
col3.metric("Sleep ↔ Focus", f"{corr_sf:.3f}", "Negative" if corr_sf < 0 else "Positive")

# =====================================================================
# SECTION 6: DATASET ACCESS
# =====================================================================
st.markdown("""
<div class="section-header">
    <div class="section-title">📋 Section 6: Dataset Access</div>
    <div class="section-desc">View and download the survey data</div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])

with col1:
    st.markdown(f"**File:** `Study vs Phone Usage Behavioral Survey.csv`")
    st.markdown(f"**Shape:** {len(df_raw)} rows × {len(df_raw.columns)} columns")
    st.dataframe(df_raw, use_container_width=True, height=300)

with col2:
    st.markdown("**📥 Download Options**")
    csv_raw = df_raw.to_csv(index=False).encode('utf-8')
    st.download_button("Download Raw CSV", csv_raw, "survey_raw.csv", "text/csv", use_container_width=True)
    
    csv_clean = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download Cleaned CSV", csv_clean, "survey_cleaned.csv", "text/csv", use_container_width=True)

