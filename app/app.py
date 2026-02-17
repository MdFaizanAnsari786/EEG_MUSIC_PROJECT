import os
import streamlit as st
import pandas as pd

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="BrainWave | EEG Health Monitor",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================= IMPORT AND APPLY THEME =================
from sky_blue_theme import DARK_MODE_CSS, WAVE_ANIMATION_CODE

# Apply the dark theme CSS
st.markdown(DARK_MODE_CSS, unsafe_allow_html=True)

# ================= OG META TAGS FOR LINK PREVIEW =================
st.markdown("""
<meta property="og:title" content="🧠 BrainWave | EEG Health Monitor" />
<meta property="og:description" content="Advanced EEG Analytics • Cognitive State Detection • Study vs Phone Detection • MSc Research Project" />
<meta property="og:image" content="https://raw.githubusercontent.com/MdFaizanAnsari786/EEG_MUSIC_PROJECT/main/app/brain_futuristic.jpg" />
<meta property="og:url" content="https://eegmusicproject-bmoj2hs8keezeqfgvv4aey.streamlit.app/" />
<meta property="og:type" content="website" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="🧠 BrainWave | EEG Health Monitor" />
<meta name="twitter:description" content="Advanced EEG Analytics • Cognitive State Detection • Study vs Phone Detection" />
<meta name="twitter:image" content="https://raw.githubusercontent.com/MdFaizanAnsari786/EEG_MUSIC_PROJECT/main/app/brain_futuristic.jpg" />
""", unsafe_allow_html=True)

# ================= PATHS =================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)
DATA_PATH = os.path.join(PROJECT_DIR, "data", "eeg study vs phone data.csv")

# ================= LOAD DATA =================
@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

df = load_data()
counts = df["label"].value_counts()
total_samples = len(df)
study_count = int(counts.get(1, 0))
phone_count = int(counts.get(0, 0))

