import os
import sys
import pandas as pd
import streamlit as st
import joblib
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Model Insights", page_icon="🤖", layout="wide")

# Import and apply theme
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sky_blue_theme import DARK_MODE_CSS
st.markdown(DARK_MODE_CSS, unsafe_allow_html=True)

st.markdown("""
<style>
    .metric-card { 
        background: rgba(14, 165, 233, 0.08); 
        backdrop-filter: blur(16px);
        border: 1px solid rgba(125, 211, 252, 0.2); 
        border-radius: 12px; 
        padding: 1.5rem; 
        text-align: center; 
    }
    .accuracy-card { 
        background: rgba(52, 211, 153, 0.08); 
        border: 1px solid rgba(52, 211, 153, 0.3); 
        border-radius: 12px; 
        padding: 1rem; 
        margin: 0.5rem 0; 
    }
    .model-name { font-weight: 700; color: #f0f9ff; font-size: 1.1rem; }
    .accuracy-value { font-size: 2rem; font-weight: 800; color: #34d399; }
</style>
""", unsafe_allow_html=True)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(BASE_DIR)
MODEL_PATH = os.path.join(PROJECT_DIR, "models", "final_eeg_model.joblib")
MODEL_COMPARISON_PATH = os.path.join(PROJECT_DIR, "models", "model_comparison.csv")
OUTPUTS_DIR = os.path.join(PROJECT_DIR, "outputs")

eeg_features = ["delta", "theta", "alpha", "beta", "gamma", "delta_rel", "theta_rel", "alpha_rel", "beta_rel", "gamma_rel",
                "alpha_beta_ratio", "theta_beta_ratio", "engagement_index", "fatigue", "workload", "calmness"]

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH) if os.path.exists(MODEL_PATH) else None

@st.cache_data
def load_model_comparison():
    if os.path.exists(MODEL_COMPARISON_PATH):
        return pd.read_csv(MODEL_COMPARISON_PATH)
    return None

model = load_model()
model_comparison = load_model_comparison()

st.markdown('<div class="page-header"><div class="page-title">🤖 Model Insights</div></div>', unsafe_allow_html=True)

# ================= MODEL ACCURACY SECTION =================
st.markdown('<div class="section-title">🏆 Model Performance Comparison</div>', unsafe_allow_html=True)

if model_comparison is not None:
    # Display accuracy cards for each model
    cols = st.columns(len(model_comparison))
    for i, row in model_comparison.iterrows():
        with cols[i]:
            acc = row['Accuracy'] * 100
            color = "#10B981" if acc >= 99.9 else "#F59E0B" if acc >= 99 else "#EF4444"
            st.markdown(f'''
            <div class="accuracy-card" style="border-color: {color}30; background: linear-gradient(145deg, {color}15, {color}05);">
                <div class="model-name">{row['Model']}</div>
                <div class="accuracy-value" style="color: {color}">{acc:.2f}%</div>
                <div style="color: #9CA3AF; font-size: 0.85rem;">Accuracy</div>
            </div>
            ''', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Detailed metrics table
    st.markdown("### 📊 Detailed Performance Metrics")
    
    # Format the dataframe nicely
    df_display = model_comparison.copy()
    df_display['Accuracy'] = df_display['Accuracy'].apply(lambda x: f"{x*100:.2f}%")
    df_display['Precision'] = df_display['Precision'].apply(lambda x: f"{x*100:.2f}%")
    df_display['Recall'] = df_display['Recall'].apply(lambda x: f"{x*100:.2f}%")
    df_display['F1-score'] = df_display['F1-score'].apply(lambda x: f"{x*100:.2f}%")
    df_display['ROC-AUC'] = df_display['ROC-AUC'].apply(lambda x: f"{x:.4f}")
    
    st.dataframe(df_display, use_container_width=True, hide_index=True)
    
    st.markdown("---")
    
    # Bar chart comparison
    st.markdown("### 📈 Accuracy Comparison Chart")
    fig = px.bar(
        model_comparison, 
        x='Model', 
        y='Accuracy',
        color='Accuracy',
        color_continuous_scale=['#EF4444', '#F59E0B', '#10B981'],
        template='plotly_dark'
    )
    fig.update_layout(
        paper_bgcolor='#0E1117', 
        plot_bgcolor='#0E1117',
        yaxis=dict(tickformat='.1%', range=[0.99, 1.005]),
        showlegend=False
    )
    fig.update_traces(marker_line_width=0)
    st.plotly_chart(fig, use_container_width=True)
    
    # Radar chart for multi-metric comparison
    st.markdown("### 🕸️ Multi-Metric Comparison")
    categories = ['Accuracy', 'Precision', 'Recall', 'F1-score', 'ROC-AUC']
    
    fig = go.Figure()
    colors = ['#00D4FF', '#7C3AED', '#10B981', '#F59E0B', '#EF4444']
    for i, row in model_comparison.iterrows():
        values = [row['Accuracy'], row['Precision'], row['Recall'], row['F1-score'], row['ROC-AUC']]
        values.append(values[0])  # Close the polygon
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories + [categories[0]],
            name=row['Model'],
            line_color=colors[i % len(colors)]
        ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0.99, 1.01]),
            bgcolor='#0E1117'
        ),
        paper_bgcolor='#0E1117',
        font_color='#9CA3AF',
        showlegend=True
    )
    st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("Model comparison data not found.")

