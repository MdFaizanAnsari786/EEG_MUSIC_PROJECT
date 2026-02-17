import os
import sys
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import joblib

st.set_page_config(page_title="EEG Prediction", page_icon="🎯", layout="wide")

# Import and apply theme
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sky_blue_theme import DARK_MODE_CSS
st.markdown(DARK_MODE_CSS, unsafe_allow_html=True)

st.markdown("""
<style>
    .prediction-card { 
        background: rgba(14, 165, 233, 0.08); 
        backdrop-filter: blur(16px);
        border: 1px solid rgba(125, 211, 252, 0.2); 
        border-radius: 16px; 
        padding: 1.5rem; 
        text-align: center; 
    }
    .prediction-card.study { border-color: rgba(52, 211, 153, 0.4); background: rgba(52, 211, 153, 0.08); }
    .prediction-card.phone { border-color: rgba(248, 113, 113, 0.4); background: rgba(248, 113, 113, 0.08); }
    .confidence-bar { height: 8px; background: rgba(125, 211, 252, 0.2); border-radius: 4px; overflow: hidden; margin-top: 0.5rem; }
    .confidence-fill { height: 100%; border-radius: 4px; }
</style>
""", unsafe_allow_html=True)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(BASE_DIR)
DATA_PATH = os.path.join(PROJECT_DIR, "data", "realistic_combined_eeg_10000_enhanced.csv")
MODEL_PATH = os.path.join(PROJECT_DIR, "models", "final_eeg_model.joblib")
SCALER_PATH = os.path.join(PROJECT_DIR, "models", "scaler.joblib")
OUTPUTS_DIR = os.path.join(PROJECT_DIR, "outputs")

@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

@st.cache_resource
def load_model_and_scaler():
    return joblib.load(MODEL_PATH), joblib.load(SCALER_PATH)

df = load_data()
model, scaler = load_model_and_scaler()

eeg_features = ["delta", "theta", "alpha", "beta", "gamma", "delta_rel", "theta_rel", "alpha_rel", "beta_rel", "gamma_rel",
                "alpha_beta_ratio", "theta_beta_ratio", "engagement_index", "fatigue", "workload", "calmness"]

st.markdown('<div class="page-header"><div class="page-title">🎯 EEG Prediction & Analysis</div></div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("### 🔧 Sample Selection")
    idx = st.number_input("Choose sample index", min_value=0, max_value=len(df)-1, value=0, step=1)
    st.markdown("---")
    st.caption(f"📊 Total: {len(df):,} | 📚 Study: {len(df[df['label']==1]):,} | 📱 Phone: {len(df[df['label']==0]):,}")

row = df.iloc[idx]
true_label = int(row["label"])

# Prediction
X_row = row[eeg_features].values.reshape(1, -1)
X_row_scaled = scaler.transform(X_row)
pred_label = int(model.predict(X_row_scaled)[0])
proba = model.predict_proba(X_row_scaled)[0] if hasattr(model, "predict_proba") else [0.5, 0.5]
study_prob, phone_prob = float(proba[1]), float(proba[0])

# Prediction Cards
col1, col2, col3 = st.columns(3)
with col1:
    cls = "study" if true_label == 1 else "phone"
    icon = "📚" if true_label == 1 else "📱"
    st.markdown(f'<div class="prediction-card {cls}"><div style="color:#9CA3AF">Ground Truth</div><div style="font-size:3rem">{icon}</div><div style="font-weight:700;color:#fff">{"Study" if true_label==1 else "Phone"}</div></div>', unsafe_allow_html=True)

with col2:
    cls = "study" if pred_label == 1 else "phone"
    icon = "📚" if pred_label == 1 else "📱"
    status = "✅" if pred_label == true_label else "❌"
    st.markdown(f'<div class="prediction-card {cls}"><div style="color:#9CA3AF">Prediction {status}</div><div style="font-size:3rem">{icon}</div><div style="font-weight:700;color:#fff">{"Study" if pred_label==1 else "Phone"}</div></div>', unsafe_allow_html=True)

with col3:
    st.markdown(f'''<div class="prediction-card">
        <div style="color:#9CA3AF">Confidence</div>
        <div style="margin-top:1rem"><span style="color:#10B981">📚 Study: {study_prob:.1%}</span></div>
        <div class="confidence-bar"><div class="confidence-fill" style="width:{study_prob*100}%;background:#10B981"></div></div>
        <div style="margin-top:1rem"><span style="color:#EF4444">📱 Phone: {phone_prob:.1%}</span></div>
        <div class="confidence-bar"><div class="confidence-fill" style="width:{phone_prob*100}%;background:#EF4444"></div></div>
    </div>''', unsafe_allow_html=True)

# Tabs for different sections
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📈 EEG Waveform", 
    "🌊 Segment Analysis", 
    "📊 Multi-Window Analysis", 
    "📋 EDA Visualizations", 
    "📁 Dataset", 
    "🔢 Feature Values"
])