# ================= SIDEBAR =================
with st.sidebar:
    st.markdown("""
    <div class="sidebar-brand">
        <div class="brand-icon">🧠</div>
        <div class="brand-text">
            <h2>BrainWave</h2>
            <span>Health Monitor</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ================= HERO SECTION WITH ANIMATED NEURAL BACKGROUND =================
import base64

# Load and encode the brain image for hero section
brain_image_path = os.path.join(BASE_DIR, "brain_futuristic.jpg")
try:
    with open(brain_image_path, "rb") as f:
        brain_base64 = base64.b64encode(f.read()).decode()
    brain_img_src = f"data:image/jpeg;base64,{brain_base64}"
except:
    brain_img_src = ""

# Load and encode the neural waves image for background (abstract design)
neural_bg_path = os.path.join(BASE_DIR, "abstract_neural_waves.png")
try:
    with open(neural_bg_path, "rb") as f:
        neural_bg_base64 = base64.b64encode(f.read()).decode()
    neural_bg_src = f"data:image/png;base64,{neural_bg_base64}"
except:
    neural_bg_src = brain_img_src  # Fallback to brain image if not found

# Full-screen animated EEG wave background CSS
st.markdown(f"""
<style>
    /* ============================================ */
    /* FULL-SCREEN ANIMATED EEG WAVE BACKGROUND */
    /* ============================================ */
    
    .wave-background {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        pointer-events: none;
        z-index: 0;
        overflow: hidden;
        background: transparent;
    }}
    
    /* Futuristic Grid Overlay */
    .wave-background::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            linear-gradient(rgba(56, 189, 248, 0.03) 1px, transparent 1px),
            linear-gradient(90deg, rgba(56, 189, 248, 0.03) 1px, transparent 1px);
        background-size: 40px 40px;
        z-index: 1;
    }}
    
    /* Scanning Line Effect */
    .wave-background::after {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 4px;
        background: linear-gradient(90deg, transparent, rgba(56, 189, 248, 0.8), rgba(139, 92, 246, 0.6), transparent);
        box-shadow: 0 0 20px rgba(56, 189, 248, 0.8), 0 0 40px rgba(56, 189, 248, 0.4);
        animation: scan-line 4s linear infinite;
        z-index: 2;
    }}
    
    @keyframes scan-line {{
        0% {{ top: 0; opacity: 1; }}
        50% {{ opacity: 0.6; }}
        100% {{ top: 100%; opacity: 1; }}
    }}
    
    /* Animated EEG Wave Lines - Futuristic Neuro Style */
    .eeg-wave {{
        position: absolute;
        width: 200%;
        height: 80px;
        left: 0;
        animation: wave-flow linear infinite;
        z-index: 3;
    }}
    
    .eeg-wave svg {{
        width: 100%;
        height: 100%;
    }}
    
    .eeg-wave path {{
        fill: none;
        stroke-linecap: round;
        stroke-linejoin: round;
    }}
    
    /* Wave positions - Futuristic Neon Style (5 waves, slow movement) */
    .eeg-wave-1 {{ top: 10%; animation-duration: 25s; }}
    .eeg-wave-1 path {{ stroke: rgba(56, 189, 248, 0.4); stroke-width: 3; filter: drop-shadow(0 0 12px rgba(56, 189, 248, 0.5)) drop-shadow(0 0 25px rgba(56, 189, 248, 0.2)); }}
    
    .eeg-wave-2 {{ top: 30%; animation-duration: 30s; animation-delay: -5s; }}
    .eeg-wave-2 path {{ stroke: rgba(52, 211, 153, 0.35); stroke-width: 2.5; filter: drop-shadow(0 0 10px rgba(52, 211, 153, 0.4)) drop-shadow(0 0 20px rgba(52, 211, 153, 0.2)); }}
    
    .eeg-wave-3 {{ top: 50%; animation-duration: 22s; animation-delay: -8s; }}
    .eeg-wave-3 path {{ stroke: rgba(248, 113, 113, 0.3); stroke-width: 2.5; filter: drop-shadow(0 0 10px rgba(248, 113, 113, 0.4)) drop-shadow(0 0 20px rgba(248, 113, 113, 0.2)); }}
    
    .eeg-wave-4 {{ top: 70%; animation-duration: 28s; animation-delay: -3s; }}
    .eeg-wave-4 path {{ stroke: rgba(56, 189, 248, 0.35); stroke-width: 2.5; filter: drop-shadow(0 0 10px rgba(56, 189, 248, 0.4)) drop-shadow(0 0 20px rgba(56, 189, 248, 0.2)); }}
    
    .eeg-wave-5 {{ top: 88%; animation-duration: 35s; animation-delay: -10s; }}
    .eeg-wave-5 path {{ stroke: rgba(52, 211, 153, 0.4); stroke-width: 3; filter: drop-shadow(0 0 15px rgba(52, 211, 153, 0.5)) drop-shadow(0 0 30px rgba(52, 211, 153, 0.2)); }}
    
    @keyframes wave-flow {{
        0% {{ transform: translateX(0); }}
        100% {{ transform: translateX(-50%); }}
    }}
    
    /* Glowing Particles floating */
    .glow-particle {{
        position: absolute;
        border-radius: 50%;
        animation: particle-drift linear infinite;
        opacity: 0.7;
    }}
    
    .glow-particle:nth-child(8) {{ width: 6px; height: 6px; top: 15%; left: 10%; animation-duration: 20s; background: radial-gradient(circle, rgba(56, 189, 248, 1), transparent); box-shadow: 0 0 15px rgba(56, 189, 248, 0.8); }}
    .glow-particle:nth-child(9) {{ width: 8px; height: 8px; top: 30%; left: 85%; animation-duration: 25s; animation-delay: -5s; background: radial-gradient(circle, rgba(139, 92, 246, 1), transparent); box-shadow: 0 0 18px rgba(139, 92, 246, 0.8); }}
    .glow-particle:nth-child(10) {{ width: 5px; height: 5px; top: 55%; left: 20%; animation-duration: 18s; animation-delay: -10s; background: radial-gradient(circle, rgba(52, 211, 153, 1), transparent); box-shadow: 0 0 12px rgba(52, 211, 153, 0.8); }}
    .glow-particle:nth-child(11) {{ width: 7px; height: 7px; top: 75%; left: 70%; animation-duration: 22s; animation-delay: -3s; background: radial-gradient(circle, rgba(56, 189, 248, 1), transparent); box-shadow: 0 0 15px rgba(56, 189, 248, 0.8); }}
    .glow-particle:nth-child(12) {{ width: 4px; height: 4px; top: 40%; left: 50%; animation-duration: 28s; animation-delay: -8s; background: radial-gradient(circle, rgba(251, 191, 36, 1), transparent); box-shadow: 0 0 10px rgba(251, 191, 36, 0.8); }}
    .glow-particle:nth-child(13) {{ width: 6px; height: 6px; top: 85%; left: 30%; animation-duration: 24s; animation-delay: -12s; background: radial-gradient(circle, rgba(139, 92, 246, 1), transparent); box-shadow: 0 0 14px rgba(139, 92, 246, 0.8); }}
    
    @keyframes particle-drift {{
        0% {{ transform: translate(0, 0) scale(1); opacity: 0.5; }}
        25% {{ transform: translate(50px, -30px) scale(1.3); opacity: 0.9; }}
        50% {{ transform: translate(100px, 20px) scale(0.8); opacity: 0.6; }}
        75% {{ transform: translate(50px, -10px) scale(1.1); opacity: 0.8; }}
        100% {{ transform: translate(0, 0) scale(1); opacity: 0.5; }}
    }}
    
    /* Pulse rings from center */
    .pulse-ring {{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        border-radius: 50%;
        border: 1px solid rgba(56, 189, 248, 0.3);
        animation: pulse-expand 4s ease-out infinite;
    }}
    
    .pulse-ring:nth-child(14) {{ animation-delay: 0s; }}
    .pulse-ring:nth-child(15) {{ animation-delay: 1s; }}
    .pulse-ring:nth-child(16) {{ animation-delay: 2s; }}
    .pulse-ring:nth-child(17) {{ animation-delay: 3s; }}
    
    @keyframes pulse-expand {{
        0% {{ width: 50px; height: 50px; opacity: 0.8; border-color: rgba(56, 189, 248, 0.5); }}
        100% {{ width: 600px; height: 600px; opacity: 0; border-color: rgba(139, 92, 246, 0.1); }}
    }}
    
    /* Hero Section Styles - Glassmorphism */
    .hero-section {{
        position: relative;
        z-index: 10;
        background: rgba(15, 23, 42, 0.7);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-radius: 24px;
        padding: 2rem;
        margin: 0 1rem 1rem 1rem;
        box-shadow: 
            0 8px 32px rgba(0, 0, 0, 0.3),
            inset 0 1px 0 rgba(255, 255, 255, 0.05);
    }}
    
    .hero-brain-animated {{
        position: absolute;
        top: 50%;
        right: 3%;
        transform: translateY(-50%);
        width: 250px;
        height: 250px;
        border-radius: 50%;
        object-fit: cover;
        animation: brain-pulse 3s ease-in-out infinite, brain-glow 4s ease-in-out infinite alternate;
        z-index: 11;
    }}
    
    @keyframes brain-pulse {{
        0%, 100% {{ transform: translateY(-50%) scale(1); }}
        50% {{ transform: translateY(-50%) scale(1.08); }}
    }}
    
    @keyframes brain-glow {{
        0% {{ filter: drop-shadow(0 0 15px rgba(56, 189, 248, 0.5)) drop-shadow(0 0 30px rgba(56, 189, 248, 0.3)); }}
        100% {{ filter: drop-shadow(0 0 30px rgba(56, 189, 248, 0.8)) drop-shadow(0 0 50px rgba(14, 165, 233, 0.5)); }}
    }}