# ================= LEARNING CURVES SECTION =================
st.markdown('<div class="section-title">📉 Learning Curves (Accuracy vs Training Size)</div>', unsafe_allow_html=True)

st.markdown("""
<div style="background: rgba(14, 165, 233, 0.08); border: 1px solid rgba(125, 211, 252, 0.15); border-radius: 12px; padding: 1rem; margin-bottom: 1rem;">
    <p style="color: #bae6fd; margin: 0; font-size: 0.9rem;">
        <strong style="color: #7dd3fc;">Learning curves</strong> show how model accuracy changes as training data increases. 
        The gap between training and validation curves indicates overfitting/underfitting.
    </p>
</div>
""", unsafe_allow_html=True)

# Learning curve files
learning_curve_files = [
    ("Logistic Regression", "learning_curve_Logistic_Regression.png"),
    ("Random Forest", "learning_curve_Random_Forest.png"),
    ("CNN 1D", "learning_curve_CNN_1D.png"),
    ("Gradient Boosting", "learning_curve_Gradient_Boosting.png"),
    ("MLP Neural Network", "learning_curve_MLP_Neural_Network.png"),
]

# Check if any learning curve files exist
existing_curves = [(name, f) for name, f in learning_curve_files if os.path.exists(os.path.join(OUTPUTS_DIR, f))]

if existing_curves:
    tabs = st.tabs([name for name, _ in existing_curves])
    for tab, (name, filename) in zip(tabs, existing_curves):
        with tab:
            st.image(os.path.join(OUTPUTS_DIR, filename), caption=f"Learning Curve - {name}", use_container_width=True)
else:
    st.info("Learning curves not found. Run `python src/generate_learning_curves.py` to generate them.")

# Loss Curves Section (MLP, Gradient Boosting, and CNN 1D)
st.markdown('<div class="section-title">📊 Training Loss Curves</div>', unsafe_allow_html=True)

st.markdown("""
<div style="background: rgba(239, 68, 68, 0.08); border: 1px solid rgba(239, 68, 68, 0.2); border-radius: 12px; padding: 1rem; margin-bottom: 1rem;">
    <p style="color: #fecaca; margin: 0; font-size: 0.9rem;">
        <strong style="color: #f87171;">Loss curves</strong> show how the model's error decreases during training. 
        A decreasing curve indicates the model is learning effectively.
    </p>
</div>
""", unsafe_allow_html=True)

