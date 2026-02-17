# Shared Theme CSS for all pages - Dark/Light Mode Support
# Updated: Unified Background Effects (Particles + Grid) for all pages

# ============================================
# DARK MODE CSS (Default)
# ============================================
DARK_MODE_CSS = """
<style>
    /* Premium Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
    
    * { font-family: 'Plus Jakarta Sans', sans-serif; }
    
    /* Hide Streamlit defaults */
    #MainMenu, footer { visibility: hidden; }
    
    /* Hide top header bar (black line) */
    header[data-testid="stHeader"] {
        background: transparent !important;
        height: 0 !important;
        min-height: 0 !important;
        padding: 0 !important;
        z-index: 0 !important;
    }

    /* Fix Sidebar Toggle Button Visibility */
    [data-testid="stSidebarCollapsedControl"] {
        top: 2rem !important;
        z-index: 99999 !important;
        color: rgba(255, 255, 255, 0.8) !important;
    }
    
    /* Main Background - Dark Blue Gradient (More Transparent) */
    .stApp {
        background: linear-gradient(135deg, rgba(12, 25, 41, 0.85) 0%, rgba(15, 40, 71, 0.8) 30%, rgba(12, 74, 110, 0.75) 60%, rgba(15, 40, 71, 0.8) 80%, rgba(12, 25, 41, 0.85) 100%) !important;
        background-attachment: fixed;
    }
    
    .main .block-container {
        padding: 0rem 2rem 1rem 2rem !important;
        margin-top: -6rem !important;
        max-width: 1600px;
    }
    
    /* ============================================ */
    /* FUTURISTIC ANIMATED BACKGROUND EFFECTS */
    /* ============================================ */
    
    /* Floating Particles Container */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 0;
        background-image: 
            radial-gradient(2px 2px at 20px 30px, rgba(56, 189, 248, 0.4), transparent),
            radial-gradient(2px 2px at 40px 70px, rgba(139, 92, 246, 0.3), transparent),
            radial-gradient(2px 2px at 50px 160px, rgba(56, 189, 248, 0.3), transparent),
            radial-gradient(2px 2px at 90px 40px, rgba(103, 232, 249, 0.4), transparent),
            radial-gradient(2px 2px at 130px 80px, rgba(167, 139, 250, 0.3), transparent),
            radial-gradient(2px 2px at 160px 120px, rgba(56, 189, 248, 0.35), transparent),
            radial-gradient(1.5px 1.5px at 200px 50px, rgba(52, 211, 153, 0.3), transparent),
            radial-gradient(2px 2px at 250px 140px, rgba(56, 189, 248, 0.4), transparent),
            radial-gradient(1.5px 1.5px at 300px 90px, rgba(139, 92, 246, 0.35), transparent),
            radial-gradient(2px 2px at 350px 180px, rgba(103, 232, 249, 0.3), transparent),
            radial-gradient(2px 2px at 400px 60px, rgba(56, 189, 248, 0.4), transparent),
            radial-gradient(1.5px 1.5px at 450px 130px, rgba(167, 139, 250, 0.35), transparent),
            radial-gradient(2px 2px at 500px 200px, rgba(52, 211, 153, 0.3), transparent),
            radial-gradient(2px 2px at 550px 80px, rgba(56, 189, 248, 0.35), transparent),
            radial-gradient(1.5px 1.5px at 600px 150px, rgba(139, 92, 246, 0.3), transparent);
        background-size: 650px 220px;
        animation: particles-float 25s linear infinite;
        opacity: 0.8;
    }
    
    @keyframes particles-float {
        0% { transform: translateY(0) translateX(0); }
        50% { transform: translateY(-15px) translateX(10px); }
        100% { transform: translateY(0) translateX(0); }
    }
    
    /* Neural Network Grid Effect */
    .stApp::after {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 0;
        background-image: 
            linear-gradient(rgba(56, 189, 248, 0.03) 1px, transparent 1px),
            linear-gradient(90deg, rgba(56, 189, 248, 0.03) 1px, transparent 1px);
        background-size: 60px 60px;
        animation: grid-pulse 8s ease-in-out infinite;
    }
    
    @keyframes grid-pulse {
        0%, 100% { opacity: 0.4; }
        50% { opacity: 0.7; }
    }
    
    /* Floating Glowing Orbs */
    .main::before {
        content: '';
        position: fixed;
        top: 10%;
        left: 5%;
        width: 300px;
        height: 300px;
        background: radial-gradient(circle, rgba(56, 189, 248, 0.15) 0%, transparent 70%);
        border-radius: 50%;
        pointer-events: none;
        z-index: 0;
        animation: orb-float-1 12s ease-in-out infinite;
        filter: blur(40px);
    }
    
    .main::after {
        content: '';
        position: fixed;
        bottom: 15%;
        right: 10%;
        width: 250px;
        height: 250px;
        background: radial-gradient(circle, rgba(139, 92, 246, 0.12) 0%, transparent 70%);
        border-radius: 50%;
        pointer-events: none;
        z-index: 0;
        animation: orb-float-2 15s ease-in-out infinite;
        filter: blur(50px);
    }
    
    @keyframes orb-float-1 {
        0%, 100% { transform: translate(0, 0) scale(1); opacity: 0.6; }
        25% { transform: translate(30px, 20px) scale(1.1); opacity: 0.8; }
        50% { transform: translate(50px, -10px) scale(1); opacity: 0.7; }
        75% { transform: translate(20px, 30px) scale(1.05); opacity: 0.9; }
    }
    
    @keyframes orb-float-2 {
        0%, 100% { transform: translate(0, 0) scale(1); opacity: 0.5; }
        33% { transform: translate(-40px, -20px) scale(1.15); opacity: 0.7; }
        66% { transform: translate(-20px, 40px) scale(0.95); opacity: 0.6; }
    }
    
    /* Scanline Effect Overlay */
    .block-container::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 1000;
        background: repeating-linear-gradient(
            0deg,
            transparent,
            transparent 2px,
            rgba(56, 189, 248, 0.01) 2px,
            rgba(56, 189, 248, 0.01) 4px
        );
        animation: scanline-move 10s linear infinite;
    }
    
    @keyframes scanline-move {
        0% { transform: translateY(0); }
        100% { transform: translateY(8px); }
    }
    
    /* ============================================ */
    /* HERO SECTION WITH BRAIN BACKGROUND */
    /* ============================================ */
    .hero-section {
        position: relative;
        padding: 3rem 2.5rem;
        margin-bottom: 2rem;
        background: linear-gradient(135deg, rgba(14, 165, 233, 0.08) 0%, rgba(56, 189, 248, 0.05) 100%);
        border-radius: 24px;
        border: 1px solid rgba(125, 211, 252, 0.15);
        overflow: hidden;
    }
    
    .hero-bg-brain {
        position: absolute;
        top: 50%;
        right: 3%;
        transform: translateY(-50%);
        width: 280px;
        height: 280px;
        background-image: url('brain_futuristic.jpg');
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
        border-radius: 50%;
        animation: brain-pulse 3s ease-in-out infinite, brain-glow 4s ease-in-out infinite alternate;
        z-index: 0;
    }
    
    @keyframes brain-pulse {
        0%, 100% { transform: translateY(-50%) scale(1); }
        50% { transform: translateY(-50%) scale(1.05); }
    }
    
    @keyframes brain-glow {
        0% { 
            filter: drop-shadow(0 0 20px rgba(56, 189, 248, 0.4)) drop-shadow(0 0 40px rgba(56, 189, 248, 0.2));
            opacity: 0.85;
        }
        100% { 
            filter: drop-shadow(0 0 35px rgba(56, 189, 248, 0.7)) drop-shadow(0 0 60px rgba(14, 165, 233, 0.4));
            opacity: 1;
        }
    }
    
    .hero-content {
        position: relative;
        z-index: 1;
    }
    
    .hero-badge {
        display: inline-block;
        padding: 8px 16px;
        background: linear-gradient(135deg, rgba(56, 189, 248, 0.15), rgba(14, 165, 233, 0.1));
        border: 1px solid rgba(125, 211, 252, 0.25);
        border-radius: 30px;
        font-size: 0.85rem;
        font-weight: 600;
        color: #7dd3fc;
        margin-bottom: 1rem;
    }
    
    .hero-title {
        font-size: 2.75rem;
        font-weight: 800;
        background: linear-gradient(90deg, #38bdf8 0%, #818cf8 50%, #c084fc 100%) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        background-clip: text !important;
        color: transparent !important;
        margin: 0 0 0.75rem 0;
        letter-spacing: -0.02em;
        line-height: 1.1;
    }
    
    .hero-subtitle {
        font-size: 1.1rem;
        color: #bae6fd;
        margin: 0 0 1.5rem 0;
        max-width: 600px;
    }
    
    .hero-status {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 8px 16px;
        background: rgba(52, 211, 153, 0.1);
        border: 1px solid rgba(52, 211, 153, 0.25);
        border-radius: 30px;
        font-size: 0.875rem;
        color: #34d399;
        font-weight: 500;
    }
    
    .status-dot {
        width: 8px;
        height: 8px;
        background: #34d399;
        border-radius: 50%;
        animation: status-pulse 2s ease-in-out infinite;
    }
    
    @keyframes status-pulse {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.5; transform: scale(1.2); }
    }
    
    /* Sidebar - Dark Frosted Glass */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, rgba(12, 74, 110, 0.9) 0%, rgba(15, 40, 71, 0.95) 100%) !important;
        backdrop-filter: blur(20px);
        border-right: 1px solid rgba(125, 211, 252, 0.15);
    }
    
    section[data-testid="stSidebar"] > div {
        background: transparent !important;
    }
    
    /* Change 'app' to 'Home' */
    [data-testid="stSidebarNav"] li:first-child a span {
        font-size: 0 !important;
    }
    [data-testid="stSidebarNav"] li:first-child a span::before {
        content: "🏠  Home";
        font-size: 14px !important;
        color: #f0f9ff;
    }
    
    /* Sidebar nav links */
    [data-testid="stSidebarNav"] a {
        color: #bae6fd !important;
        border-radius: 10px;
    }
    [data-testid="stSidebarNav"] a:hover {
        background: rgba(56, 189, 248, 0.1) !important;
        color: #f0f9ff !important;
    }
    [data-testid="stSidebarNav"] a[aria-selected="true"] {
        background: linear-gradient(135deg, #0ea5e9, #38bdf8) !important;
        color: white !important;
    }
    
    /* Metrics Row - Horizontal Grid */
    .metrics-row {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 1.25rem;
        margin-bottom: 1.5rem;
    }
    
    @media screen and (max-width: 992px) {
        .metrics-row { grid-template-columns: repeat(2, 1fr); }
    }
    @media screen and (max-width: 576px) {
        .metrics-row { grid-template-columns: 1fr; }
    }
    
    /* Cards */
    .glass-card, .metric-card, .content-card, .nav-card, .audio-card, .prediction-card, .control-panel, .wave-bands-card {
        background: rgba(14, 165, 233, 0.08) !important;
        backdrop-filter: blur(16px);
        border: 1px solid rgba(125, 211, 252, 0.15) !important;
        border-radius: 20px !important;
        padding: 1.5rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
    }
    
    .metric-card {
        position: relative;
        overflow: hidden;
    }
    
    .metric-card::after {
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        width: 100px;
        height: 100px;
        background: radial-gradient(circle, rgba(56, 189, 248, 0.15) 0%, transparent 70%);
        opacity: 0.5;
    }
    
    .metric-header {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        margin-bottom: 1rem;
    }
    
    .metric-icon {
        width: 48px;
        height: 48px;
        border-radius: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.25rem;
    }
    
    .metric-icon.cyan { background: rgba(56, 189, 248, 0.15); }
    .metric-icon.green { background: rgba(52, 211, 153, 0.15); }
    .metric-icon.orange { background: rgba(251, 191, 36, 0.15); }
    .metric-icon.purple { background: rgba(139, 92, 246, 0.15); }
    
    .metric-badge {
        display: flex;
        align-items: center;
        gap: 4px;
        padding: 4px 10px;
        border-radius: 8px;
        font-size: 0.75rem;
        font-weight: 600;
    }
    
    .metric-badge.up {
        background: rgba(52, 211, 153, 0.15);
        color: #34d399;
    }
    
    .metric-badge.down {
        background: rgba(248, 113, 113, 0.15);
        color: #f87171;
    }
    
    .metric-value {
        font-size: 2.25rem;
        font-weight: 800;
        color: #f0f9ff;
        line-height: 1;
        margin-bottom: 6px;
    }
    
    .metric-label {
        font-size: 0.875rem;
        color: #bae6fd;
        font-weight: 500;
    }
    
    .glass-card:hover, .metric-card:hover, .nav-card:hover {
        transform: translateY(-6px) scale(1.01);
        box-shadow: 
            0 20px 40px rgba(56, 189, 248, 0.25),
            0 0 30px rgba(56, 189, 248, 0.15),
            inset 0 0 20px rgba(56, 189, 248, 0.05);
        border-color: rgba(125, 211, 252, 0.5) !important;
        background: linear-gradient(135deg, rgba(14, 165, 233, 0.18), rgba(56, 189, 248, 0.12)) !important;
        animation: card-glow 2s ease-in-out infinite;
    }
    
    @keyframes card-glow {
        0%, 100% { box-shadow: 0 20px 40px rgba(56, 189, 248, 0.25), 0 0 30px rgba(56, 189, 248, 0.15); }
        50% { box-shadow: 0 20px 50px rgba(56, 189, 248, 0.35), 0 0 40px rgba(56, 189, 248, 0.2); }
    }
    
    /* Holographic Shimmer Effect on Cards */
    .glass-card::before, .content-card::before, .prediction-card::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(
            45deg,
            transparent 30%,
            rgba(56, 189, 248, 0.08) 40%,
            rgba(139, 92, 246, 0.08) 50%,
            rgba(56, 189, 248, 0.08) 60%,
            transparent 70%
        );
        transform: rotate(45deg);
        animation: shimmer 6s ease-in-out infinite;
        pointer-events: none;
        z-index: 1;
    }
    
    @keyframes shimmer {
        0% { transform: translateX(-100%) rotate(45deg); }
        100% { transform: translateX(100%) rotate(45deg); }
    }
    
    /* Enhanced Data Card Pulse Effect */
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(
            135deg,
            transparent 0%,
            rgba(56, 189, 248, 0.05) 50%,
            transparent 100%
        );
        opacity: 0;
        transition: opacity 0.5s ease;
        border-radius: 20px;
        pointer-events: none;
    }
    
    .metric-card:hover::before {
        opacity: 1;
        animation: pulse-glow 2s ease-in-out infinite;
    }
    
    @keyframes pulse-glow {
        0%, 100% { opacity: 0.5; }
        50% { opacity: 1; }
    }
    
    /* Futuristic Border Animation */
    .hero-section, .wave-bands-card {
        position: relative;
    }
    
    .hero-section::after, .wave-bands-card::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        border-radius: 24px;
        padding: 2px;
        background: linear-gradient(135deg, rgba(56, 189, 248, 0.5), rgba(139, 92, 246, 0.3), rgba(56, 189, 248, 0.5));
        -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
        mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
        -webkit-mask-composite: xor;
        mask-composite: exclude;
        opacity: 0.4;
        animation: border-glow 4s ease-in-out infinite;
        pointer-events: none;
    }
    
    @keyframes border-glow {
        0%, 100% { opacity: 0.3; }
        50% { opacity: 0.7; }
    }

    
    /* Wave Bands - Attractive Styling */
    .wave-bands-card {
        margin-bottom: 1.5rem;
    }
    
    .wave-item {
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        text-align: center;
        padding: 1rem 0.5rem;
    }
    
    .wave-dot {
        width: 16px;
        height: 16px;
        border-radius: 50%;
        margin-bottom: 10px;
        animation: wave-pulse 2s ease-in-out infinite;
    }
    
    .wave-dot.delta { background: #a78bfa; box-shadow: 0 0 20px #a78bfa, 0 0 40px rgba(167, 139, 250, 0.5); }
    .wave-dot.theta { background: #67e8f9; box-shadow: 0 0 20px #67e8f9, 0 0 40px rgba(103, 232, 249, 0.5); }
    .wave-dot.alpha { background: #6ee7b7; box-shadow: 0 0 20px #6ee7b7, 0 0 40px rgba(110, 231, 183, 0.5); }
    .wave-dot.beta { background: #fcd34d; box-shadow: 0 0 20px #fcd34d, 0 0 40px rgba(252, 211, 77, 0.5); }
    .wave-dot.gamma { background: #fca5a5; box-shadow: 0 0 20px #fca5a5, 0 0 40px rgba(252, 165, 165, 0.5); }
    
    @keyframes wave-pulse {
        0%, 100% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.2); opacity: 0.8; }
    }
    
    .wave-name {
        font-weight: 700;
        font-size: 1rem;
        color: #f0f9ff;
        margin-bottom: 4px;
    }
    
    .wave-range {
        font-size: 0.75rem;
        color: #7dd3fc;
        margin-bottom: 6px;
    }
    
    .wave-value {
        font-weight: 800;
        font-size: 1.25rem;
        color: #38bdf8;
    }
    
    .card-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1.25rem;
    }
    
    .card-title {
        display: flex;
        align-items: center;
        gap: 12px;
        font-size: 1.1rem;
        font-weight: 700;
        color: #f0f9ff;
    }
    
    .card-title-icon {
        width: 36px;
        height: 36px;
        background: linear-gradient(135deg, rgba(56, 189, 248, 0.2), rgba(14, 165, 233, 0.2));
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    /* Page Header */
    .page-header {
        background: rgba(14, 165, 233, 0.08) !important;
        backdrop-filter: blur(16px);
        border: 1px solid rgba(125, 211, 252, 0.15) !important;
        border-radius: 20px !important;
        padding: 1.5rem 2rem;
        margin-bottom: 1.5rem;
    }
    
    .page-title {
        font-size: 1.75rem;
        font-weight: 800;
        background: linear-gradient(90deg, #38bdf8 0%, #818cf8 50%, #c084fc 100%) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        background-clip: text !important;
        color: transparent !important;
    }
    
    .page-subtitle {
        color: #bae6fd !important;
    }
    
    /* Section Header */
    .section-header {
        background: linear-gradient(90deg, rgba(56, 189, 248, 0.1), transparent) !important;
        border-left: 4px solid #38bdf8 !important;
        padding: 0.75rem 1.25rem;
        margin: 1.5rem 0 1rem 0;
        border-radius: 0 12px 12px 0;
    }
    
    .section-title {
        background: linear-gradient(90deg, #38bdf8 0%, #818cf8 50%, #c084fc 100%) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        background-clip: text !important;
        color: transparent !important;
        font-weight: 700 !important;
    }

    
    .section-desc {
        color: #bae6fd !important;
    }
    
    /* Metrics */
    [data-testid="stMetricValue"] { color: #f0f9ff !important; font-weight: 700; }
    [data-testid="stMetricLabel"] { color: #bae6fd !important; }
    .metric-value { color: #f0f9ff !important; font-size: 2.25rem; font-weight: 800; }
    .metric-label { color: #bae6fd !important; }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        background: rgba(14, 165, 233, 0.05) !important;
        border-radius: 12px;
        padding: 0.5rem;
        border: 1px solid rgba(125, 211, 252, 0.1);
    }
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        color: #bae6fd !important;
        border-radius: 8px;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #0ea5e9, #38bdf8) !important;
        color: white !important;
    }
    
    /* Buttons - Futuristic Neon Style */
    .stButton > button {
        background: linear-gradient(135deg, rgba(56, 189, 248, 0.2), rgba(14, 165, 233, 0.15)) !important;
        border: 1px solid rgba(125, 211, 252, 0.4) !important;
        color: #f0f9ff !important;
        border-radius: 14px;
        font-weight: 600;
        position: relative;
        overflow: hidden;
        transition: all 0.3s ease;
        box-shadow: 0 0 15px rgba(56, 189, 248, 0.2);
    }
    
    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(56, 189, 248, 0.3), transparent);
        transition: left 0.5s ease;
    }
    
    .stButton > button:hover::before {
        left: 100%;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, rgba(56, 189, 248, 0.35), rgba(14, 165, 233, 0.3)) !important;
        border-color: #7dd3fc !important;
        box-shadow: 
            0 0 20px rgba(56, 189, 248, 0.4),
            0 0 40px rgba(56, 189, 248, 0.2),
            0 8px 32px rgba(56, 189, 248, 0.25);
        transform: translateY(-2px);
    }
    
    .stButton > button:active {
        transform: translateY(0);
        box-shadow: 0 0 15px rgba(56, 189, 248, 0.3);
    }
    
    /* Header */
    .dashboard-header { border-bottom: 1px solid rgba(125, 211, 252, 0.15) !important; }
    .header-text h1 { color: #f0f9ff !important; }
    .header-text p { color: #bae6fd !important; }
    .header-icon {
        background: linear-gradient(135deg, #38bdf8, #0ea5e9) !important;
        box-shadow: 0 8px 32px rgba(56, 189, 248, 0.4);
    }
    
    /* Wave bands */
    .wave-name { color: #f0f9ff !important; }
    .wave-range, .wave-value { color: #bae6fd !important; }
    
    /* Nav cards */
    .nav-card-title { color: #f0f9ff !important; }
    .nav-card-desc { color: #bae6fd !important; }
    .nav-card-icon {
        background: linear-gradient(135deg, rgba(56, 189, 248, 0.15), rgba(14, 165, 233, 0.15)) !important;
    }
    .nav-card-tag {
        background: rgba(56, 189, 248, 0.1) !important;
        border: 1px solid rgba(125, 211, 252, 0.2) !important;
        color: #7dd3fc !important;
    }
    
    /* Individual Module Cards - Strong Blur like Brain Wave Bands */
    .module-card {
        background: linear-gradient(135deg, rgba(15, 40, 60, 0.85), rgba(10, 30, 50, 0.9)) !important;
        backdrop-filter: blur(30px) saturate(150%) !important;
        -webkit-backdrop-filter: blur(30px) saturate(150%) !important;
        border: 1px solid rgba(56, 189, 248, 0.35) !important;
        border-radius: 16px !important;
        padding: 1.5rem !important;
        text-align: center !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.08) !important;
    }
    .module-card:hover {
        background: linear-gradient(135deg, rgba(15, 45, 70, 0.9), rgba(10, 35, 55, 0.95)) !important;
        border-color: rgba(56, 189, 248, 0.5) !important;
        box-shadow: 0 12px 40px rgba(56, 189, 248, 0.2), inset 0 1px 0 rgba(255, 255, 255, 0.1) !important;
        transform: translateY(-3px) !important;
    }
    .module-title {
        background: linear-gradient(90deg, #38bdf8 0%, #818cf8 50%, #c084fc 100%) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        background-clip: text !important;
        color: transparent !important;
        font-size: 1.25rem !important;
        font-weight: 700 !important;
        margin: 0 !important;
        letter-spacing: 0.02em !important;
    }
    /* Footer */
    .dashboard-footer { border-top: 1px solid rgba(125, 211, 252, 0.15) !important; }
    .footer-brand { color: #f0f9ff !important; }
    .footer-desc { color: #bae6fd !important; }
    .tech-badge {
        background: rgba(56, 189, 248, 0.1) !important;
        border: 1px solid rgba(125, 211, 252, 0.2) !important;
        color: #7dd3fc !important;
    }
    
    /* Sidebar brand */
    .sidebar-brand { border-bottom: 1px solid rgba(125, 211, 252, 0.15) !important; }
    .brand-text h2 { color: #f0f9ff !important; }
    .brand-text span { color: #7dd3fc !important; }
    .brand-icon {
        background: linear-gradient(135deg, #38bdf8, #0ea5e9) !important;
        box-shadow: 0 8px 32px rgba(56, 189, 248, 0.3);
    }
    
    /* Inputs */
    .stSelectbox > div > div, .stNumberInput > div > div > input {
        background: rgba(14, 165, 233, 0.1) !important;
        border-color: rgba(125, 211, 252, 0.2) !important;
        color: #f0f9ff !important;
    }
    .stSelectbox label, .stNumberInput label { color: #bae6fd !important; }
    
    /* Expander */
    .streamlit-expanderHeader {
        background: rgba(14, 165, 233, 0.08) !important;
        border: 1px solid rgba(125, 211, 252, 0.15) !important;
        color: #f0f9ff !important;
    }
    
    /* DataFrame */
    .stDataFrame { background: rgba(14, 165, 233, 0.05) !important; border-radius: 12px; }
    
    /* Alert */
    .stAlert {
        background: rgba(14, 165, 233, 0.1) !important;
        border: 1px solid rgba(125, 211, 252, 0.2) !important;
        color: #bae6fd !important;
    }
    
    /* Plotly */
    .js-plotly-plot .plotly .main-svg { background: transparent !important; }
    
    /* Image constraints */
    .stImage > img { max-height: 350px; object-fit: contain; }
</style>
"""