with tab1:
    t = np.linspace(0, 2, 512, endpoint=False)
    wave = sum(row[f"{b}_rel"] * np.sin(2*np.pi*f*t) for b, f in [("delta",2),("theta",6),("alpha",10),("beta",20),("gamma",40)])
    wave += 0.05 * np.random.randn(len(t))
    wave /= (np.max(np.abs(wave)) + 1e-9)
    
    fig, ax = plt.subplots(figsize=(12, 4))
    fig.patch.set_facecolor('#0E1117')
    ax.set_facecolor('#0E1117')
    color = '#10B981' if true_label == 1 else '#EF4444'
    ax.plot(t, wave, color=color, linewidth=1.5)
    ax.fill_between(t, wave, alpha=0.2, color=color)
    ax.set_title(f"EEG Waveform - Sample #{idx}", color='white', fontweight='bold')
    ax.set_xlabel("Time (s)", color='#9CA3AF')
    ax.set_ylabel("Amplitude", color='#9CA3AF')
    ax.tick_params(colors='#9CA3AF')
    for spine in ['top','right']: ax.spines[spine].set_visible(False)
    for spine in ['bottom','left']: ax.spines[spine].set_color('#333')
    ax.grid(True, alpha=0.2, color='#333')
    st.pyplot(fig)
    plt.close(fig)