mlp_loss_path = os.path.join(OUTPUTS_DIR, "mlp_loss_curve.png")
gb_loss_path = os.path.join(OUTPUTS_DIR, "gb_loss_curve.png")
cnn1d_loss_path = os.path.join(OUTPUTS_DIR, "cnn1d_loss_curve.png")
cnn1d_acc_path = os.path.join(OUTPUTS_DIR, "cnn1d_accuracy_curve.png")

loss_tabs = []
loss_files = []

# Add CNN 1D first (newest model)
if os.path.exists(cnn1d_loss_path):
    loss_tabs.append("🧬 CNN 1D Loss")
    loss_files.append(("cnn1d_loss_curve.png", "CNN 1D - Training & Validation Loss"))

if os.path.exists(cnn1d_acc_path):
    loss_tabs.append("📈 CNN 1D Accuracy")
    loss_files.append(("cnn1d_accuracy_curve.png", "CNN 1D - Training & Validation Accuracy"))

if os.path.exists(mlp_loss_path):
    loss_tabs.append("🧠 MLP Neural Network")
    loss_files.append(("mlp_loss_curve.png", "MLP Neural Network - Training Loss Over Epochs"))

if os.path.exists(gb_loss_path):
    loss_tabs.append("🌲 Gradient Boosting")
    loss_files.append(("gb_loss_curve.png", "Gradient Boosting - Training Loss Over Iterations"))

if loss_tabs:
    tabs = st.tabs(loss_tabs)
    for tab, (filename, caption) in zip(tabs, loss_files):
        with tab:
            st.image(os.path.join(OUTPUTS_DIR, filename), caption=caption, use_container_width=True)
else:
    st.info("Loss curves not found. Run `python src/generate_cnn1d_curves.py` to generate them.")

# ================= FEATURE IMPORTANCE =================
st.markdown('<div class="section-title">📊 Feature Importance</div>', unsafe_allow_html=True)

if model and hasattr(model, 'feature_importances_'):
    imp = pd.DataFrame({'Feature': eeg_features, 'Importance': model.feature_importances_}).sort_values('Importance', ascending=True)
    fig = px.bar(imp, x='Importance', y='Feature', orientation='h', template='plotly_dark')
    fig.update_traces(marker_color='#7C3AED')
    fig.update_layout(paper_bgcolor='#0E1117', plot_bgcolor='#0E1117', height=320)
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Feature importance not available.")

# ================= CONFUSION MATRIX & ROC =================
st.markdown('<div class="section-title">📈 Visual Performance</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    cm_path = os.path.join(OUTPUTS_DIR, "confusion_matrix.png")
    if os.path.exists(cm_path):
        st.markdown("### Confusion Matrix")
        st.image(cm_path, use_container_width=True)

with col2:
    roc_path = os.path.join(OUTPUTS_DIR, "roc_curve.png")
    if os.path.exists(roc_path):
        st.markdown("### ROC Curve")
        st.image(roc_path, use_container_width=True)

# ================= INDIVIDUAL ROC CURVES =================
st.markdown('<div class="section-title">🏆 ROC Curves by Model</div>', unsafe_allow_html=True)

roc_files = [f for f in os.listdir(OUTPUTS_DIR) if f.startswith('roc_') and f.endswith('.png') and f != 'roc_curve.png'] if os.path.exists(OUTPUTS_DIR) else []

if roc_files:
    tabs = st.tabs([f.replace('roc_','').replace('.png','').replace('_',' ') for f in roc_files])
    for tab, f in zip(tabs, roc_files):
        with tab:
            st.image(os.path.join(OUTPUTS_DIR, f), use_container_width=True)

# ================= MODEL INFO =================
st.markdown('<div class="section-title">ℹ️ Model Information</div>', unsafe_allow_html=True)

if model:
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Model Type", type(model).__name__)
    with c2:
        st.metric("Features", len(eeg_features))
    with c3:
        if hasattr(model, 'n_estimators'):
            st.metric("Estimators", model.n_estimators)
        else:
            st.metric("Estimators", "N/A")
