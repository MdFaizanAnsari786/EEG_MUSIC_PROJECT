import os
import sys
import streamlit as st

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Brain Music | Neuro-Sonification",
    page_icon="🎵",
    layout="wide"
)

# Import and apply theme
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sky_blue_theme import DARK_MODE_CSS
st.markdown(DARK_MODE_CSS, unsafe_allow_html=True)

# ================= ADDITIONAL CSS =================
st.markdown("""
<style>
    .audio-card {
        background: rgba(14, 165, 233, 0.08);
        backdrop-filter: blur(16px);
        border: 1px solid rgba(125, 211, 252, 0.15);
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        height: 100%;
    }
    
    .audio-card.study {
        border-color: rgba(52, 211, 153, 0.4);
        background: rgba(52, 211, 153, 0.08);
    }
    
    .audio-card.phone {
        border-color: rgba(248, 113, 113, 0.4);
        background: rgba(248, 113, 113, 0.08);
    }
    
    .album-art {
        width: 150px;
        height: 150px;
        border-radius: 16px;
        margin: 0 auto 1.5rem;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 4rem;
    }
    
    .album-art.study {
        background: linear-gradient(135deg, #34d399 0%, #10b981 100%);
        box-shadow: 0 10px 40px rgba(52, 211, 153, 0.3);
    }
    
    .album-art.phone {
        background: linear-gradient(135deg, #f87171 0%, #ef4444 100%);
        box-shadow: 0 10px 40px rgba(248, 113, 113, 0.3);
    }
    
    .audio-title {
        font-size: 1.5rem;
        font-weight: 700;
        color: #f0f9ff;
        margin-bottom: 0.5rem;
    }
    
    .audio-desc {
        color: #bae6fd;
        font-size: 0.95rem;
        margin-bottom: 1.5rem;
        line-height: 1.5;
    }
    
    .mfcc-section {
        background: rgba(14, 165, 233, 0.05);
        border-radius: 16px;
        padding: 1.5rem;
        margin-top: 2rem;
    }
    
    .music-info {
        display: flex;
        gap: 1rem;
        flex-wrap: wrap;
        justify-content: center;
        margin-top: 1rem;
    }
    
    .info-tag {
        background: rgba(125, 211, 252, 0.15);
        border: 1px solid rgba(125, 211, 252, 0.2);
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        color: #7dd3fc;
    }
</style>
""", unsafe_allow_html=True)

# ================= PATHS =================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(BASE_DIR)
OUTPUTS_DIR = os.path.join(PROJECT_DIR, "outputs")

study_wav = os.path.join(OUTPUTS_DIR, "study_song_full.wav")
phone_wav = os.path.join(OUTPUTS_DIR, "phone_song_full.wav")
study_mfcc = os.path.join(OUTPUTS_DIR, "study_mfcc.png")
phone_mfcc = os.path.join(OUTPUTS_DIR, "phone_mfcc.png")

# ================= HEADER =================
st.markdown("""
<div class="page-header">
    <div class="page-title">🎵 Brain-Generated Music</div>
    <div class="page-subtitle">Listen to music created from EEG brain activity patterns - calm focused vs chaotic distracted</div>
</div>
""", unsafe_allow_html=True)