# ==================== TAB 2: SEGMENT ANALYSIS ====================
with tab2:
    st.markdown('<div class="section-title">🌊 Wave Segment Analysis (1-Second Window)</div>', unsafe_allow_html=True)
    st.info("Analyzing EEG-like alpha waves (8-13 Hz) comparing Study (focused) vs Play (distracted) states")
    
    # Settings
    fs = 128  # Sampling frequency
    vis_duration = 2
    analysis_duration = 1
    t_vis = np.linspace(0, vis_duration, fs * vis_duration)
    window_size = fs
    t_window = np.linspace(0, analysis_duration, window_size)
    
    # Generate alpha waves
    def generate_alpha_wave(state="study"):
        base_freq = 10
        if state == "study":
            noise = np.random.normal(0, 0.2, len(t_vis))
        else:
            noise = np.random.normal(0, 0.6, len(t_vis))
        return np.sin(2 * np.pi * base_freq * t_vis) + noise
    
    alpha_study = generate_alpha_wave("study")
    alpha_play = generate_alpha_wave("play")
    
    # 2-Second Wave Visualization
    st.markdown("### 📈 Sample Alpha Wave (2 Seconds)")
    fig, ax = plt.subplots(figsize=(12, 4))
    fig.patch.set_facecolor('#0E1117')
    ax.set_facecolor('#0E1117')
    ax.plot(t_vis, alpha_study, label="Study (Focused)", alpha=0.85, color='#10B981')
    ax.plot(t_vis, alpha_play, label="Play (Distracted)", alpha=0.85, color='#EF4444')
    ax.set_title("Sample Alpha Wave: Study vs Play", color='white', fontweight='bold')
    ax.set_xlabel("Time (seconds)", color='#9CA3AF')
    ax.set_ylabel("Amplitude", color='#9CA3AF')
    ax.tick_params(colors='#9CA3AF')
    ax.legend(facecolor='#1a1f2e', edgecolor='#333', labelcolor='white')
    for spine in ax.spines.values(): spine.set_color('#333')
    ax.grid(True, alpha=0.2, color='#333')
    st.pyplot(fig)
    plt.close(fig)
    
    # 1-Second Window
    study_window = alpha_study[:window_size]
    play_window = alpha_play[:window_size]
    
    st.markdown("### 🔍 1-Second Analysis Segment")
    fig, ax = plt.subplots(figsize=(10, 4))
    fig.patch.set_facecolor('#0E1117')
    ax.set_facecolor('#0E1117')
    ax.plot(t_window, study_window, label="Study Window", color='#10B981')
    ax.plot(t_window, play_window, label="Play Window", color='#EF4444')
    ax.set_title("1-Second Alpha Wave Segment (Used for Analysis)", color='white', fontweight='bold')
    ax.set_xlabel("Time (seconds)", color='#9CA3AF')
    ax.set_ylabel("Amplitude", color='#9CA3AF')
    ax.tick_params(colors='#9CA3AF')
    ax.legend(facecolor='#1a1f2e', edgecolor='#333', labelcolor='white')
    for spine in ax.spines.values(): spine.set_color('#333')
    ax.grid(True, alpha=0.2, color='#333')
    st.pyplot(fig)
    plt.close(fig)
    
    # Feature Extraction
    def time_domain_features(window):
        return np.mean(window), np.var(window), np.sum(window ** 2)
    
    def relative_alpha_power(window):
        fft_vals = np.fft.fft(window)
        freqs = np.fft.fftfreq(len(fft_vals), d=1/fs)
        power = np.abs(fft_vals) ** 2
        total_power = power.sum()
        alpha_power = power[(freqs >= 8) & (freqs <= 13)].sum()
        return alpha_power / total_power if total_power != 0 else 0
    
    study_mean, study_var, study_energy = time_domain_features(study_window)
    play_mean, play_var, play_energy = time_domain_features(play_window)
    study_alpha_rel = relative_alpha_power(study_window)
    play_alpha_rel = relative_alpha_power(play_window)
    
    # Results Table
    st.markdown("### 📊 Feature Comparison Table")
    results_df = pd.DataFrame({
        'Metric': ['Mean', 'Variance', 'Energy', 'Relative Alpha Power'],
        'Study (Focused)': [f"{study_mean:.4f}", f"{study_var:.4f}", f"{study_energy:.4f}", f"{study_alpha_rel:.4f}"],
        'Play (Distracted)': [f"{play_mean:.4f}", f"{play_var:.4f}", f"{play_energy:.4f}", f"{play_alpha_rel:.4f}"]
    })
    st.dataframe(results_df, use_container_width=True, hide_index=True)
    
    # Metrics display
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Study Variance", f"{study_var:.4f}", "Lower = Stable")
    col2.metric("Play Variance", f"{play_var:.4f}", "Higher = Noisy", delta_color="inverse")
    col3.metric("Study Alpha Power", f"{study_alpha_rel:.4f}", "Higher = Focused")
    col4.metric("Play Alpha Power", f"{play_alpha_rel:.4f}", "Lower = Distracted", delta_color="inverse")
    
    # Interpretations
    st.success("""
    **🔑 Key Interpretations:**
    - ✅ **Study state** shows lower variance → stable neural activity
    - ⚠️ **Play state** shows higher energy → increased noise and distraction
    - ✅ Higher relative alpha power in study → better focus
    """)