# ============================================
# LIGHT MODE CSS - Dribbble Reference Match
# ============================================
LIGHT_MODE_CSS = """
<style>
    /* Premium Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');
    
    * { font-family: 'Plus Jakarta Sans', sans-serif; }
    
    /* Hide Streamlit defaults */
    #MainMenu, footer { visibility: hidden; }
    
    /* Hide top header bar */
    header[data-testid="stHeader"] {
        background: transparent !important;
        height: 0 !important;
        min-height: 0 !important;
        padding: 0 !important;
    }
    
    /* Main Background - Cream + Blue Futuristic */
    .stApp {
        background: linear-gradient(135deg, #F5F0E8 0%, #EBE5DC 30%, #E8EEF5 60%, #F0F4F8 100%) !important;
        background-attachment: fixed;
    }
    
    .main .block-container {
        padding: 0.5rem 2rem 1rem 2rem;
        max-width: 1600px;
    }
    
    /* Sidebar - Cream with blue accent */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #FAF8F5 0%, #F5F0E8 100%) !important;
        border-right: 2px solid rgba(59, 130, 246, 0.15) !important;
        box-shadow: 4px 0 24px rgba(59, 130, 246, 0.08) !important;
    }
    
    section[data-testid="stSidebar"] > div {
        background: transparent !important;
    }
    
    /* Change 'app' to 'Home' */
    [data-testid="stSidebarNav"] li:first-child a span {
        font-size: 0 !important;
    }
    [data-testid="stSidebarNav"] li:first-child a span::before {
        content: "🏠  Home";
        font-size: 14px !important;
        color: #1e293b;
    }
    
    /* Sidebar nav links - Light theme */
    [data-testid="stSidebarNav"] a {
        color: #475569 !important;
        border-radius: 12px;
    }
    [data-testid="stSidebarNav"] a:hover {
        background: rgba(59, 130, 246, 0.08) !important;
        color: #1e293b !important;
    }
    [data-testid="stSidebarNav"] a[aria-selected="true"] {
        background: linear-gradient(135deg, #3b82f6, #2563eb) !important;
        color: white !important;
    }
    
    /* Cards - Cream-white with blue glow futuristic style */
    .glass-card, .metric-card, .content-card, .nav-card, .audio-card, .prediction-card, .control-panel, .wave-bands-card {
        background: linear-gradient(145deg, #FFFEF9 0%, #F8F6F0 100%) !important;
        backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(59, 130, 246, 0.12) !important;
        border-radius: 20px !important;
        padding: 1.5rem;
        box-shadow: 0 4px 20px rgba(59, 130, 246, 0.08), 
                    0 8px 40px rgba(59, 130, 246, 0.04),
                    inset 0 1px 0 rgba(255, 255, 255, 0.8) !important;
    }
    
    .glass-card:hover, .metric-card:hover, .nav-card:hover {
        transform: translateY(-6px);
        box-shadow: 0 8px 32px rgba(59, 130, 246, 0.15), 
                    0 16px 48px rgba(59, 130, 246, 0.1),
                    0 0 0 1px rgba(59, 130, 246, 0.2) !important;
        border-color: rgba(59, 130, 246, 0.25) !important;
    }
    
    /* Page Header - Bright white card */
    .page-header {
        background: #FFFFFF !important;
        backdrop-filter: none !important;
        border: none !important;
        border-radius: 20px !important;
        padding: 1.5rem 2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04), 0 4px 16px rgba(0, 0, 0, 0.02) !important;
    }
    
    .page-title {
        font-size: 1.75rem;
        font-weight: 800;
        color: #1e293b !important;
    }
    
    .page-subtitle {
        color: #64748b !important;
    }
    
    /* Section Header */
    .section-header {
        background: linear-gradient(90deg, rgba(59, 130, 246, 0.04), transparent) !important;
        border-left: 4px solid #3b82f6 !important;
        padding: 0.75rem 1.25rem;
        margin: 1.5rem 0 1rem 0;
        border-radius: 0 12px 12px 0;
    }
    
    .section-title {
        color: #1e293b !important;
        font-weight: 700;
    }
    
    .section-desc {
        color: #64748b !important;
    }
    
    /* Metrics */
    [data-testid="stMetricValue"] { color: #1e293b !important; font-weight: 700; }
    [data-testid="stMetricLabel"] { color: #64748b !important; }
    .metric-value { color: #1e293b !important; font-size: 2.25rem; font-weight: 800; }
    .metric-label { color: #64748b !important; }
    .metric-icon { background: rgba(59, 130, 246, 0.1) !important; }
    
    /* Tabs - Cream-blue futuristic style */
    .stTabs [data-baseweb="tab-list"] {
        background: linear-gradient(145deg, #F5F0E8, #EBE5DC) !important;
        border-radius: 16px;
        padding: 0.5rem;
        border: 1px solid rgba(59, 130, 246, 0.15) !important;
        box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.03) !important;
    }
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        color: #64748b !important;
        border-radius: 12px;
    }
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(59, 130, 246, 0.08) !important;
        color: #1e293b !important;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #3b82f6, #2563eb) !important;
        color: white !important;
        border: none !important;
    }
    
    /* Buttons - Blue with glow futuristic */
    .stButton > button {
        background: linear-gradient(135deg, #3b82f6, #2563eb) !important;
        border: 1px solid rgba(59, 130, 246, 0.3) !important;
        color: white !important;
        border-radius: 14px;
        font-weight: 600;
        box-shadow: 0 4px 20px rgba(59, 130, 246, 0.35), 
                    0 0 40px rgba(59, 130, 246, 0.15) !important;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #2563eb, #1d4ed8) !important;
        box-shadow: 0 8px 32px rgba(59, 130, 246, 0.45), 
                    0 0 60px rgba(59, 130, 246, 0.2) !important;
        transform: translateY(-3px);
    }
    
    /* Header - Cream-blue futuristic */
    .dashboard-header { 
        border-bottom: 2px solid rgba(59, 130, 246, 0.12) !important;
        padding-bottom: 1rem;
    }
    .header-text h1 { color: #1e3a5f !important; }
    .header-text p { color: #5a7a9a !important; }
    .header-icon {
        background: linear-gradient(135deg, #3b82f6, #2563eb) !important;
        box-shadow: 0 8px 32px rgba(59, 130, 246, 0.35), 
                    0 0 50px rgba(59, 130, 246, 0.15) !important;
    }
    .header-status {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.12), rgba(16, 185, 129, 0.08)) !important;
        border: 1px solid rgba(16, 185, 129, 0.25) !important;
        color: #10b981 !important;
    }
    
    /* Wave bands */
    .wave-name { color: #1e293b !important; }
    .wave-range { color: #64748b !important; }
    .wave-value { color: #1e293b !important; }
    .wave-dot { box-shadow: 0 0 8px currentColor !important; }
    
    /* Nav cards */
    .nav-card-title { color: #1e293b !important; }
    .nav-card-desc { color: #64748b !important; }
    .nav-card-icon {
        background: rgba(59, 130, 246, 0.08) !important;
        border: 1px solid rgba(59, 130, 246, 0.1) !important;
    }
    .nav-card-tag {
        background: rgba(59, 130, 246, 0.08) !important;
        border: 1px solid rgba(59, 130, 246, 0.12) !important;
        color: #3b82f6 !important;
    }
    
    /* Footer */
    .dashboard-footer { border-top: 1px solid rgba(59, 130, 246, 0.1) !important; }
    .footer-brand { color: #1e293b !important; }
    .footer-desc { color: #64748b !important; }
    .tech-badge {
        background: rgba(59, 130, 246, 0.06) !important;
        border: 1px solid rgba(59, 130, 246, 0.12) !important;
        color: #3b82f6 !important;
    }
    
    /* Sidebar brand */
    .sidebar-brand { border-bottom: 1px solid rgba(59, 130, 246, 0.1) !important; }
    .brand-text h2 { color: #1e293b !important; }
    .brand-text span { color: #3b82f6 !important; }
    .brand-icon {
        background: linear-gradient(135deg, #3b82f6, #2563eb) !important;
        box-shadow: 0 8px 24px rgba(59, 130, 246, 0.25) !important;
    }
    
    /* Inputs */
    .stSelectbox > div > div, .stNumberInput > div > div > input {
        background: #ffffff !important;
        border: 1px solid rgba(59, 130, 246, 0.15) !important;
        color: #1e293b !important;
    }
    .stSelectbox label, .stNumberInput label { color: #64748b !important; }
    
    /* Expander */
    .streamlit-expanderHeader {
        background: #ffffff !important;
        border: 1px solid rgba(59, 130, 246, 0.1) !important;
        color: #1e293b !important;
        border-radius: 12px !important;
    }
    
    /* DataFrame */
    .stDataFrame { 
        background: #ffffff !important; 
        border-radius: 16px !important;
        box-shadow: 0 2px 8px rgba(59, 130, 246, 0.04) !important;
    }
    
    /* Alert */
    .stAlert {
        background: #ffffff !important;
        border: 1px solid rgba(59, 130, 246, 0.1) !important;
        color: #64748b !important;
        border-radius: 12px !important;
    }
    
    /* Plotly - light background */
    .js-plotly-plot .plotly .main-svg { background: transparent !important; }
    
    /* Image constraints */
    .stImage > img { max-height: 350px; object-fit: contain; }
    
    /* Markdown text */
    .stMarkdown { color: #1e293b !important; }
    .stMarkdown p { color: #475569 !important; }
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 { color: #1e293b !important; }
    
    /* Caption */
    .stCaption { color: #64748b !important; }
    
    /* Info/Success boxes */
    .stSuccess { 
        background: rgba(16, 185, 129, 0.08) !important;
        border: 1px solid rgba(16, 185, 129, 0.2) !important;
    }
    .stInfo {
        background: rgba(59, 130, 246, 0.08) !important;
        border: 1px solid rgba(59, 130, 246, 0.2) !important;
    }
</style>
"""