# ================= AUDIO PLAYERS =================
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="audio-card study">
        <div class="album-art study">🧘</div>
        <div class="audio-title">Focused Mind</div>
        <div class="audio-desc">
            Generated from Study/Reading brain patterns.<br>
            Smooth, melodic, and harmonious tones reflecting concentrated attention.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if os.path.exists(study_wav):
        st.audio(study_wav)
    else:
        st.warning("Study audio file not found.")
    
    st.markdown("""
    <div class="music-info">
        <span class="info-tag">🎼 Harmonic</span>
        <span class="info-tag">🎹 Melodic</span>
        <span class="info-tag">🌊 Smooth</span>
        <span class="info-tag">📚 Focus State</span>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="audio-card phone">
        <div class="album-art phone">📱</div>
        <div class="audio-title">Distracted Mind</div>
        <div class="audio-desc">
            Generated from Phone/Scrolling brain patterns.<br>
            Erratic, dissonant, and chaotic tones reflecting scattered attention.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if os.path.exists(phone_wav):
        st.audio(phone_wav)
    else:
        st.warning("Phone audio file not found.")
    
    st.markdown("""
    <div class="music-info">
        <span class="info-tag">🔊 Chaotic</span>
        <span class="info-tag">⚡ Erratic</span>
        <span class="info-tag">🌀 Dissonant</span>
        <span class="info-tag">📱 Distracted State</span>
    </div>
    """, unsafe_allow_html=True)

# ================= MFCC ANALYSIS =================
st.markdown('<div class="section-title">🔬 MFCC Spectral Analysis</div>', unsafe_allow_html=True)

st.markdown("""
**MFCC (Mel-Frequency Cepstral Coefficients)** are features commonly used in audio analysis to represent 
the short-term power spectrum of a sound. They help visualize the tonal quality differences between 
focused and distracted brain-generated music.
""")

tab1, tab2 = st.tabs(["📚 Study MFCC", "📱 Phone MFCC"])

with tab1:
    if os.path.exists(study_mfcc):
        st.image(study_mfcc, caption="MFCC Analysis - Study/Focused Brain Music", use_container_width=True)
        st.markdown("""
        **Observations:**
        - More uniform and structured patterns
        - Consistent energy distribution across frequencies
        - Reflects the organized nature of focused thinking
        """)
    else:
        st.info("Study MFCC image not found.")

with tab2:
    if os.path.exists(phone_mfcc):
        st.image(phone_mfcc, caption="MFCC Analysis - Phone/Distracted Brain Music", use_container_width=True)
        st.markdown("""
        **Observations:**
        - More scattered and irregular patterns
        - Variable energy distribution
        - Reflects the chaotic nature of distracted thinking
        """)
    else:
        st.info("Phone MFCC image not found.")

# ================= MFCC COMPARISON INSIGHTS =================
st.markdown('<div class="section-title">📊 MFCC Comparison: Study vs Phone</div>', unsafe_allow_html=True)

st.markdown("""
<style>
    .mfcc-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 0.6rem;
        margin-bottom: 1rem;
    }
    @media (max-width: 768px) {
        .mfcc-grid { grid-template-columns: repeat(2, 1fr); }
    }
    .mfcc-card {
        background: rgba(14, 165, 233, 0.08);
        border: 1px solid rgba(125, 211, 252, 0.15);
        border-radius: 10px;
        padding: 0.6rem;
        text-align: center;
    }
    .mfcc-num {
        font-size: 0.7rem;
        color: #7dd3fc;
        font-weight: 600;
        margin-bottom: 0.3rem;
    }
    .mfcc-vals {
        font-size: 0.65rem;
        line-height: 1.4;
    }
    .v-study { color: #34d399; }
    .v-phone { color: #f87171; }
    .v-diff { color: #fbbf24; font-weight: 600; }
    .mfcc-summary {
        background: rgba(52, 211, 153, 0.05);
        border: 1px solid rgba(52, 211, 153, 0.2);
        border-radius: 12px;
        padding: 1rem;
        margin-top: 0.8rem;
    }
    .summary-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1rem;
    }
    .summary-col h4 {
        font-size: 0.9rem;
        margin: 0 0 0.5rem 0;
    }
    .summary-col p {
        font-size: 0.8rem;
        color: #bae6fd;
        margin: 0;
        line-height: 1.5;
    }
</style>

<div class="mfcc-grid">
    <div class="mfcc-card">
        <div class="mfcc-num">MFCC1</div>
        <div class="mfcc-vals"><span class="v-study">S:-7.64</span> <span class="v-phone">P:-1.59</span><br><span class="v-diff">Δ-6.05</span></div>
    </div>
    <div class="mfcc-card">
        <div class="mfcc-num">MFCC2</div>
        <div class="mfcc-vals"><span class="v-study">S:30.13</span> <span class="v-phone">P:26.63</span><br><span class="v-diff">Δ+3.50</span></div>
    </div>
    <div class="mfcc-card">
        <div class="mfcc-num">MFCC3</div>
        <div class="mfcc-vals"><span class="v-study">S:-19.83</span> <span class="v-phone">P:-34.37</span><br><span class="v-diff">Δ+14.54</span></div>
    </div>
    <div class="mfcc-card" style="border-color: rgba(251, 191, 36, 0.4);">
        <div class="mfcc-num">MFCC4 ⭐</div>
        <div class="mfcc-vals"><span class="v-study">S:-2.30</span> <span class="v-phone">P:-26.69</span><br><span class="v-diff">Δ+24.39</span></div>
    </div>
    <div class="mfcc-card">
        <div class="mfcc-num">MFCC5</div>
        <div class="mfcc-vals"><span class="v-study">S:-9.80</span> <span class="v-phone">P:9.24</span><br><span class="v-diff">Δ-19.03</span></div>
    </div>
    <div class="mfcc-card">
        <div class="mfcc-num">MFCC6</div>
        <div class="mfcc-vals"><span class="v-study">S:-25.73</span> <span class="v-phone">P:-24.86</span><br><span class="v-diff">Δ-0.87</span></div>
    </div>
    <div class="mfcc-card">
        <div class="mfcc-num">MFCC7</div>
        <div class="mfcc-vals"><span class="v-study">S:-10.40</span> <span class="v-phone">P:-22.99</span><br><span class="v-diff">Δ+12.59</span></div>
    </div>
    <div class="mfcc-card">
        <div class="mfcc-num">MFCC8</div>
        <div class="mfcc-vals"><span class="v-study">S:-15.26</span> <span class="v-phone">P:-17.72</span><br><span class="v-diff">Δ+2.46</span></div>
    </div>
    <div class="mfcc-card">
        <div class="mfcc-num">MFCC9</div>
        <div class="mfcc-vals"><span class="v-study">S:-25.41</span> <span class="v-phone">P:-12.61</span><br><span class="v-diff">Δ-12.80</span></div>
    </div>
    <div class="mfcc-card">
        <div class="mfcc-num">MFCC10</div>
        <div class="mfcc-vals"><span class="v-study">S:-8.86</span> <span class="v-phone">P:-18.24</span><br><span class="v-diff">Δ+9.38</span></div>
    </div>
    <div class="mfcc-card">
        <div class="mfcc-num">MFCC11</div>
        <div class="mfcc-vals"><span class="v-study">S:0.84</span> <span class="v-phone">P:4.42</span><br><span class="v-diff">Δ-3.58</span></div>
    </div>
    <div class="mfcc-card">
        <div class="mfcc-num">MFCC12</div>
        <div class="mfcc-vals"><span class="v-study">S:0.23</span> <span class="v-phone">P:2.04</span><br><span class="v-diff">Δ-1.82</span></div>
    </div>
    <div class="mfcc-card">
        <div class="mfcc-num">MFCC13</div>
        <div class="mfcc-vals"><span class="v-study">S:-4.10</span> <span class="v-phone">P:10.36</span><br><span class="v-diff">Δ-14.46</span></div>
    </div>
</div>

<div class="mfcc-summary">
    <div class="summary-grid">
        <div class="summary-col">
            <h4 style="color: #34d399;">📚 Study (Focused)</h4>
            <p>Stable energy • Smoother transitions • Structured patterns • Harmonic tones</p>
        </div>
        <div class="summary-col">
            <h4 style="color: #f87171;">📱 Phone (Distracted)</h4>
            <p>Variable energy • Abrupt changes • Irregular patterns • Chaotic tones</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ================= DETAILED MFCC INSIGHTS =================
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style="background: rgba(52, 211, 153, 0.08); border: 1px solid rgba(52, 211, 153, 0.3); border-radius: 12px; padding: 1rem; margin-bottom: 1rem;">
        <div style="font-size: 1rem; font-weight: 600; color: #34d399; margin-bottom: 0.8rem;">📚 Study/Focused State Characteristics</div>
        <div style="background: rgba(52, 211, 153, 0.1); border-left: 3px solid #34d399; padding: 0.6rem 0.8rem; margin: 0.5rem 0; border-radius: 0 6px 6px 0;">
            <strong style="color: #34d399;">Lower MFCC1 (-7.64):</strong> <span style="color: #bae6fd; font-size: 0.85rem;">Indicates more stable, consistent energy levels reflecting focused attention</span>
        </div>
        <div style="background: rgba(52, 211, 153, 0.1); border-left: 3px solid #34d399; padding: 0.6rem 0.8rem; margin: 0.5rem 0; border-radius: 0 6px 6px 0;">
            <strong style="color: #34d399;">Higher MFCC2 (30.13):</strong> <span style="color: #bae6fd; font-size: 0.85rem;">Smoother spectral transitions producing more melodic, harmonious tones</span>
        </div>
        <div style="background: rgba(52, 211, 153, 0.1); border-left: 3px solid #34d399; padding: 0.6rem 0.8rem; margin: 0.5rem 0; border-radius: 0 6px 6px 0;">
            <strong style="color: #34d399;">Balanced MFCC4 (-2.30):</strong> <span style="color: #bae6fd; font-size: 0.85rem;">Well-organized spectral details with structured patterns</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background: rgba(248, 113, 113, 0.08); border: 1px solid rgba(248, 113, 113, 0.3); border-radius: 12px; padding: 1rem; margin-bottom: 1rem;">
        <div style="font-size: 1rem; font-weight: 600; color: #f87171; margin-bottom: 0.8rem;">📱 Phone/Distracted State Characteristics</div>
        <div style="background: rgba(248, 113, 113, 0.1); border-left: 3px solid #f87171; padding: 0.6rem 0.8rem; margin: 0.5rem 0; border-radius: 0 6px 6px 0;">
            <strong style="color: #f87171;">Higher MFCC1 (-1.59):</strong> <span style="color: #bae6fd; font-size: 0.85rem;">More variable energy levels reflecting erratic attention patterns</span>
        </div>
        <div style="background: rgba(248, 113, 113, 0.1); border-left: 3px solid #f87171; padding: 0.6rem 0.8rem; margin: 0.5rem 0; border-radius: 0 6px 6px 0;">
            <strong style="color: #f87171;">Lower MFCC3 (-34.37):</strong> <span style="color: #bae6fd; font-size: 0.85rem;">More abrupt spectral changes producing dissonant, chaotic sounds</span>
        </div>
        <div style="background: rgba(248, 113, 113, 0.1); border-left: 3px solid #f87171; padding: 0.6rem 0.8rem; margin: 0.5rem 0; border-radius: 0 6px 6px 0;">
            <strong style="color: #f87171;">Extreme MFCC4 (-26.69):</strong> <span style="color: #bae6fd; font-size: 0.85rem;">Highly irregular spectral details showing fragmented patterns</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# What This Means Section
st.markdown("""
<div style="background: rgba(14, 165, 233, 0.08); border: 1px solid rgba(125, 211, 252, 0.2); border-radius: 12px; padding: 1rem; margin-top: 0.5rem;">
    <div style="font-size: 1rem; font-weight: 600; color: #fbbf24; margin-bottom: 0.6rem;">🧠 What This Means</div>
    <p style="color: #bae6fd; line-height: 1.6; margin: 0; font-size: 0.9rem;">
        The MFCC analysis reveals distinct acoustic fingerprints for different cognitive states. 
        <strong style="color: #34d399;">Focused brain activity</strong> produces music with 
        <em>smoother spectral characteristics</em>, more <em>harmonic structure</em>, and 
        <em>consistent energy distribution</em>. In contrast, 
        <strong style="color: #f87171;">distracted brain activity</strong> generates music with 
        <em>irregular spectral patterns</em>, <em>abrupt tonal changes</em>, and 
        <em>variable energy levels</em> — reflecting the fragmented nature of attention during phone use.
    </p>
</div>
""", unsafe_allow_html=True)

# ================= HOW IT WORKS =================
st.markdown('<div class="section-title">💡 How Brain Music is Generated</div>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div style="text-align: center; padding: 1rem;">
        <div style="font-size: 2.5rem; margin-bottom: 1rem;">📡</div>
        <div style="font-weight: 600; color: #00D4FF; margin-bottom: 0.5rem;">1. EEG Signals</div>
        <div style="font-size: 0.85rem; color: #9CA3AF;">Brain's electrical activity captured during different cognitive states</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="text-align: center; padding: 1rem;">
        <div style="font-size: 2.5rem; margin-bottom: 1rem;">🔢</div>
        <div style="font-weight: 600; color: #00D4FF; margin-bottom: 0.5rem;">2. Band Powers</div>
        <div style="font-size: 0.85rem; color: #9CA3AF;">Delta, Theta, Alpha, Beta, Gamma frequencies extracted</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div style="text-align: center; padding: 1rem;">
        <div style="font-size: 2.5rem; margin-bottom: 1rem;">🎼</div>
        <div style="font-weight: 600; color: #00D4FF; margin-bottom: 0.5rem;">3. Note Mapping</div>
        <div style="font-size: 0.85rem; color: #9CA3AF;">EEG features mapped to musical notes, tempo, and dynamics</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div style="text-align: center; padding: 1rem;">
        <div style="font-size: 2.5rem; margin-bottom: 1rem;">🎵</div>
        <div style="font-weight: 600; color: #00D4FF; margin-bottom: 0.5rem;">4. Audio Output</div>
        <div style="font-size: 0.85rem; color: #9CA3AF;">MIDI converted to audio reflecting brain state characteristics</div>
    </div>
    """, unsafe_allow_html=True)