# ==================== TAB 3: MULTI-WINDOW ANALYSIS ====================
with tab3:
    st.markdown('<div class="section-title">📊 Multi-Window Wave Analysis (10 Windows)</div>', unsafe_allow_html=True)
    st.info("Temporal analysis across multiple 1-second windows to track variance and alpha power over time")
    
    # Settings
    fs_mw = 128
    duration_mw = 10
    t_mw = np.linspace(0, duration_mw, int(fs_mw * duration_mw), endpoint=False)
    window_size_mw = fs_mw
    step_size_mw = fs_mw
    
    # Generate waves
    def generate_alpha_wave_mw(state="study"):
        base_freq = 10
        if state == "study":
            noise = np.random.normal(0, 0.2, len(t_mw))
        else:
            noise = np.random.normal(0, 0.6, len(t_mw))
        return np.sin(2 * np.pi * base_freq * t_mw) + noise
    
    alpha_study_mw = generate_alpha_wave_mw("study")
    alpha_play_mw = generate_alpha_wave_mw("play")
    
    # Multi-window analysis
    study_results = []
    play_results = []
    
    for start in range(0, len(alpha_study_mw) - window_size_mw + 1, step_size_mw):
        end = start + window_size_mw
        s_window = alpha_study_mw[start:end]
        p_window = alpha_play_mw[start:end]
        
        s_mean, s_var, s_energy = time_domain_features(s_window)
        s_alpha = relative_alpha_power(s_window)
        p_mean, p_var, p_energy = time_domain_features(p_window)
        p_alpha = relative_alpha_power(p_window)
        
        study_results.append([s_mean, s_var, s_energy, s_alpha])
        play_results.append([p_mean, p_var, p_energy, p_alpha])
    
    study_results = np.array(study_results)
    play_results = np.array(play_results)
    windows = np.arange(1, len(study_results) + 1)
    
    # Summary metrics
    st.markdown("### 📈 Average Values Across All Windows")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**📚 Study (Focused)**")
        st.metric("Variance Avg", f"{study_results[:,1].mean():.4f}")
        st.metric("Energy Avg", f"{study_results[:,2].mean():.4f}")
        st.metric("Rel Alpha Avg", f"{study_results[:,3].mean():.4f}")
    with col2:
        st.markdown("**📱 Play (Distracted)**")
        st.metric("Variance Avg", f"{play_results[:,1].mean():.4f}")
        st.metric("Energy Avg", f"{play_results[:,2].mean():.4f}")
        st.metric("Rel Alpha Avg", f"{play_results[:,3].mean():.4f}")
    
    # Variance Plot
    st.markdown("### 📉 Variance Across Windows")
    fig, ax = plt.subplots(figsize=(12, 4))
    fig.patch.set_facecolor('#0E1117')
    ax.set_facecolor('#0E1117')
    ax.plot(windows, study_results[:,1], label="Study Variance", marker='o', color='#10B981')
    ax.plot(windows, play_results[:,1], label="Play Variance", marker='s', color='#EF4444')
    ax.set_xlabel("Window Number", color='#9CA3AF')
    ax.set_ylabel("Variance", color='#9CA3AF')
    ax.set_title("Variance Across Windows", color='white', fontweight='bold')
    ax.tick_params(colors='#9CA3AF')
    ax.legend(facecolor='#1a1f2e', edgecolor='#333', labelcolor='white')
    for spine in ax.spines.values(): spine.set_color('#333')
    ax.grid(True, alpha=0.2, color='#333')
    st.pyplot(fig)
    plt.close(fig)
    
    # Alpha Power Plot
    st.markdown("### 🧠 Relative Alpha Power Across Windows")
    fig, ax = plt.subplots(figsize=(12, 4))
    fig.patch.set_facecolor('#0E1117')
    ax.set_facecolor('#0E1117')
    ax.plot(windows, study_results[:,3], label="Study Relative Alpha", marker='o', color='#10B981')
    ax.plot(windows, play_results[:,3], label="Play Relative Alpha", marker='s', color='#EF4444')
    ax.set_xlabel("Window Number", color='#9CA3AF')
    ax.set_ylabel("Relative Alpha Power", color='#9CA3AF')
    ax.set_title("Relative Alpha Power Across Windows", color='white', fontweight='bold')
    ax.tick_params(colors='#9CA3AF')
    ax.legend(facecolor='#1a1f2e', edgecolor='#333', labelcolor='white')
    for spine in ax.spines.values(): spine.set_color('#333')
    ax.grid(True, alpha=0.2, color='#333')
    st.pyplot(fig)
    plt.close(fig)
    
    # Full Results Table
    st.markdown("### 📋 Window-by-Window Results")
    window_df = pd.DataFrame({
        'Window': windows,
        'Study Variance': [f"{v:.4f}" for v in study_results[:,1]],
        'Play Variance': [f"{v:.4f}" for v in play_results[:,1]],
        'Study Alpha Rel': [f"{v:.4f}" for v in study_results[:,3]],
        'Play Alpha Rel': [f"{v:.4f}" for v in play_results[:,3]]
    })
    st.dataframe(window_df, use_container_width=True, hide_index=True)