def get_theme_css(theme_mode="dark"):
    """Get the appropriate CSS based on theme mode."""
    if theme_mode == "light":
        return LIGHT_MODE_CSS
    return DARK_MODE_CSS

def apply_theme(st, theme_mode="dark"):
    """Apply theme CSS to Streamlit page."""
    css = get_theme_css(theme_mode)
    st.markdown(css, unsafe_allow_html=True)

# For backward compatibility
THEME_CSS = DARK_MODE_CSS

WAVE_ANIMATION_CODE = """
<style>
    /* ============================================ */
    /* FULL-SCREEN ANIMATED EEG WAVE BACKGROUND */
    /* ============================================ */
    
    .wave-background {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        pointer-events: none;
        z-index: 0;
        overflow: hidden;
        background: transparent;
    }
    
    /* Futuristic Grid Overlay */
    .wave-background::before {
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
    }
    
    /* Scanning Line Effect */
    .wave-background::after {
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
    }
    
    @keyframes scan-line {
        0% { top: 0; opacity: 1; }
        50% { opacity: 0.6; }
        100% { top: 100%; opacity: 1; }
    }
    
    /* Animated EEG Wave Lines */
    .eeg-wave {
        position: absolute;
        width: 200%;
        height: 80px;
        left: 0;
        animation: wave-flow linear infinite;
        z-index: 3;
    }
    
    .eeg-wave svg {
        width: 100%;
        height: 100%;
    }
    
    .eeg-wave path {
        fill: none;
        stroke-linecap: round;
        stroke-linejoin: round;
    }
    
    .eeg-wave-1 { top: 10%; animation-duration: 25s; }
    .eeg-wave-1 path { stroke: rgba(56, 189, 248, 0.4); stroke-width: 3; filter: drop-shadow(0 0 12px rgba(56, 189, 248, 0.5)) drop-shadow(0 0 25px rgba(56, 189, 248, 0.2)); }
    
    .eeg-wave-2 { top: 30%; animation-duration: 30s; animation-delay: -5s; }
    .eeg-wave-2 path { stroke: rgba(52, 211, 153, 0.35); stroke-width: 2.5; filter: drop-shadow(0 0 10px rgba(52, 211, 153, 0.4)) drop-shadow(0 0 20px rgba(52, 211, 153, 0.2)); }
    
    .eeg-wave-3 { top: 50%; animation-duration: 22s; animation-delay: -8s; }
    .eeg-wave-3 path { stroke: rgba(248, 113, 113, 0.3); stroke-width: 2.5; filter: drop-shadow(0 0 10px rgba(248, 113, 113, 0.4)) drop-shadow(0 0 20px rgba(248, 113, 113, 0.2)); }
    
    .eeg-wave-4 { top: 70%; animation-duration: 28s; animation-delay: -3s; }
    .eeg-wave-4 path { stroke: rgba(56, 189, 248, 0.35); stroke-width: 2.5; filter: drop-shadow(0 0 10px rgba(56, 189, 248, 0.4)) drop-shadow(0 0 20px rgba(56, 189, 248, 0.2)); }
    
    .eeg-wave-5 { top: 88%; animation-duration: 35s; animation-delay: -10s; }
    .eeg-wave-5 path { stroke: rgba(52, 211, 153, 0.4); stroke-width: 3; filter: drop-shadow(0 0 15px rgba(52, 211, 153, 0.5)) drop-shadow(0 0 30px rgba(52, 211, 153, 0.2)); }
    
    @keyframes wave-flow {
        0% { transform: translateX(0); }
        100% { transform: translateX(-50%); }
    }
    
    /* Glowing Particles */
    .glow-particle {
        position: absolute;
        border-radius: 50%;
        animation: particle-drift linear infinite;
        opacity: 0.7;
    }
    
    .glow-particle:nth-child(8) { width: 6px; height: 6px; top: 15%; left: 10%; animation-duration: 20s; background: radial-gradient(circle, rgba(56, 189, 248, 1), transparent); box-shadow: 0 0 15px rgba(56, 189, 248, 0.8); }
    .glow-particle:nth-child(9) { width: 8px; height: 8px; top: 30%; left: 85%; animation-duration: 25s; animation-delay: -5s; background: radial-gradient(circle, rgba(139, 92, 246, 1), transparent); box-shadow: 0 0 18px rgba(139, 92, 246, 0.8); }
    .glow-particle:nth-child(10) { width: 5px; height: 5px; top: 55%; left: 20%; animation-duration: 18s; animation-delay: -10s; background: radial-gradient(circle, rgba(52, 211, 153, 1), transparent); box-shadow: 0 0 12px rgba(52, 211, 153, 0.8); }
    .glow-particle:nth-child(11) { width: 7px; height: 7px; top: 75%; left: 70%; animation-duration: 22s; animation-delay: -3s; background: radial-gradient(circle, rgba(56, 189, 248, 1), transparent); box-shadow: 0 0 15px rgba(56, 189, 248, 0.8); }
    .glow-particle:nth-child(12) { width: 4px; height: 4px; top: 40%; left: 50%; animation-duration: 28s; animation-delay: -8s; background: radial-gradient(circle, rgba(251, 191, 36, 1), transparent); box-shadow: 0 0 10px rgba(251, 191, 36, 0.8); }
    .glow-particle:nth-child(13) { width: 6px; height: 6px; top: 85%; left: 30%; animation-duration: 24s; animation-delay: -12s; background: radial-gradient(circle, rgba(139, 92, 246, 1), transparent); box-shadow: 0 0 14px rgba(139, 92, 246, 0.8); }
    
    @keyframes particle-drift {
        0% { transform: translate(0, 0) scale(1); opacity: 0.5; }
        25% { transform: translate(50px, -30px) scale(1.3); opacity: 0.9; }
        50% { transform: translate(100px, 20px) scale(0.8); opacity: 0.6; }
        75% { transform: translate(50px, -10px) scale(1.1); opacity: 0.8; }
        100% { transform: translate(0, 0) scale(1); opacity: 0.5; }
    }
    
    /* Pulse Rings */
    .pulse-ring {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        border-radius: 50%;
        border: 1px solid rgba(56, 189, 248, 0.3);
        animation: pulse-expand 4s ease-out infinite;
    }
    .pulse-ring:nth-child(14) { animation-delay: 0s; }
    .pulse-ring:nth-child(15) { animation-delay: 1s; }
    .pulse-ring:nth-child(16) { animation-delay: 2s; }
    .pulse-ring:nth-child(17) { animation-delay: 3s; }
    
    @keyframes pulse-expand {
        0% { width: 50px; height: 50px; opacity: 0.8; border-color: rgba(56, 189, 248, 0.5); }
        100% { width: 600px; height: 600px; opacity: 0; border-color: rgba(139, 92, 246, 0.1); }
    }
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
"""
