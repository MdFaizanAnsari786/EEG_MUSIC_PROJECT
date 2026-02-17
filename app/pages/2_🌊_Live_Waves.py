import os
import sys
import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Live Waves | Neuro-Sonification",
    page_icon="🌊",
    layout="wide"
)

# Import and apply theme with session state
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sky_blue_theme import DARK_MODE_CSS
st.markdown(DARK_MODE_CSS, unsafe_allow_html=True)

# ================= ADDITIONAL CSS =================
st.markdown("""
<style>
    .control-panel {
        background: rgba(14, 165, 233, 0.08);
        backdrop-filter: blur(16px);
        border: 1px solid rgba(125, 211, 252, 0.15);
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
    }
    
    .wave-legend {
        display: flex;
        gap: 2rem;
        justify-content: center;
        margin-top: 1rem;
    }
    
    .legend-item {
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .legend-dot {
        width: 12px;
        height: 12px;
        border-radius: 50%;
    }
    
    .status-indicator {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 600;
    }
    
    .status-live {
        background: rgba(248, 113, 113, 0.2);
        color: #f87171;
        border: 1px solid rgba(248, 113, 113, 0.3);
    }
    
    .status-paused {
        background: rgba(125, 211, 252, 0.2);
        color: #7dd3fc;
        border: 1px solid rgba(125, 211, 252, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# ================= PATHS =================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(BASE_DIR)
DATA_PATH = os.path.join(PROJECT_DIR, "data", "realistic_combined_eeg_10000_enhanced.csv")

# ================= LOAD DATA =================
@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

df = load_data()

# ================= HEADER =================
st.markdown("""
<div class="page-header">
    <div class="page-title">🌊 Live EEG Waves</div>
    <div class="page-subtitle">Real-time animated visualization comparing Study vs Phone brain patterns</div>
</div>
""", unsafe_allow_html=True)

# ================= INITIALIZE SESSION STATE =================
if 'study_live_wave' not in st.session_state:
    study_row = df[df["label"] == 1].iloc[0]
    phone_row = df[df["label"] == 0].iloc[0]
    
    fs = 256
    seconds = 2
    t = np.linspace(0, seconds, int(seconds * fs), endpoint=False)
    
    study_wave = (
        study_row["delta_rel"] * np.sin(2*np.pi*2*t) +
        study_row["theta_rel"] * np.sin(2*np.pi*6*t) +
        study_row["alpha_rel"] * np.sin(2*np.pi*10*t) +
        study_row["beta_rel"]  * np.sin(2*np.pi*20*t) +
        study_row["gamma_rel"] * np.sin(2*np.pi*40*t)
    )
    study_wave += 0.05 * np.random.randn(len(t))
    study_wave /= (np.max(np.abs(study_wave)) + 1e-9)
    
    phone_wave = (
        phone_row["delta_rel"] * np.sin(2*np.pi*2*t) +
        phone_row["theta_rel"] * np.sin(2*np.pi*6*t) +
        phone_row["alpha_rel"] * np.sin(2*np.pi*10*t) +
        phone_row["beta_rel"]  * np.sin(2*np.pi*20*t) +
        phone_row["gamma_rel"] * np.sin(2*np.pi*40*t)
    )
    phone_wave += 0.05 * np.random.randn(len(t))
    phone_wave /= (np.max(np.abs(phone_wave)) + 1e-9)
    
    st.session_state.study_live_wave = study_wave.copy()
    st.session_state.phone_live_wave = phone_wave.copy()
    st.session_state.t_live = t

# ================= CONTROL PANEL =================
st.markdown('<div class="control-panel">', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns([1, 1, 1, 2])

with col1:
    live_mode = st.toggle("🔴 Live Animation", value=False)

with col2:
    if st.button("🔄 Reset Waves"):
        study_row = df[df["label"] == 1].iloc[0]
        phone_row = df[df["label"] == 0].iloc[0]
        t = st.session_state.t_live
        
        study_wave = (
            study_row["delta_rel"] * np.sin(2*np.pi*2*t) +
            study_row["theta_rel"] * np.sin(2*np.pi*6*t) +
            study_row["alpha_rel"] * np.sin(2*np.pi*10*t) +
            study_row["beta_rel"]  * np.sin(2*np.pi*20*t) +
            study_row["gamma_rel"] * np.sin(2*np.pi*40*t)
        )
        study_wave += 0.05 * np.random.randn(len(t))
        study_wave /= (np.max(np.abs(study_wave)) + 1e-9)
        
        phone_wave = (
            phone_row["delta_rel"] * np.sin(2*np.pi*2*t) +
            phone_row["theta_rel"] * np.sin(2*np.pi*6*t) +
            phone_row["alpha_rel"] * np.sin(2*np.pi*10*t) +
            phone_row["beta_rel"]  * np.sin(2*np.pi*20*t) +
            phone_row["gamma_rel"] * np.sin(2*np.pi*40*t)
        )
        phone_wave += 0.05 * np.random.randn(len(t))
        phone_wave /= (np.max(np.abs(phone_wave)) + 1e-9)
        
        st.session_state.study_live_wave = study_wave.copy()
        st.session_state.phone_live_wave = phone_wave.copy()

with col3:
    if live_mode:
        st.markdown('<div class="status-indicator status-live">🔴 LIVE</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="status-indicator status-paused">⏸️ PAUSED</div>', unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="wave-legend">
        <div class="legend-item">
            <div class="legend-dot" style="background: #10B981;"></div>
            <span style="color: #10B981;">Study / Focused</span>
        </div>
        <div class="legend-item">
            <div class="legend-dot" style="background: #EF4444;"></div>
            <span style="color: #EF4444;">Phone / Distracted</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ================= UPDATE WAVES =================
if live_mode:
    for _ in range(3):
        st.session_state.study_live_wave = np.roll(st.session_state.study_live_wave, -1)
        st.session_state.phone_live_wave = np.roll(st.session_state.phone_live_wave, -1)
        st.session_state.study_live_wave[-1] = st.session_state.study_live_wave[-2] + np.random.normal(0, 0.01)
        st.session_state.phone_live_wave[-1] = st.session_state.phone_live_wave[-2] + np.random.normal(0, 0.03)

# ================= PLOT WAVES =================
fig = make_subplots(
    rows=2, cols=1,
    subplot_titles=("📚 FOCUSED BRAIN (Study / Reading)", "📱 DISTRACTED BRAIN (Phone / Scrolling)"),
    vertical_spacing=0.12
)

# Study wave
fig.add_trace(
    go.Scatter(
        x=st.session_state.t_live,
        y=st.session_state.study_live_wave,
        mode='lines',
        name='Study',
        line=dict(color='#10B981', width=2),
        fill='tozeroy',
        fillcolor='rgba(16, 185, 129, 0.1)'
    ),
    row=1, col=1
)

# Phone wave
fig.add_trace(
    go.Scatter(
        x=st.session_state.t_live,
        y=st.session_state.phone_live_wave,
        mode='lines',
        name='Phone',
        line=dict(color='#EF4444', width=2),
        fill='tozeroy',
        fillcolor='rgba(239, 68, 68, 0.1)'
    ),
    row=2, col=1
)

# Update layout
fig.update_layout(
    height=400,
    showlegend=False,
    paper_bgcolor='#0E1117',
    plot_bgcolor='#0E1117',
    font=dict(color='#9CA3AF'),
    margin=dict(t=60, b=50, l=60, r=40)
)

fig.update_yaxes(range=[-1.5, 1.5], gridcolor='rgba(255,255,255,0.1)', zerolinecolor='rgba(255,255,255,0.2)')
fig.update_xaxes(gridcolor='rgba(255,255,255,0.1)')
fig.update_xaxes(title_text="Time (seconds)", row=2, col=1)
fig.update_yaxes(title_text="Amplitude", row=1, col=1)
fig.update_yaxes(title_text="Amplitude", row=2, col=1)

st.plotly_chart(fig, use_container_width=True)

# ================= EXPLANATION =================
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 📚 Focused Brain Pattern
    - **Smoother, more rhythmic waves**
    - Higher alpha wave presence (relaxed focus)
    - Lower beta variability
    - Consistent attention patterns
    - Associated with deep learning and concentration
    """)

with col2:
    st.markdown("""
    ### 📱 Distracted Brain Pattern
    - **More erratic, irregular waves**
    - Higher theta/beta ratio
    - Frequent attention shifts
    - Increased noise in signals
    - Associated with scattered attention
    """)

# Auto-refresh
if live_mode:
    time.sleep(0.1)
    st.rerun()