with tab4:
    st.markdown('<div class="section-title">📊 EDA Visualizations (from EDA.py)</div>', unsafe_allow_html=True)
    
    # Box Plots
    st.markdown("### 📦 Box Plots - EEG Bands (Study vs Phone)")
    box_cols = st.columns(5)
    bands = ["delta", "theta", "alpha", "beta", "gamma"]
    for i, band in enumerate(bands):
        box_path = os.path.join(OUTPUTS_DIR, f"box_{band}.png")
        if os.path.exists(box_path):
            with box_cols[i]:
                st.image(box_path, caption=band.upper())
    
    st.markdown("---")
    
    # Histograms
    st.markdown("### 📊 Histograms - EEG Band Distributions")
    hist_cols = st.columns(5)
    for i, band in enumerate(bands):
        hist_path = os.path.join(OUTPUTS_DIR, f"hist_{band}.png")
        if os.path.exists(hist_path):
            with hist_cols[i]:
                st.image(hist_path, caption=band.upper())
    
    st.markdown("---")
    
    # Derived Features
    st.markdown("### 🧮 Derived Features Histograms")
    derived = ["alpha_beta_ratio", "theta_beta_ratio", "engagement_index", "fatigue", "workload", "calmness"]
    derived_cols = st.columns(3)
    for i, feat in enumerate(derived):
        path = os.path.join(OUTPUTS_DIR, f"hist_{feat}_derived.png")
        if os.path.exists(path):
            with derived_cols[i % 3]:
                st.image(path, caption=feat.replace("_", " ").title())
    
    st.markdown("---")
    
    # Correlation & Label Distribution
    col1, col2 = st.columns(2)
    with col1:
        corr_path = os.path.join(OUTPUTS_DIR, "correlation_matrix.png")
        if os.path.exists(corr_path):
            st.markdown("### 🔗 Correlation Matrix")
            st.image(corr_path)
    with col2:
        label_path = os.path.join(OUTPUTS_DIR, "label_distribution.png")
        if os.path.exists(label_path):
            st.markdown("### 📈 Label Distribution")
            st.image(label_path)

with tab5:
    st.markdown('<div class="section-title">📋 EEG Dataset Access</div>', unsafe_allow_html=True)
    st.markdown(f"**File:** `realistic_combined_eeg_10000_enhanced.csv`")
    st.markdown(f"**Rows:** {len(df):,} | **Columns:** {len(df.columns)}")
    
    # Data preview
    st.markdown("### Preview (first 100 rows)")
    st.dataframe(df.head(100), use_container_width=True, height=400)
    
    # Download button
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Full CSV", csv, "eeg_data.csv", "text/csv")
    
    # Stats
    st.markdown("### 📊 Dataset Statistics")
    st.dataframe(df.describe())

with tab6:
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**Absolute Band Powers**")
        st.dataframe(pd.DataFrame({f: [f"{row[f]:.4f}"] for f in ["delta","theta","alpha","beta","gamma"]}).T.rename(columns={0:"Value"}))
        st.markdown("**Band Ratios**")
        st.dataframe(pd.DataFrame({f: [f"{row[f]:.4f}"] for f in ["alpha_beta_ratio","theta_beta_ratio"]}).T.rename(columns={0:"Value"}))
    with c2:
        st.markdown("**Relative Band Powers**")
        st.dataframe(pd.DataFrame({f: [f"{row[f]:.4f}"] for f in ["delta_rel","theta_rel","alpha_rel","beta_rel","gamma_rel"]}).T.rename(columns={0:"Value"}))
        st.markdown("**Derived Metrics**")
        st.dataframe(pd.DataFrame({f: [f"{row[f]:.4f}"] for f in ["engagement_index","fatigue","workload","calmness"]}).T.rename(columns={0:"Value"}))