</style>

<div class="wave-background">
    <div class="eeg-wave eeg-wave-1"><svg viewBox="0 0 2400 100" preserveAspectRatio="none"><path d="M0,50 L50,50 L60,20 L70,80 L80,45 L100,55 L120,50 L170,50 L180,15 L190,85 L200,40 L220,60 L240,50 L290,50 L300,25 L310,75 L320,50 L400,50 L410,10 L420,90 L430,35 L450,65 L470,50 L520,50 L530,30 L540,70 L550,50 L600,50 L610,5 L620,95 L630,40 L650,60 L670,50 L720,50 L730,20 L740,80 L750,50 L800,50 L810,15 L820,85 L830,45 L850,55 L870,50 L920,50 L930,25 L940,75 L950,50 L1000,50 L1010,10 L1020,90 L1030,40 L1050,60 L1070,50 L1120,50 L1130,30 L1140,70 L1150,50 L1200,50 L1210,5 L1220,95 L1230,45 L1250,55 L1270,50 L1320,50 L1330,20 L1340,80 L1350,50 L1400,50 L1410,15 L1420,85 L1430,40 L1450,60 L1470,50 L1520,50 L1530,25 L1540,75 L1550,50 L1600,50 L1610,10 L1620,90 L1630,45 L1650,55 L1670,50 L1720,50 L1730,30 L1740,70 L1750,50 L1800,50 L1810,5 L1820,95 L1830,40 L1850,60 L1870,50 L1920,50 L1930,20 L1940,80 L1950,50 L2000,50 L2010,15 L2020,85 L2030,45 L2050,55 L2070,50 L2120,50 L2130,25 L2140,75 L2150,50 L2200,50 L2210,10 L2220,90 L2230,40 L2250,60 L2270,50 L2320,50 L2330,30 L2340,70 L2350,50 L2400,50"/></svg></div>
    <div class="eeg-wave eeg-wave-2"><svg viewBox="0 0 2400 100" preserveAspectRatio="none"><path d="M0,50 L30,50 L40,35 L50,65 L60,50 L100,50 L110,40 L115,20 L120,80 L125,60 L130,50 L170,50 L180,30 L190,70 L200,50 L240,50 L250,45 L255,15 L260,85 L265,55 L270,50 L310,50 L320,40 L330,60 L340,50 L380,50 L390,35 L395,10 L400,90 L405,65 L410,50 L450,50 L460,45 L470,55 L480,50 L520,50 L530,30 L535,5 L540,95 L545,70 L550,50 L590,50 L600,40 L610,60 L620,50 L660,50 L670,35 L675,20 L680,80 L685,65 L690,50 L730,50 L740,45 L750,55 L760,50 L800,50 L810,30 L815,10 L820,90 L825,70 L830,50 L870,50 L880,40 L890,60 L900,50 L940,50 L950,35 L955,15 L960,85 L965,65 L970,50 L1010,50 L1020,45 L1030,55 L1040,50 L1080,50 L1090,30 L1095,5 L1100,95 L1105,70 L1110,50 L1150,50 L1160,40 L1170,60 L1180,50 L1220,50 L1230,35 L1235,20 L1240,80 L1245,65 L1250,50 L1290,50 L1300,45 L1310,55 L1320,50 L1360,50 L1370,30 L1375,10 L1380,90 L1385,70 L1390,50 L1430,50 L1440,40 L1450,60 L1460,50 L1500,50 L1510,35 L1515,15 L1520,85 L1525,65 L1530,50 L1570,50 L1580,45 L1590,55 L1600,50 L1640,50 L1650,30 L1655,5 L1660,95 L1665,70 L1670,50 L1710,50 L1720,40 L1730,60 L1740,50 L1780,50 L1790,35 L1795,20 L1800,80 L1805,65 L1810,50 L1850,50 L1860,45 L1870,55 L1880,50 L1920,50 L1930,30 L1935,10 L1940,90 L1945,70 L1950,50 L1990,50 L2000,40 L2010,60 L2020,50 L2060,50 L2070,35 L2075,15 L2080,85 L2085,65 L2090,50 L2130,50 L2140,45 L2150,55 L2160,50 L2200,50 L2210,30 L2215,5 L2220,95 L2225,70 L2230,50 L2270,50 L2280,40 L2290,60 L2300,50 L2340,50 L2350,35 L2355,20 L2360,80 L2365,65 L2370,50 L2400,50"/></svg></div>
    <div class="eeg-wave eeg-wave-3"><svg viewBox="0 0 2400 100" preserveAspectRatio="none"><path d="M0,50 L80,50 L90,40 L100,60 L110,50 L190,50 L200,35 L210,65 L220,50 L300,50 L310,30 L315,15 L320,85 L325,70 L330,50 L410,50 L420,45 L430,55 L440,50 L520,50 L530,40 L535,25 L540,75 L545,60 L550,50 L630,50 L640,35 L650,65 L660,50 L740,50 L750,30 L755,10 L760,90 L765,70 L770,50 L850,50 L860,45 L870,55 L880,50 L960,50 L970,40 L975,20 L980,80 L985,60 L990,50 L1070,50 L1080,35 L1090,65 L1100,50 L1180,50 L1190,30 L1195,15 L1200,85 L1205,70 L1210,50 L1290,50 L1300,45 L1310,55 L1320,50 L1400,50 L1410,40 L1415,25 L1420,75 L1425,60 L1430,50 L1510,50 L1520,35 L1530,65 L1540,50 L1620,50 L1630,30 L1635,10 L1640,90 L1645,70 L1650,50 L1730,50 L1740,45 L1750,55 L1760,50 L1840,50 L1850,40 L1855,20 L1860,80 L1865,60 L1870,50 L1950,50 L1960,35 L1970,65 L1980,50 L2060,50 L2070,30 L2075,15 L2080,85 L2085,70 L2090,50 L2170,50 L2180,45 L2190,55 L2200,50 L2280,50 L2290,40 L2295,25 L2300,75 L2305,60 L2310,50 L2400,50"/></svg></div>
    <div class="eeg-wave eeg-wave-4"><svg viewBox="0 0 2400 100" preserveAspectRatio="none"><path d="M0,50 L40,50 L45,45 L50,10 L55,90 L60,55 L65,50 L120,50 L125,48 L130,15 L135,85 L140,52 L145,50 L200,50 L205,45 L210,5 L215,95 L220,55 L225,50 L280,50 L285,48 L290,20 L295,80 L300,52 L305,50 L360,50 L365,45 L370,10 L375,90 L380,55 L385,50 L440,50 L445,48 L450,15 L455,85 L460,52 L465,50 L520,50 L525,45 L530,5 L535,95 L540,55 L545,50 L600,50 L605,48 L610,20 L615,80 L620,52 L625,50 L680,50 L685,45 L690,10 L695,90 L700,55 L705,50 L760,50 L765,48 L770,15 L775,85 L780,52 L785,50 L840,50 L845,45 L850,5 L855,95 L860,55 L865,50 L920,50 L925,48 L930,20 L935,80 L940,52 L945,50 L1000,50 L1005,45 L1010,10 L1015,90 L1020,55 L1025,50 L1080,50 L1085,48 L1090,15 L1095,85 L1100,52 L1105,50 L1160,50 L1165,45 L1170,5 L1175,95 L1180,55 L1185,50 L1240,50 L1245,48 L1250,20 L1255,80 L1260,52 L1265,50 L1320,50 L1325,45 L1330,10 L1335,90 L1340,55 L1345,50 L1400,50 L1405,48 L1410,15 L1415,85 L1420,52 L1425,50 L1480,50 L1485,45 L1490,5 L1495,95 L1500,55 L1505,50 L1560,50 L1565,48 L1570,20 L1575,80 L1580,52 L1585,50 L1640,50 L1645,45 L1650,10 L1655,90 L1660,55 L1665,50 L1720,50 L1725,48 L1730,15 L1735,85 L1740,52 L1745,50 L1800,50 L1805,45 L1810,5 L1815,95 L1820,55 L1825,50 L1880,50 L1885,48 L1890,20 L1895,80 L1900,52 L1905,50 L1960,50 L1965,45 L1970,10 L1975,90 L1980,55 L1985,50 L2040,50 L2045,48 L2050,15 L2055,85 L2060,52 L2065,50 L2120,50 L2125,45 L2130,5 L2135,95 L2140,55 L2145,50 L2200,50 L2205,48 L2210,20 L2215,80 L2220,52 L2225,50 L2280,50 L2285,45 L2290,10 L2295,90 L2300,55 L2305,50 L2360,50 L2365,48 L2370,15 L2375,85 L2380,52 L2385,50 L2400,50"/></svg></div>
    <div class="eeg-wave eeg-wave-5"><svg viewBox="0 0 2400 100" preserveAspectRatio="none"><path d="M0,50 L60,50 L70,45 L80,20 L90,80 L100,55 L120,50 L180,50 L190,40 L200,60 L210,50 L270,50 L280,35 L290,65 L300,50 L360,50 L370,45 L380,25 L390,75 L400,55 L420,50 L480,50 L490,40 L500,60 L510,50 L570,50 L580,35 L590,15 L600,85 L610,65 L630,50 L690,50 L700,45 L710,55 L720,50 L780,50 L790,40 L800,60 L810,50 L870,50 L880,35 L890,20 L900,80 L910,65 L930,50 L990,50 L1000,45 L1010,55 L1020,50 L1080,50 L1090,40 L1100,60 L1110,50 L1170,50 L1180,35 L1190,25 L1200,75 L1210,65 L1230,50 L1290,50 L1300,45 L1310,55 L1320,50 L1380,50 L1390,40 L1400,60 L1410,50 L1470,50 L1480,35 L1490,15 L1500,85 L1510,65 L1530,50 L1590,50 L1600,45 L1610,55 L1620,50 L1680,50 L1690,40 L1700,60 L1710,50 L1770,50 L1780,35 L1790,20 L1800,80 L1810,65 L1830,50 L1890,50 L1900,45 L1910,55 L1920,50 L1980,50 L1990,40 L2000,60 L2010,50 L2070,50 L2080,35 L2090,25 L2100,75 L2110,65 L2130,50 L2190,50 L2200,45 L2210,55 L2220,50 L2280,50 L2290,40 L2300,60 L2310,50 L2370,50 L2380,35 L2390,65 L2400,50"/></svg></div>
    <div class="glow-particle"></div><div class="glow-particle"></div><div class="glow-particle"></div><div class="glow-particle"></div><div class="glow-particle"></div><div class="glow-particle"></div>
    <div class="pulse-ring"></div><div class="pulse-ring"></div><div class="pulse-ring"></div><div class="pulse-ring"></div>
