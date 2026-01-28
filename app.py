"""
🌬️ AIR GUARD - PM2.5 Forecasting & AQI Alerts
Modern Dashboard with Beautiful Glassmorphism UI
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import json
from pathlib import Path
from datetime import datetime, timedelta
import random

# ═══════════════════════════════════════════════════════════════════════════════
# 📌 PAGE CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="AIR GUARD 🌬️ PM2.5 Forecast",
    page_icon="🌬️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ═══════════════════════════════════════════════════════════════════════════════
# 🎨 CUSTOM CSS - ULTRA MODERN GLASSMORPHISM DESIGN
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
/* Import Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800;900&family=Rajdhani:wght@300;400;500;600;700&family=Space+Grotesk:wght@300;400;500;600;700&display=swap');

/* Main Background with Animated Gradient */
.stApp {
    background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e, #0f0c29);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
}

@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Hide Streamlit Default Elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
.stDeployButton {display: none;}
header[data-testid="stHeader"] {
    background: transparent;
}

/* Sidebar Styling */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, rgba(15, 12, 41, 0.95) 0%, rgba(48, 43, 99, 0.95) 100%);
    border-right: 1px solid rgba(255, 255, 255, 0.1);
}

section[data-testid="stSidebar"] .stRadio > label {
    color: #ffffff !important;
    font-family: 'Space Grotesk', sans-serif;
}

/* Custom Scrollbar */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}
::-webkit-scrollbar-track {
    background: rgba(255, 255, 255, 0.05);
}
::-webkit-scrollbar-thumb {
    background: linear-gradient(45deg, #667eea, #764ba2);
    border-radius: 10px;
}

/* Main Title Styling */
.main-title {
    font-family: 'Orbitron', monospace;
    font-size: 3.5rem;
    font-weight: 800;
    text-align: center;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #f5576c 75%, #fda085 100%);
    background-size: 300% 300%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: titleGradient 5s ease infinite;
    text-shadow: 0 0 30px rgba(102, 126, 234, 0.5);
    margin-bottom: 0.5rem;
    letter-spacing: 3px;
}

@keyframes titleGradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.sub-title {
    font-family: 'Rajdhani', sans-serif;
    font-size: 1.3rem;
    color: rgba(255, 255, 255, 0.7);
    text-align: center;
    margin-bottom: 2rem;
    letter-spacing: 5px;
    text-transform: uppercase;
}

/* Glassmorphism Card */
.glass-card {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-radius: 24px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 2rem;
    margin: 1rem 0;
    box-shadow: 
        0 8px 32px rgba(0, 0, 0, 0.3),
        inset 0 0 32px rgba(255, 255, 255, 0.02);
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.glass-card:hover {
    transform: translateY(-5px);
    box-shadow: 
        0 15px 45px rgba(102, 126, 234, 0.3),
        inset 0 0 32px rgba(255, 255, 255, 0.05);
    border-color: rgba(102, 126, 234, 0.4);
}

/* Stats Cards with Neon Glow */
.stat-card {
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.2) 0%, rgba(118, 75, 162, 0.2) 100%);
    backdrop-filter: blur(20px);
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.15);
    padding: 1.5rem;
    text-align: center;
    position: relative;
    overflow: hidden;
    transition: all 0.3s ease;
}

.stat-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
    transition: left 0.5s ease;
}

.stat-card:hover::before {
    left: 100%;
}

.stat-card:hover {
    transform: scale(1.02);
    box-shadow: 0 0 30px rgba(102, 126, 234, 0.4);
}

.stat-icon {
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
}

.stat-value {
    font-family: 'Orbitron', monospace;
    font-size: 2.2rem;
    font-weight: 700;
    background: linear-gradient(135deg, #ffffff 0%, #a8c0ff 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0.3rem 0;
}

.stat-label {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.9rem;
    color: rgba(255, 255, 255, 0.7);
    text-transform: uppercase;
    letter-spacing: 2px;
}

/* AQI Level Cards */
.aqi-good {
    background: linear-gradient(135deg, rgba(0, 200, 83, 0.3) 0%, rgba(0, 230, 118, 0.2) 100%);
    border-color: rgba(0, 200, 83, 0.5);
    box-shadow: 0 0 25px rgba(0, 200, 83, 0.3);
}

.aqi-moderate {
    background: linear-gradient(135deg, rgba(255, 193, 7, 0.3) 0%, rgba(255, 214, 0, 0.2) 100%);
    border-color: rgba(255, 193, 7, 0.5);
    box-shadow: 0 0 25px rgba(255, 193, 7, 0.3);
}

.aqi-unhealthy-sensitive {
    background: linear-gradient(135deg, rgba(255, 152, 0, 0.3) 0%, rgba(255, 183, 77, 0.2) 100%);
    border-color: rgba(255, 152, 0, 0.5);
    box-shadow: 0 0 25px rgba(255, 152, 0, 0.3);
}

.aqi-unhealthy {
    background: linear-gradient(135deg, rgba(244, 67, 54, 0.3) 0%, rgba(239, 83, 80, 0.2) 100%);
    border-color: rgba(244, 67, 54, 0.5);
    box-shadow: 0 0 25px rgba(244, 67, 54, 0.3);
}

.aqi-very-unhealthy {
    background: linear-gradient(135deg, rgba(156, 39, 176, 0.3) 0%, rgba(186, 104, 200, 0.2) 100%);
    border-color: rgba(156, 39, 176, 0.5);
    box-shadow: 0 0 25px rgba(156, 39, 176, 0.3);
}

.aqi-hazardous {
    background: linear-gradient(135deg, rgba(128, 0, 0, 0.3) 0%, rgba(183, 28, 28, 0.2) 100%);
    border-color: rgba(128, 0, 0, 0.5);
    box-shadow: 0 0 25px rgba(128, 0, 0, 0.3);
}

/* Section Headers */
.section-header {
    font-family: 'Orbitron', monospace;
    font-size: 1.8rem;
    font-weight: 600;
    color: #ffffff;
    margin: 2rem 0 1rem 0;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid;
    border-image: linear-gradient(90deg, #667eea, #764ba2, transparent) 1;
    display: flex;
    align-items: center;
    gap: 0.8rem;
}

/* Table Styling */
.styled-table {
    width: 100%;
    border-collapse: collapse;
    font-family: 'Space Grotesk', sans-serif;
    background: rgba(255, 255, 255, 0.02);
    border-radius: 16px;
    overflow: hidden;
}

.styled-table thead tr {
    background: linear-gradient(90deg, rgba(102, 126, 234, 0.3), rgba(118, 75, 162, 0.3));
    text-transform: uppercase;
    letter-spacing: 1px;
}

.styled-table th,
.styled-table td {
    padding: 15px 20px;
    text-align: left;
    color: #ffffff;
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
}

.styled-table tbody tr {
    transition: all 0.3s ease;
}

.styled-table tbody tr:hover {
    background: rgba(102, 126, 234, 0.15);
}

/* Animated Background Particles */
.particles {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    overflow: hidden;
    z-index: -1;
}

.particle {
    position: absolute;
    width: 6px;
    height: 6px;
    background: radial-gradient(circle, rgba(102, 126, 234, 0.8) 0%, transparent 70%);
    border-radius: 50%;
    animation: float 20s infinite ease-in-out;
}

@keyframes float {
    0%, 100% {
        transform: translateY(100vh) rotate(0deg);
        opacity: 0;
    }
    10% {
        opacity: 1;
    }
    90% {
        opacity: 1;
    }
    100% {
        transform: translateY(-100vh) rotate(720deg);
        opacity: 0;
    }
}

/* Navigation Pills */
.nav-pills {
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin: 2rem 0;
    flex-wrap: wrap;
}

.nav-pill {
    font-family: 'Space Grotesk', sans-serif;
    padding: 0.8rem 1.5rem;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 50px;
    color: #ffffff;
    cursor: pointer;
    transition: all 0.3s ease;
    text-decoration: none;
}

.nav-pill:hover, .nav-pill.active {
    background: linear-gradient(135deg, #667eea, #764ba2);
    border-color: transparent;
    box-shadow: 0 5px 25px rgba(102, 126, 234, 0.4);
}

/* Pulse Animation for Alerts */
.pulse {
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0% { box-shadow: 0 0 0 0 rgba(102, 126, 234, 0.4); }
    70% { box-shadow: 0 0 0 15px rgba(102, 126, 234, 0); }
    100% { box-shadow: 0 0 0 0 rgba(102, 126, 234, 0); }
}

/* Progress Bar */
.progress-container {
    width: 100%;
    height: 10px;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 10px;
    overflow: hidden;
    margin: 1rem 0;
}

.progress-bar {
    height: 100%;
    background: linear-gradient(90deg, #667eea, #764ba2, #f093fb);
    background-size: 200% 100%;
    animation: progressAnim 2s linear infinite;
    border-radius: 10px;
}

@keyframes progressAnim {
    0% { background-position: 200% 0; }
    100% { background-position: 0 0; }
}

/* Chart Container */
.chart-container {
    background: rgba(255, 255, 255, 0.02);
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 1rem;
    margin: 1rem 0;
}

/* Info Box */
.info-box {
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.15) 0%, rgba(118, 75, 162, 0.15) 100%);
    border-left: 4px solid #667eea;
    border-radius: 0 16px 16px 0;
    padding: 1.2rem 1.5rem;
    margin: 1rem 0;
    color: rgba(255, 255, 255, 0.9);
    font-family: 'Space Grotesk', sans-serif;
}

/* Warning Box */
.warning-box {
    background: linear-gradient(135deg, rgba(255, 152, 0, 0.15) 0%, rgba(255, 193, 7, 0.15) 100%);
    border-left: 4px solid #ff9800;
    border-radius: 0 16px 16px 0;
    padding: 1.2rem 1.5rem;
    margin: 1rem 0;
    color: rgba(255, 255, 255, 0.9);
    font-family: 'Space Grotesk', sans-serif;
}

/* Success Box */
.success-box {
    background: linear-gradient(135deg, rgba(0, 200, 83, 0.15) 0%, rgba(0, 230, 118, 0.15) 100%);
    border-left: 4px solid #00c853;
    border-radius: 0 16px 16px 0;
    padding: 1.2rem 1.5rem;
    margin: 1rem 0;
    color: rgba(255, 255, 255, 0.9);
    font-family: 'Space Grotesk', sans-serif;
}

/* Floating Labels */
.floating-label {
    position: relative;
    display: inline-block;
}

.floating-label::after {
    content: '';
    position: absolute;
    bottom: -5px;
    left: 0;
    width: 100%;
    height: 2px;
    background: linear-gradient(90deg, #667eea, #764ba2);
    transform: scaleX(0);
    transition: transform 0.3s ease;
}

.floating-label:hover::after {
    transform: scaleX(1);
}

/* Metric Display */
.metric-display {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    padding: 2rem;
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
    border-radius: 50%;
    width: 180px;
    height: 180px;
    margin: 0 auto;
    border: 3px solid rgba(102, 126, 234, 0.3);
    box-shadow: 
        0 0 30px rgba(102, 126, 234, 0.2),
        inset 0 0 30px rgba(102, 126, 234, 0.1);
}

.metric-value-large {
    font-family: 'Orbitron', monospace;
    font-size: 3rem;
    font-weight: 800;
    background: linear-gradient(135deg, #ffffff 0%, #667eea 50%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.metric-unit {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1rem;
    color: rgba(255, 255, 255, 0.6);
    margin-top: 0.3rem;
}

/* Team Member Cards */
.team-card {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(20px);
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 1.5rem;
    text-align: center;
    transition: all 0.4s ease;
}

.team-card:hover {
    transform: translateY(-10px) scale(1.02);
    box-shadow: 0 20px 40px rgba(102, 126, 234, 0.3);
    border-color: rgba(102, 126, 234, 0.5);
}

.team-avatar {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    background: linear-gradient(135deg, #667eea, #764ba2);
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 0 auto 1rem auto;
    font-size: 2.5rem;
    box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
}

.team-name {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.2rem;
    font-weight: 600;
    color: #ffffff;
    margin-bottom: 0.3rem;
}

.team-role {
    font-family: 'Rajdhani', sans-serif;
    font-size: 0.9rem;
    color: rgba(255, 255, 255, 0.6);
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* Footer */
.footer {
    text-align: center;
    padding: 2rem;
    margin-top: 3rem;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    font-family: 'Space Grotesk', sans-serif;
    color: rgba(255, 255, 255, 0.5);
}

/* Responsive Design */
@media (max-width: 768px) {
    .main-title {
        font-size: 2rem;
    }
    .stat-value {
        font-size: 1.5rem;
    }
    .metric-display {
        width: 140px;
        height: 140px;
    }
    .metric-value-large {
        font-size: 2rem;
    }
}

/* Streamlit specific overrides */
.stSelectbox label, .stSlider label, .stMultiSelect label {
    color: #ffffff !important;
    font-family: 'Space Grotesk', sans-serif !important;
}

div[data-testid="stMetricValue"] {
    font-family: 'Orbitron', monospace !important;
    color: #ffffff !important;
}

div[data-testid="stMetricLabel"] {
    font-family: 'Space Grotesk', sans-serif !important;
    color: rgba(255, 255, 255, 0.7) !important;
}

.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    background: rgba(255, 255, 255, 0.02);
    border-radius: 16px;
    padding: 8px;
}

.stTabs [data-baseweb="tab"] {
    font-family: 'Space Grotesk', sans-serif;
    color: rgba(255, 255, 255, 0.7);
    border-radius: 12px;
    padding: 10px 20px;
    background: transparent;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #667eea, #764ba2) !important;
    color: #ffffff !important;
}

/* Plotly chart background fix */
.js-plotly-plot .plotly .main-svg {
    background: transparent !important;
}
</style>

<!-- Floating Particles Background -->
<div class="particles">
    <div class="particle" style="left: 5%; animation-delay: 0s;"></div>
    <div class="particle" style="left: 15%; animation-delay: 2s;"></div>
    <div class="particle" style="left: 25%; animation-delay: 4s;"></div>
    <div class="particle" style="left: 35%; animation-delay: 1s;"></div>
    <div class="particle" style="left: 45%; animation-delay: 3s;"></div>
    <div class="particle" style="left: 55%; animation-delay: 5s;"></div>
    <div class="particle" style="left: 65%; animation-delay: 2s;"></div>
    <div class="particle" style="left: 75%; animation-delay: 4s;"></div>
    <div class="particle" style="left: 85%; animation-delay: 1s;"></div>
    <div class="particle" style="left: 95%; animation-delay: 3s;"></div>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# 📂 DATA LOADING FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════
DATA_DIR = Path("data/processed")

@st.cache_data
def load_data():
    """Load all processed data files."""
    data = {}
    
    # Load cleaned data
    cleaned_path = DATA_DIR / "cleaned.parquet"
    if cleaned_path.exists():
        data['cleaned'] = pd.read_parquet(cleaned_path)
    
    # Load supervised metrics (metrics.json has direct structure)
    metrics_path = DATA_DIR / "metrics.json"
    if metrics_path.exists():
        with open(metrics_path, 'r') as f:
            metrics_raw = json.load(f)
            data['metrics'] = metrics_raw
            # Extract accuracy/f1 for supervised
            data['supervised_accuracy'] = metrics_raw.get('accuracy', 0)
            data['supervised_f1'] = metrics_raw.get('f1_macro', 0)
    
    # Load Self-Training metrics (has test_metrics nested)
    self_metrics_path = DATA_DIR / "metrics_self_training.json"
    if self_metrics_path.exists():
        with open(self_metrics_path, 'r') as f:
            self_raw = json.load(f)
            data['metrics_self_training'] = self_raw
            test_m = self_raw.get('test_metrics', {})
            data['self_training_accuracy'] = test_m.get('accuracy', 0)
            data['self_training_f1'] = test_m.get('f1_macro', 0)
    
    # Load Co-Training metrics (has test_metrics nested)
    co_metrics_path = DATA_DIR / "metrics_co_training.json"
    if co_metrics_path.exists():
        with open(co_metrics_path, 'r') as f:
            co_raw = json.load(f)
            data['metrics_co_training'] = co_raw
            test_m = co_raw.get('test_metrics', {})
            data['co_training_accuracy'] = test_m.get('accuracy', 0)
            data['co_training_f1'] = test_m.get('f1_macro', 0)
    
    # Load predictions (CSV files)
    pred_files = {
        'preds_self_training': 'predictions_self_training_sample.csv',
        'preds_co_training': 'predictions_co_training_sample.csv',
        'preds_classifier': 'predictions_sample.csv'
    }
    
    for key, filename in pred_files.items():
        path = DATA_DIR / filename
        if path.exists():
            data[key] = pd.read_csv(path)
    
    # Build semi-supervised report for comparison page
    data['semi_report'] = {
        'self_training': {
            'accuracy': data.get('self_training_accuracy', 0),
            'f1_score': data.get('self_training_f1', 0),
            'precision': data.get('metrics_self_training', {}).get('test_metrics', {}).get('report', {}).get('macro avg', {}).get('precision', 0),
            'recall': data.get('metrics_self_training', {}).get('test_metrics', {}).get('report', {}).get('macro avg', {}).get('recall', 0)
        },
        'co_training': {
            'accuracy': data.get('co_training_accuracy', 0),
            'f1_score': data.get('co_training_f1', 0),
            'precision': data.get('metrics_co_training', {}).get('test_metrics', {}).get('report', {}).get('macro avg', {}).get('precision', 0),
            'recall': data.get('metrics_co_training', {}).get('test_metrics', {}).get('report', {}).get('macro avg', {}).get('recall', 0)
        },
        'supervised': {
            'accuracy': data.get('supervised_accuracy', 0),
            'f1_score': data.get('supervised_f1', 0),
            'precision': data.get('metrics', {}).get('report', {}).get('macro avg', {}).get('precision', 0),
            'recall': data.get('metrics', {}).get('report', {}).get('macro avg', {}).get('recall', 0)
        }
    }
    
    return data

# ═══════════════════════════════════════════════════════════════════════════════
# 🎯 HELPER FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════
def get_aqi_level(pm25):
    """Determine AQI level and corresponding info."""
    if pm25 <= 12:
        return "Good", "#00c853", "aqi-good", "😊"
    elif pm25 <= 35.4:
        return "Moderate", "#ffc107", "aqi-moderate", "😐"
    elif pm25 <= 55.4:
        return "Unhealthy for Sensitive", "#ff9800", "aqi-unhealthy-sensitive", "😷"
    elif pm25 <= 150.4:
        return "Unhealthy", "#f44336", "aqi-unhealthy", "🤢"
    elif pm25 <= 250.4:
        return "Very Unhealthy", "#9c27b0", "aqi-very-unhealthy", "💀"
    else:
        return "Hazardous", "#800000", "aqi-hazardous", "☠️"

def create_gauge_chart(value, title, max_val=300):
    """Create an animated gauge chart."""
    level, color, _, emoji = get_aqi_level(value)
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=value,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': f"{title} {emoji}", 'font': {'size': 20, 'color': 'white', 'family': 'Space Grotesk'}},
        number={'font': {'size': 50, 'color': 'white', 'family': 'Orbitron'}},
        gauge={
            'axis': {'range': [0, max_val], 'tickwidth': 1, 'tickcolor': "white", 'tickfont': {'color': 'white'}},
            'bar': {'color': color, 'thickness': 0.8},
            'bgcolor': "rgba(255,255,255,0.1)",
            'borderwidth': 2,
            'bordercolor': "rgba(255,255,255,0.2)",
            'steps': [
                {'range': [0, 12], 'color': 'rgba(0, 200, 83, 0.3)'},
                {'range': [12, 35.4], 'color': 'rgba(255, 193, 7, 0.3)'},
                {'range': [35.4, 55.4], 'color': 'rgba(255, 152, 0, 0.3)'},
                {'range': [55.4, 150.4], 'color': 'rgba(244, 67, 54, 0.3)'},
                {'range': [150.4, 250.4], 'color': 'rgba(156, 39, 176, 0.3)'},
                {'range': [250.4, 300], 'color': 'rgba(128, 0, 0, 0.3)'}
            ],
            'threshold': {
                'line': {'color': "white", 'width': 4},
                'thickness': 0.8,
                'value': value
            }
        }
    ))
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font={'color': 'white'},
        height=300,
        margin=dict(l=30, r=30, t=60, b=30)
    )
    
    return fig

def create_time_series_chart(df, y_col, title, color='#667eea'):
    """Create an interactive time series chart."""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=df.index if isinstance(df.index, pd.DatetimeIndex) else df['datetime'] if 'datetime' in df.columns else range(len(df)),
        y=df[y_col],
        mode='lines',
        name=y_col,
        line=dict(color=color, width=2),
        fill='tozeroy',
        fillcolor=f'rgba{tuple(list(int(color.lstrip("#")[i:i+2], 16) for i in (0, 2, 4)) + [0.2])}'
    ))
    
    fig.update_layout(
        title=dict(text=title, font=dict(size=18, color='white', family='Orbitron')),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        xaxis=dict(
            gridcolor='rgba(255,255,255,0.1)',
            showgrid=True,
            zeroline=False
        ),
        yaxis=dict(
            gridcolor='rgba(255,255,255,0.1)',
            showgrid=True,
            zeroline=False
        ),
        hovermode='x unified',
        height=400,
        margin=dict(l=50, r=30, t=60, b=50)
    )
    
    return fig

def create_comparison_chart(data_dict, title):
    """Create a comparison bar chart."""
    fig = go.Figure()
    
    colors = ['#667eea', '#764ba2', '#f093fb', '#f5576c', '#fda085']
    
    for idx, (name, value) in enumerate(data_dict.items()):
        fig.add_trace(go.Bar(
            name=name,
            x=[name],
            y=[value],
            marker_color=colors[idx % len(colors)],
            text=[f'{value:.2%}' if value < 1 else f'{value:.2f}'],
            textposition='outside',
            textfont=dict(color='white', size=14, family='Orbitron')
        ))
    
    fig.update_layout(
        title=dict(text=title, font=dict(size=18, color='white', family='Orbitron')),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        xaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
        yaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
        showlegend=False,
        height=400,
        margin=dict(l=50, r=30, t=60, b=50)
    )
    
    return fig

# ═══════════════════════════════════════════════════════════════════════════════
# 📱 SIDEBAR NAVIGATION
# ═══════════════════════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 1rem 0;">
        <div style="font-size: 4rem; margin-bottom: 0.5rem;">🌬️</div>
        <div style="font-family: 'Orbitron', monospace; font-size: 1.5rem; font-weight: 700; 
                    background: linear-gradient(135deg, #667eea, #764ba2);
                    -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            AIR GUARD
        </div>
        <div style="font-family: 'Rajdhani', sans-serif; font-size: 0.8rem; 
                    color: rgba(255,255,255,0.6); letter-spacing: 2px; margin-top: 0.3rem;">
            PM2.5 MONITORING SYSTEM
        </div>
    </div>
    <hr style="border-color: rgba(255,255,255,0.1); margin: 1rem 0;">
    """, unsafe_allow_html=True)
    
    page = st.radio(
        "📍 Navigation",
        ["🏠 Dashboard", "🔮 Predictions", "📊 Model Comparison", "🗺️ Stations", "ℹ️ About"],
        label_visibility="collapsed"
    )
    
    st.markdown("<hr style='border-color: rgba(255,255,255,0.1); margin: 1rem 0;'>", unsafe_allow_html=True)
    
    # Current Time Display
    st.markdown(f"""
    <div style="text-align: center; padding: 1rem; 
                background: rgba(255,255,255,0.05); border-radius: 16px; margin-top: 1rem;">
        <div style="font-family: 'Space Grotesk'; color: rgba(255,255,255,0.6); font-size: 0.8rem;">
            🕐 Current Time
        </div>
        <div style="font-family: 'Orbitron'; color: #ffffff; font-size: 1.2rem; margin-top: 0.3rem;">
            {datetime.now().strftime('%H:%M:%S')}
        </div>
        <div style="font-family: 'Rajdhani'; color: rgba(255,255,255,0.5); font-size: 0.9rem;">
            {datetime.now().strftime('%d %B %Y')}
        </div>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# 📄 PAGE CONTENT
# ═══════════════════════════════════════════════════════════════════════════════

# Load data
data = load_data()

# ─────────────────────────────────────────────────────────────────────────────
# 🏠 DASHBOARD PAGE
# ─────────────────────────────────────────────────────────────────────────────
if page == "🏠 Dashboard":
    st.markdown("""
    <h1 class="main-title">AIR GUARD</h1>
    <p class="sub-title">PM2.5 Forecasting & AQI Alert System</p>
    """, unsafe_allow_html=True)
    
    if 'cleaned' in data:
        df = data['cleaned']
        
        # Key Metrics Row
        col1, col2, col3, col4 = st.columns(4)
        
        # Calculate metrics
        current_pm25 = df['PM2.5'].iloc[-1] if 'PM2.5' in df.columns else 0
        avg_pm25 = df['PM2.5'].mean() if 'PM2.5' in df.columns else 0
        max_pm25 = df['PM2.5'].max() if 'PM2.5' in df.columns else 0
        total_records = len(df)
        
        level, color, css_class, emoji = get_aqi_level(current_pm25)
        
        with col1:
            st.markdown(f"""
            <div class="stat-card {css_class}">
                <div class="stat-icon">{emoji}</div>
                <div class="stat-value">{current_pm25:.1f}</div>
                <div class="stat-label">Current PM2.5</div>
                <div style="font-size: 0.8rem; color: {color}; margin-top: 0.5rem;">{level}</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-icon">📊</div>
                <div class="stat-value">{avg_pm25:.1f}</div>
                <div class="stat-label">Average PM2.5</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-icon">⚠️</div>
                <div class="stat-value">{max_pm25:.1f}</div>
                <div class="stat-label">Maximum PM2.5</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-icon">📈</div>
                <div class="stat-value">{total_records:,}</div>
                <div class="stat-label">Total Records</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # AQI Gauge and Time Series
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown('<div class="section-header">🎯 Air Quality Index</div>', unsafe_allow_html=True)
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            gauge = create_gauge_chart(current_pm25, "PM2.5 Level")
            st.plotly_chart(gauge, use_container_width=True)
            
            # AQI Scale Legend
            st.markdown("""
            <div style="padding: 1rem; font-family: 'Space Grotesk';">
                <div style="display: flex; align-items: center; margin: 0.3rem 0;">
                    <div style="width: 15px; height: 15px; background: #00c853; border-radius: 50%; margin-right: 10px;"></div>
                    <span style="color: rgba(255,255,255,0.8);">Good (0-12)</span>
                </div>
                <div style="display: flex; align-items: center; margin: 0.3rem 0;">
                    <div style="width: 15px; height: 15px; background: #ffc107; border-radius: 50%; margin-right: 10px;"></div>
                    <span style="color: rgba(255,255,255,0.8);">Moderate (12-35.4)</span>
                </div>
                <div style="display: flex; align-items: center; margin: 0.3rem 0;">
                    <div style="width: 15px; height: 15px; background: #ff9800; border-radius: 50%; margin-right: 10px;"></div>
                    <span style="color: rgba(255,255,255,0.8);">USG (35.4-55.4)</span>
                </div>
                <div style="display: flex; align-items: center; margin: 0.3rem 0;">
                    <div style="width: 15px; height: 15px; background: #f44336; border-radius: 50%; margin-right: 10px;"></div>
                    <span style="color: rgba(255,255,255,0.8);">Unhealthy (55.4-150.4)</span>
                </div>
                <div style="display: flex; align-items: center; margin: 0.3rem 0;">
                    <div style="width: 15px; height: 15px; background: #9c27b0; border-radius: 50%; margin-right: 10px;"></div>
                    <span style="color: rgba(255,255,255,0.8);">Very Unhealthy (150.4-250.4)</span>
                </div>
                <div style="display: flex; align-items: center; margin: 0.3rem 0;">
                    <div style="width: 15px; height: 15px; background: #800000; border-radius: 50%; margin-right: 10px;"></div>
                    <span style="color: rgba(255,255,255,0.8);">Hazardous (>250.4)</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="section-header">📈 PM2.5 Trend Analysis</div>', unsafe_allow_html=True)
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            
            # Sample data for visualization (last 1000 points)
            sample_df = df.tail(1000).copy()
            
            if 'PM2.5' in sample_df.columns:
                fig = create_time_series_chart(sample_df, 'PM2.5', 'PM2.5 Concentration Over Time', '#667eea')
                st.plotly_chart(fig, use_container_width=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Station Distribution
        st.markdown('<div class="section-header">🗺️ Station Overview</div>', unsafe_allow_html=True)
        
        if 'station' in df.columns:
            station_stats = df.groupby('station')['PM2.5'].agg(['mean', 'max', 'min', 'std']).round(2)
            station_stats.columns = ['Average', 'Maximum', 'Minimum', 'Std Dev']
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                
                fig = px.bar(
                    x=station_stats.index,
                    y=station_stats['Average'],
                    color=station_stats['Average'],
                    color_continuous_scale=['#00c853', '#ffc107', '#ff9800', '#f44336'],
                    labels={'x': 'Station', 'y': 'Average PM2.5'},
                    title='Average PM2.5 by Station'
                )
                
                fig.update_layout(
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='white', family='Space Grotesk'),
                    title_font=dict(size=16, family='Orbitron'),
                    xaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
                    yaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
                    coloraxis_showscale=False,
                    height=400
                )
                
                st.plotly_chart(fig, use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)
            
            with col2:
                st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                
                fig = px.box(
                    df.sample(min(10000, len(df))),
                    x='station',
                    y='PM2.5',
                    color='station',
                    title='PM2.5 Distribution by Station'
                )
                
                fig.update_layout(
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    font=dict(color='white', family='Space Grotesk'),
                    title_font=dict(size=16, family='Orbitron'),
                    xaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
                    yaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
                    showlegend=False,
                    height=400
                )
                
                st.plotly_chart(fig, use_container_width=True)
                st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="warning-box">
            ⚠️ <strong>Data Not Found:</strong> Please run the preprocessing notebook first to generate the cleaned data.
        </div>
        """, unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# 🔮 PREDICTIONS PAGE
# ─────────────────────────────────────────────────────────────────────────────
elif page == "🔮 Predictions":
    st.markdown("""
    <h1 class="main-title">🔮 PM2.5 Predictions</h1>
    <p class="sub-title">Semi-Supervised Learning Results</p>
    """, unsafe_allow_html=True)
    
    # Model Selection
    tabs = st.tabs(["🎯 Self-Training", "🤝 Co-Training", "📊 Supervised"])
    
    pred_files = {
        'Self-Training': ('preds_self_training', 'self_training_accuracy'),
        'Co-Training': ('preds_co_training', 'co_training_accuracy'),
        'Supervised': ('preds_classifier', 'supervised_accuracy')
    }
    
    for tab, (name, (key, acc_key)) in zip(tabs, pred_files.items()):
        with tab:
            if key in data:
                pred_df = data[key]
                
                st.markdown(f'<div class="section-header">📊 {name} Predictions</div>', unsafe_allow_html=True)
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    total = len(pred_df)
                    st.markdown(f"""
                    <div class="stat-card">
                        <div class="stat-icon">📈</div>
                        <div class="stat-value">{total:,}</div>
                        <div class="stat-label">Total Predictions</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Get prediction column
                pred_col = 'y_pred' if 'y_pred' in pred_df.columns else pred_df.columns[-1]
                
                with col2:
                    if pred_col in pred_df.columns:
                        unique_classes = pred_df[pred_col].nunique()
                        st.markdown(f"""
                        <div class="stat-card">
                            <div class="stat-icon">🏷️</div>
                            <div class="stat-value">{unique_classes}</div>
                            <div class="stat-label">AQI Classes</div>
                        </div>
                        """, unsafe_allow_html=True)
                
                with col3:
                    acc = data.get(acc_key, 0)
                    st.markdown(f"""
                    <div class="stat-card">
                        <div class="stat-icon">✅</div>
                        <div class="stat-value">{acc:.1%}</div>
                        <div class="stat-label">Accuracy</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                st.markdown("<br>", unsafe_allow_html=True)
                
                # Prediction Distribution
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                    
                    if pred_col in pred_df.columns:
                        class_dist = pred_df[pred_col].value_counts()
                        
                        fig = px.pie(
                            values=class_dist.values,
                            names=class_dist.index,
                            title=f'{name} - AQI Class Distribution',
                            color_discrete_sequence=px.colors.sequential.Plasma_r
                        )
                        
                        fig.update_layout(
                            paper_bgcolor='rgba(0,0,0,0)',
                            plot_bgcolor='rgba(0,0,0,0)',
                            font=dict(color='white', family='Space Grotesk'),
                            title_font=dict(size=16, family='Orbitron'),
                            height=400
                        )
                        
                        st.plotly_chart(fig, use_container_width=True)
                    
                    st.markdown('</div>', unsafe_allow_html=True)
                
                with col2:
                    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
                    
                    if pred_col in pred_df.columns:
                        class_dist = pred_df[pred_col].value_counts().sort_index()
                        
                        fig = go.Figure(go.Bar(
                            x=class_dist.index.astype(str),
                            y=class_dist.values,
                            marker_color=['#00c853', '#ffc107', '#ff9800', '#f44336', '#9c27b0', '#800000'][:len(class_dist)],
                            text=class_dist.values,
                            textposition='outside',
                            textfont=dict(color='white', size=12)
                        ))
                        
                        fig.update_layout(
                            title=f'{name} - Predictions by Class',
                            paper_bgcolor='rgba(0,0,0,0)',
                            plot_bgcolor='rgba(0,0,0,0)',
                            font=dict(color='white', family='Space Grotesk'),
                            title_font=dict(size=16, family='Orbitron'),
                            xaxis=dict(gridcolor='rgba(255,255,255,0.1)', title='AQI Class'),
                            yaxis=dict(gridcolor='rgba(255,255,255,0.1)', title='Count'),
                            height=400
                        )
                        
                        st.plotly_chart(fig, use_container_width=True)
                    
                    st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="warning-box">
                    ⚠️ <strong>{name} predictions not found.</strong> Run the corresponding notebook first.
                </div>
                """, unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# 📊 MODEL COMPARISON PAGE
# ─────────────────────────────────────────────────────────────────────────────
elif page == "📊 Model Comparison":
    st.markdown("""
    <h1 class="main-title">📊 Model Comparison</h1>
    <p class="sub-title">Semi-Supervised vs Supervised Learning</p>
    """, unsafe_allow_html=True)
    
    if 'semi_report' in data:
        report = data['semi_report']
        
        # Summary Cards
        st.markdown('<div class="section-header">🏆 Model Performance Summary</div>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            self_f1 = report.get('self_training', {}).get('f1_score', 0)
            st.markdown(f"""
            <div class="stat-card pulse">
                <div class="stat-icon">🎯</div>
                <div class="stat-value">{self_f1:.1%}</div>
                <div class="stat-label">Self-Training F1</div>
                <div style="font-size: 0.8rem; color: #00c853; margin-top: 0.5rem;">Best Performer</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            co_f1 = report.get('co_training', {}).get('f1_score', 0)
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-icon">🤝</div>
                <div class="stat-value">{co_f1:.1%}</div>
                <div class="stat-label">Co-Training F1</div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            sup_acc = report.get('supervised', {}).get('accuracy', 0)
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-icon">📈</div>
                <div class="stat-value">{sup_acc:.1%}</div>
                <div class="stat-label">Supervised Accuracy</div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Detailed Comparison Charts
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            
            # F1 Score Comparison
            models = ['Self-Training', 'Co-Training', 'Supervised']
            f1_scores = [
                report.get('self_training', {}).get('f1_score', 0),
                report.get('co_training', {}).get('f1_score', 0),
                report.get('supervised', {}).get('f1_score', 0)
            ]
            
            fig = go.Figure(go.Bar(
                x=models,
                y=f1_scores,
                marker_color=['#667eea', '#764ba2', '#f093fb'],
                text=[f'{s:.1%}' for s in f1_scores],
                textposition='outside',
                textfont=dict(color='white', size=14, family='Orbitron')
            ))
            
            fig.update_layout(
                title='F1 Score Comparison',
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='white', family='Space Grotesk'),
                title_font=dict(size=18, family='Orbitron'),
                xaxis=dict(gridcolor='rgba(255,255,255,0.1)'),
                yaxis=dict(gridcolor='rgba(255,255,255,0.1)', tickformat='.0%'),
                height=400
            )
            
            st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            
            # Radar Chart for Multiple Metrics
            categories = ['Accuracy', 'Precision', 'Recall', 'F1 Score']
            
            self_metrics = [
                report.get('self_training', {}).get('accuracy', 0),
                report.get('self_training', {}).get('precision', 0),
                report.get('self_training', {}).get('recall', 0),
                report.get('self_training', {}).get('f1_score', 0)
            ]
            
            co_metrics = [
                report.get('co_training', {}).get('accuracy', 0),
                report.get('co_training', {}).get('precision', 0),
                report.get('co_training', {}).get('recall', 0),
                report.get('co_training', {}).get('f1_score', 0)
            ]
            
            fig = go.Figure()
            
            fig.add_trace(go.Scatterpolar(
                r=self_metrics + [self_metrics[0]],
                theta=categories + [categories[0]],
                fill='toself',
                name='Self-Training',
                line_color='#667eea',
                fillcolor='rgba(102, 126, 234, 0.3)'
            ))
            
            fig.add_trace(go.Scatterpolar(
                r=co_metrics + [co_metrics[0]],
                theta=categories + [categories[0]],
                fill='toself',
                name='Co-Training',
                line_color='#f093fb',
                fillcolor='rgba(240, 147, 251, 0.3)'
            ))
            
            fig.update_layout(
                title='Multi-Metric Comparison',
                polar=dict(
                    bgcolor='rgba(0,0,0,0)',
                    radialaxis=dict(
                        visible=True,
                        range=[0, 1],
                        gridcolor='rgba(255,255,255,0.2)'
                    ),
                    angularaxis=dict(gridcolor='rgba(255,255,255,0.2)')
                ),
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='white', family='Space Grotesk'),
                title_font=dict(size=18, family='Orbitron'),
                legend=dict(
                    bgcolor='rgba(0,0,0,0)',
                    font=dict(color='white')
                ),
                height=400
            )
            
            st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Key Insights
        st.markdown('<div class="section-header">💡 Key Insights</div>', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="glass-card">
            <div class="info-box">
                <strong>🎯 Self-Training Performance:</strong> Self-Training achieved the highest F1 score, 
                demonstrating its effectiveness in leveraging unlabeled data for air quality classification.
            </div>
            <div class="info-box">
                <strong>🤝 Co-Training Analysis:</strong> Co-Training uses two different feature views to 
                iteratively label data. While effective, it shows slightly lower performance on this dataset.
            </div>
            <div class="success-box">
                <strong>✅ Key Finding:</strong> Semi-supervised learning methods successfully utilize 
                unlabeled air quality data to improve classification accuracy with limited labeled samples.
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="warning-box">
            ⚠️ <strong>Report Not Found:</strong> Please run the semi_supervised_report notebook first.
        </div>
        """, unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# 🗺️ STATIONS PAGE
# ─────────────────────────────────────────────────────────────────────────────
elif page == "🗺️ Stations":
    st.markdown("""
    <h1 class="main-title">🗺️ Monitoring Stations</h1>
    <p class="sub-title">Beijing Air Quality Network</p>
    """, unsafe_allow_html=True)
    
    # Station Information
    stations = {
        'Aotizhongxin': {'lat': 39.9829, 'lon': 116.3974, 'type': 'Urban'},
        'Changping': {'lat': 40.2206, 'lon': 116.2310, 'type': 'Suburban'},
        'Dingling': {'lat': 40.2917, 'lon': 116.2203, 'type': 'Rural'},
        'Dongsi': {'lat': 39.9296, 'lon': 116.4171, 'type': 'Urban'},
        'Guanyuan': {'lat': 39.9294, 'lon': 116.3547, 'type': 'Urban'},
        'Gucheng': {'lat': 39.9142, 'lon': 116.1847, 'type': 'Industrial'},
        'Huairou': {'lat': 40.3283, 'lon': 116.6367, 'type': 'Rural'},
        'Nongzhanguan': {'lat': 39.9372, 'lon': 116.4619, 'type': 'Urban'},
        'Shunyi': {'lat': 40.1281, 'lon': 116.6550, 'type': 'Suburban'},
        'Tiantan': {'lat': 39.8867, 'lon': 116.4072, 'type': 'Urban'},
        'Wanliu': {'lat': 39.9875, 'lon': 116.3031, 'type': 'Urban'},
        'Wanshouxigong': {'lat': 39.8789, 'lon': 116.3522, 'type': 'Urban'}
    }
    
    st.markdown('<div class="section-header">📍 Station Locations</div>', unsafe_allow_html=True)
    
    # Create map dataframe
    map_df = pd.DataFrame([
        {'station': name, **info} 
        for name, info in stations.items()
    ])
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        
        # Create map
        fig = px.scatter_mapbox(
            map_df,
            lat='lat',
            lon='lon',
            hover_name='station',
            color='type',
            size_max=15,
            zoom=9,
            center={'lat': 40.0, 'lon': 116.4},
            mapbox_style='carto-darkmatter',
            title='Beijing Air Quality Monitoring Network'
        )
        
        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white', family='Space Grotesk'),
            title_font=dict(size=18, family='Orbitron'),
            height=500,
            margin=dict(l=0, r=0, t=50, b=0)
        )
        
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("""
        <h3 style="font-family: 'Orbitron'; color: white; font-size: 1.2rem; margin-bottom: 1rem;">
            📊 Station Statistics
        </h3>
        """, unsafe_allow_html=True)
        
        type_counts = map_df['type'].value_counts()
        
        for station_type, count in type_counts.items():
            icon = {'Urban': '🏙️', 'Suburban': '🏘️', 'Rural': '🌾', 'Industrial': '🏭'}.get(station_type, '📍')
            st.markdown(f"""
            <div style="display: flex; justify-content: space-between; padding: 0.8rem; 
                        background: rgba(255,255,255,0.05); border-radius: 10px; margin-bottom: 0.5rem;">
                <span style="color: rgba(255,255,255,0.8); font-family: 'Space Grotesk';">{icon} {station_type}</span>
                <span style="color: #667eea; font-family: 'Orbitron'; font-weight: 600;">{count}</span>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div style="margin-top: 1.5rem; padding: 1rem; background: linear-gradient(135deg, rgba(102, 126, 234, 0.2), rgba(118, 75, 162, 0.2)); 
                    border-radius: 15px; text-align: center;">
            <div style="font-family: 'Space Grotesk'; color: rgba(255,255,255,0.6); font-size: 0.9rem;">Total Stations</div>
            <div style="font-family: 'Orbitron'; color: white; font-size: 2.5rem; font-weight: 700;">{len(stations)}</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Station Details Table
    st.markdown('<div class="section-header">📋 Station Details</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    
    if 'cleaned' in data:
        df = data['cleaned']
        if 'station' in df.columns and 'PM2.5' in df.columns:
            station_stats = df.groupby('station')['PM2.5'].agg(['mean', 'max', 'min', 'std', 'count']).round(2)
            station_stats.columns = ['Avg PM2.5', 'Max', 'Min', 'Std Dev', 'Records']
            
            # Add station type
            station_stats['Type'] = station_stats.index.map(lambda x: stations.get(x, {}).get('type', 'Unknown'))
            
            # Display as styled dataframe
            st.dataframe(
                station_stats.style.background_gradient(subset=['Avg PM2.5'], cmap='RdYlGn_r'),
                use_container_width=True,
                height=450
            )
    
    st.markdown('</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# ℹ️ ABOUT PAGE
# ─────────────────────────────────────────────────────────────────────────────
elif page == "ℹ️ About":
    st.markdown("""
    <h1 class="main-title">ℹ️ About AIR GUARD</h1>
    <p class="sub-title">PM2.5 Forecasting & AQI Alert System</p>
    """, unsafe_allow_html=True)
    
    # Project Overview
    st.markdown('<div class="section-header">🎯 Project Overview</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="glass-card">
        <p style="font-family: 'Space Grotesk'; color: rgba(255,255,255,0.9); font-size: 1.1rem; line-height: 1.8;">
            <strong style="color: #667eea;">AIR GUARD</strong> is an advanced air quality monitoring and prediction system 
            that leverages <strong style="color: #764ba2;">Semi-Supervised Learning</strong> techniques to forecast PM2.5 
            concentrations and provide AQI (Air Quality Index) alerts.
        </p>
        <br>
        <p style="font-family: 'Space Grotesk'; color: rgba(255,255,255,0.9); font-size: 1.1rem; line-height: 1.8;">
            The project utilizes the <strong style="color: #f093fb;">Beijing Multi-Site Air Quality Dataset</strong> from UCI, 
            containing hourly readings from 12 monitoring stations across Beijing (2013-2017), totaling over 420,000 records.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Key Features
    st.markdown('<div class="section-header">✨ Key Features</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    features = [
        ("🔬", "Semi-Supervised Learning", "Self-Training & Co-Training algorithms for leveraging unlabeled data"),
        ("📊", "Multi-Station Analysis", "Comprehensive data from 12 Beijing monitoring stations"),
        ("📈", "Time Series Forecasting", "ARIMA models for PM2.5 trend prediction"),
        ("🎯", "AQI Classification", "6-level air quality classification system"),
        ("🗺️", "Spatial Visualization", "Interactive maps and station comparisons"),
        ("⚡", "Real-time Dashboard", "Modern Streamlit interface with live updates")
    ]
    
    for i, (icon, title, desc) in enumerate(features):
        col = [col1, col2, col3][i % 3]
        with col:
            st.markdown(f"""
            <div class="stat-card" style="min-height: 180px;">
                <div class="stat-icon">{icon}</div>
                <div style="font-family: 'Space Grotesk'; color: white; font-size: 1.1rem; font-weight: 600; margin: 0.5rem 0;">
                    {title}
                </div>
                <div style="font-family: 'Rajdhani'; color: rgba(255,255,255,0.7); font-size: 0.9rem;">
                    {desc}
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Technology Stack
    st.markdown('<div class="section-header">🛠️ Technology Stack</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="glass-card">
        <div style="display: flex; flex-wrap: wrap; gap: 1rem; justify-content: center;">
            <div class="nav-pill">🐍 Python 3.10+</div>
            <div class="nav-pill">📊 Pandas</div>
            <div class="nav-pill">🔢 NumPy</div>
            <div class="nav-pill">🤖 Scikit-Learn</div>
            <div class="nav-pill">📈 Plotly</div>
            <div class="nav-pill">🎨 Streamlit</div>
            <div class="nav-pill">📉 Statsmodels</div>
            <div class="nav-pill">🗃️ PyArrow</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Team Section
    st.markdown('<div class="section-header">👥 Project Team - Group 7</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    team = [
        ("👨‍💻", "Nguyễn Văn Tài", "Team Leader"),
        ("👩‍💻", "Member 2", "Data Engineer"),
        ("👨‍🔬", "Member 3", "ML Engineer")
    ]
    
    for col, (icon, name, role) in zip([col1, col2, col3], team):
        with col:
            st.markdown(f"""
            <div class="team-card">
                <div class="team-avatar">{icon}</div>
                <div class="team-name">{name}</div>
                <div class="team-role">{role}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # Dataset Info
    st.markdown('<div class="section-header">📚 Dataset Information</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="glass-card">
        <table class="styled-table">
            <thead>
                <tr>
                    <th>Attribute</th>
                    <th>Details</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>📂 Source</td>
                    <td>UCI Machine Learning Repository - Dataset #501</td>
                </tr>
                <tr>
                    <td>📊 Records</td>
                    <td>420,768 hourly observations</td>
                </tr>
                <tr>
                    <td>🗺️ Stations</td>
                    <td>12 monitoring stations across Beijing</td>
                </tr>
                <tr>
                    <td>📅 Period</td>
                    <td>March 2013 - February 2017</td>
                </tr>
                <tr>
                    <td>🔢 Features</td>
                    <td>PM2.5, PM10, SO2, NO2, CO, O3, Temperature, Pressure, etc.</td>
                </tr>
            </tbody>
        </table>
    </div>
    """, unsafe_allow_html=True)
    
    # GitHub Link
    st.markdown("""
    <div class="glass-card" style="text-align: center; padding: 2rem;">
        <div style="font-size: 3rem; margin-bottom: 1rem;">📦</div>
        <div style="font-family: 'Orbitron'; color: white; font-size: 1.3rem; margin-bottom: 1rem;">
            View on GitHub
        </div>
        <a href="https://github.com/NVT-Master/Nhom7_-Air_Guard" target="_blank" 
           style="display: inline-block; padding: 0.8rem 2rem; background: linear-gradient(135deg, #667eea, #764ba2);
                  color: white; text-decoration: none; border-radius: 50px; font-family: 'Space Grotesk';
                  transition: all 0.3s ease; box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);">
            🔗 NVT-Master/Nhom7_-Air_Guard
        </a>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# 📎 FOOTER
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="footer">
    <p>🌬️ <strong>AIR GUARD</strong> - PM2.5 Forecasting & AQI Alert System</p>
    <p style="font-size: 0.8rem; margin-top: 0.5rem;">
        Data Mining Mini Project | Group 7 | 2024
    </p>
    <p style="font-size: 0.7rem; margin-top: 0.3rem; color: rgba(255,255,255,0.3);">
        Built with ❤️ using Streamlit, Plotly & Semi-Supervised Learning
    </p>
</div>
""", unsafe_allow_html=True)