</div>

<div class="hero-section"><img src="{brain_img_src}" class="hero-brain-animated" alt="Brain"><div class="hero-content"><div class="hero-badge">🧠 EEG Neuro-Sonification Platform</div><h1 class="hero-title">Brain Health Monitor</h1><p class="hero-subtitle">Advanced Cognitive State Analysis | Study vs Phone Detection</p><div class="hero-status"><span class="status-dot"></span><span>Live Monitoring Active</span></div></div></div>
""", unsafe_allow_html=True)

# ================= METRICS ROW =================
st.markdown(f"""
<div class="metrics-row">
    <div class="metric-card">
        <div class="metric-header">
            <div class="metric-icon cyan">📊</div>
            <div class="metric-badge up">↑ Active</div>
        </div>
        <div class="metric-value">{total_samples:,}</div>
        <div class="metric-label">Total EEG Samples</div>
    </div>
    <div class="metric-card">
        <div class="metric-header">
            <div class="metric-icon green">📚</div>
            <div class="metric-badge up">↑ {study_count*100//total_samples}%</div>
        </div>
        <div class="metric-value">{study_count:,}</div>
        <div class="metric-label">Study / Focused</div>
    </div>
    <div class="metric-card">
        <div class="metric-header">
            <div class="metric-icon orange">📱</div>
            <div class="metric-badge down">↓ {phone_count*100//total_samples}%</div>
        </div>
        <div class="metric-value">{phone_count:,}</div>
        <div class="metric-label">Phone / Distracted</div>
    </div>
    <div class="metric-card">
        <div class="metric-header">
            <div class="metric-icon purple">🎯</div>
            <div class="metric-badge up">↑ High</div>
        </div>
        <div class="metric-value">99.95%</div>
        <div class="metric-label">Model Accuracy</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ================= WAVE BANDS SECTION =================
st.markdown("""
<div class="wave-bands-card">
    <div class="card-header">
        <div class="card-title">
            <div class="card-title-icon">📈</div>
            <span>Brain Wave Bands</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# Wave bands data - calculated from actual EEG dataset
delta_mean = df['delta'].mean()
theta_mean = df['theta'].mean()
alpha_mean = df['alpha'].mean()
beta_mean = df['beta'].mean()
gamma_mean = df['gamma'].mean()

waves = [
    ("Delta", "0.5-4 Hz", "delta", f"{delta_mean:.2f} µV"),
    ("Theta", "4-8 Hz", "theta", f"{theta_mean:.2f} µV"),
    ("Alpha", "8-13 Hz", "alpha", f"{alpha_mean:.2f} µV"),
    ("Beta", "13-30 Hz", "beta", f"{beta_mean:.2f} µV"),
    ("Gamma", "30-100 Hz", "gamma", f"{gamma_mean:.2f} µV"),
]

# Display waves in 5 columns
wave_cols = st.columns(5)
for i, (wave_name, wave_range, wave_class, wave_val) in enumerate(waves):
    with wave_cols[i]:
        st.markdown(f"""
        <div class="wave-item" style="flex-direction: column; text-align: center; border-bottom: none;">
            <div class="wave-dot {wave_class}" style="margin-bottom: 8px;"></div>
            <div class="wave-name">{wave_name}</div>
            <div class="wave-range">{wave_range}</div>
            <div class="wave-value">{wave_val}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ================= NAVIGATION CARDS =================
st.markdown("""
<div class="analysis-modules-container">
    <div class="section-title">
        <div class="section-title-icon">🔬</div>
        <span>Analysis Modules</span>
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="module-card"><div class="module-title">🎯 EEG Prediction</div></div>', unsafe_allow_html=True)
    if st.button("Open Prediction →", key="nav_eeg"):
        st.switch_page("pages/1_🎯_EEG_Prediction.py")

with col2:
    st.markdown('<div class="module-card"><div class="module-title">🌊 Live Brainwaves</div></div>', unsafe_allow_html=True)
    if st.button("Open Waves →", key="nav_waves"):
        st.switch_page("pages/2_🌊_Live_Waves.py")

with col3:
    st.markdown('<div class="module-card"><div class="module-title">🎵 Brain Music</div></div>', unsafe_allow_html=True)
    if st.button("Open Music →", key="nav_music"):
        st.switch_page("pages/3_🎵_Brain_Music.py")

col4, col5, col6 = st.columns(3)

with col4:
    st.markdown('<div class="module-card"><div class="module-title">📊 Survey Analysis</div></div>', unsafe_allow_html=True)
    if st.button("Open Survey →", key="nav_survey"):
        st.switch_page("pages/4_📊_Survey_Analysis.py")

with col5:
    st.markdown('<div class="module-card"><div class="module-title">🤖 Model Insights</div></div>', unsafe_allow_html=True)
    if st.button("Open Insights →", key="nav_model"):
        st.switch_page("pages/5_🤖_Model_Insights.py")

with col6:
    st.markdown('<div class="module-card"><div class="module-title">🚀 About Project</div></div>', unsafe_allow_html=True)
    if st.button("Open About →", key="nav_about"):
        pass

# ================= SIDEBAR SHARE =================
with st.sidebar:
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center;">
        <h3>📱 Share App</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # QR Code for the app
    qr_url = "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://eegmusicproject-bmoj2hs8keezeqfgvv4aey.streamlit.app/"
    st.image(qr_url, caption="Scan to Open on Mobile", width=150)
    st.markdown("""
    <div style="text-align: center; margin-top: 10px;">
        <small>Scan this QR code to open the app on your phone!</small>
    </div>
    """, unsafe_allow_html=True)

# ================= FOOTER =================
st.markdown("""
<div class="dashboard-footer">
    <div class="footer-brand">🧠 BrainWave Health Monitor</div>
    <div class="footer-desc">Advanced EEG Analytics • Cognitive State Detection • MSc Research Project</div>
    <div class="footer-badges">
        <span class="tech-badge">Streamlit</span>
        <span class="tech-badge">Scikit-Learn</span>
        <span class="tech-badge">EEG Analysis</span>
        <span class="tech-badge">Sonification</span>
        <span class="tech-badge">Healthcare AI</span>
    </div>
</div>
""", unsafe_allow_html=True)