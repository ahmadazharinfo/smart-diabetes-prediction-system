"""
Smart Diabetes Monitoring and Prediction System
University of Basrah — Computer Engineering Department
Authors: Ahmad Azhar Almansoor | Ibrahim Madian Fadhil
Supervisor: Asst. Dr. Sarah Aziz Hafidh | Academic Year: 2024-2025
"""

import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

st.set_page_config(
    page_title="DiabetesAI — Risk Assessment",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body { background:#0B1120 !important; }

[data-testid="stAppViewContainer"] { background:#0B1120 !important; font-family:'Inter',sans-serif !important; }
[data-testid="stHeader"]           { display:none !important; }
[data-testid="stSidebar"]          { display:none !important; }
[data-testid="stDecoration"]       { display:none !important; }
#MainMenu, footer, header          { visibility:hidden; }

/* THE KEY FIX — keep Streamlit's natural padding, just set it to what we want */
.block-container {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
    padding-left: 5% !important;
    padding-right: 5% !important;
    max-width: 100% !important;
}

div[data-testid="stVerticalBlock"] { gap:0 !important; }

/* ── NAVBAR ── */
.navbar {
    background: #0B1120;
    border-bottom: 1px solid rgba(255,255,255,0.07);
    margin-left: -5%;
    margin-right: -5%;
    margin-top: 0;
    margin-bottom: 0;
    padding: 0 5%;
    height: 70px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}
.nb-left   { display:flex; align-items:center; gap:12px; }
.nb-icon   { width:38px; height:38px; background:linear-gradient(135deg,#3B82F6,#06B6D4); border-radius:10px; display:flex; align-items:center; justify-content:center; font-size:1.1rem; }
.nb-name   { font-size:1.1rem; font-weight:800; color:#fff; letter-spacing:-.01em; font-family:'Inter',sans-serif; }
.nb-sub    { font-size:.62rem; color:rgba(255,255,255,.3); letter-spacing:.09em; text-transform:uppercase; }
.nb-right  { display:flex; gap:8px; }
.pill      { padding:4px 13px; border-radius:999px; font-size:.65rem; font-weight:700; letter-spacing:.05em; text-transform:uppercase; }
.pill-b    { background:rgba(59,130,246,.12); border:1px solid rgba(59,130,246,.28); color:#93C5FD; }
.pill-c    { background:rgba(6,182,212,.1);   border:1px solid rgba(6,182,212,.22);  color:#67E8F9; }

/* ── HERO ── */
.hero {
    background: #0B1120;
    padding: 52px 0 48px;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content:''; position:absolute; top:-100px; right:-5%;
    width:480px; height:480px;
    background:radial-gradient(circle, rgba(59,130,246,.1) 0%, transparent 65%);
    pointer-events:none;
}
.hero-tag {
    display:inline-flex; align-items:center; gap:8px;
    background:rgba(59,130,246,.1); border:1px solid rgba(59,130,246,.2);
    color:#93C5FD; padding:5px 16px; border-radius:999px;
    font-size:.67rem; font-weight:700; letter-spacing:.1em; text-transform:uppercase;
    margin-bottom:20px;
}
.hero-h1   { font-size:2.75rem; font-weight:800; color:#fff; line-height:1.1; letter-spacing:-.025em; margin-bottom:16px; font-family:'Inter',sans-serif; }
.hero-h1 .ac { color:#38BDF8; }
.hero-p    { font-size:.92rem; color:rgba(255,255,255,.42); line-height:1.8; max-width:520px; font-weight:400; }

/* ── STATS ── */
.stats-grid {
    display:grid; grid-template-columns:repeat(4,1fr);
    gap:1px; background:rgba(255,255,255,.06);
    border:1px solid rgba(255,255,255,.07); border-radius:16px;
    overflow:hidden; margin: 0 0 44px;
}
.stat-cell   { background:#0D1526; padding:18px 22px; position:relative; }
.stat-cell::before { content:''; position:absolute; top:0; left:0; right:0; height:2px; }
.s1::before  { background:#3B82F6; } .s2::before { background:#8B5CF6; }
.s3::before  { background:#06B6D4; } .s4::before { background:#10B981; }
.stat-n      { font-size:1.6rem; font-weight:800; color:#fff; line-height:1; margin-bottom:5px; font-family:'Inter',sans-serif; }
.stat-l      { font-size:.63rem; color:rgba(255,255,255,.3); font-weight:700; text-transform:uppercase; letter-spacing:.09em; }

/* ── SECTION HEADERS ── */
.sec-head  { margin-bottom:22px; }
.sec-badge { display:inline-flex; align-items:center; gap:7px; background:rgba(59,130,246,.1); border:1px solid rgba(59,130,246,.18); color:#93C5FD; padding:4px 13px; border-radius:999px; font-size:.63rem; font-weight:700; letter-spacing:.1em; text-transform:uppercase; margin-bottom:9px; }
.sec-title { font-size:1.25rem; font-weight:800; color:#fff; letter-spacing:-.01em; font-family:'Inter',sans-serif; }
.sec-desc  { font-size:.82rem; color:rgba(255,255,255,.35); margin-top:5px; line-height:1.65; }
.hdiv      { height:1px; background:rgba(255,255,255,.06); margin:36px 0; }

/* ── FORM CARDS ── */
.fcard {
    background: rgba(255,255,255,.03);
    border: 1px solid rgba(255,255,255,.08);
    border-radius: 16px;
    overflow: hidden;
    height: 100%;
}
.fcard-head {
    padding:14px 18px;
    border-bottom:1px solid rgba(255,255,255,.06);
    display:flex; align-items:center; gap:10px;
    background:rgba(255,255,255,.02);
}
.fcard-icon  { width:30px; height:30px; border-radius:8px; display:flex; align-items:center; justify-content:center; font-size:.9rem; flex-shrink:0; }
.fi-b        { background:rgba(59,130,246,.18); }
.fi-r        { background:rgba(239,68,68,.15); }
.fi-g        { background:rgba(16,185,129,.14); }
.fcard-title { font-size:.72rem; font-weight:800; color:#fff; letter-spacing:.05em; text-transform:uppercase; }
.fcard-cnt   { margin-left:auto; font-size:.62rem; color:rgba(255,255,255,.22); font-weight:600; background:rgba(255,255,255,.04); padding:2px 9px; border-radius:999px; }
.fcard-body  { padding:16px 18px; }


/* ── WIDGET OVERRIDES ── */
div[data-testid="stSelectbox"] > label,
div[data-testid="stSlider"] > label {
    font-size:.71rem !important; font-weight:700 !important;
    color:rgba(255,255,255,.4) !important;
    text-transform:uppercase !important; letter-spacing:.07em !important;
    font-family:'Inter',sans-serif !important;
    margin-top:16px !important;
}
div[data-testid="stSelectbox"] > div > div {
    background:rgba(255,255,255,.05) !important;
    border:1px solid rgba(255,255,255,.1) !important;
    border-radius:10px !important;
    color:#fff !important; font-size:.85rem !important;
    font-family:'Inter',sans-serif !important;
}
div[data-testid="stButton"] > button {
    background:linear-gradient(135deg,#3B82F6,#06B6D4) !important;
    color:#fff !important; border:none !important;
    border-radius:12px !important; padding:14px !important;
    font-size:.92rem !important; font-weight:700 !important;
    font-family:'Inter',sans-serif !important;
    width:100% !important; letter-spacing:.02em !important;
    box-shadow:0 4px 18px rgba(59,130,246,.35) !important;
}

/* ── RESULT CARDS ── */
.rc-high {
    background:linear-gradient(145deg,#110808,#1C0B0B);
    border:1px solid rgba(239,68,68,.2); border-top:3px solid #EF4444;
    border-radius:18px; padding:28px; position:relative; overflow:hidden;
}
.rc-high::after { content:''; position:absolute; top:0; right:0; width:220px; height:220px; background:radial-gradient(circle,rgba(239,68,68,.08) 0%,transparent 65%); pointer-events:none; }
.rc-low {
    background:linear-gradient(145deg,#070D19,#0B1221);
    border:1px solid rgba(6,182,212,.16); border-top:3px solid #06B6D4;
    border-radius:18px; padding:28px; position:relative; overflow:hidden;
}
.rc-low::after { content:''; position:absolute; top:0; right:0; width:220px; height:220px; background:radial-gradient(circle,rgba(6,182,212,.07) 0%,transparent 65%); pointer-events:none; }
.rc-hdr   { display:flex; align-items:center; gap:14px; margin-bottom:22px; position:relative; z-index:1; }
.rc-em    { font-size:2.4rem; line-height:1; }
.rc-tag   { font-size:.6rem; font-weight:700; letter-spacing:.14em; text-transform:uppercase; opacity:.45; color:#fff; margin-bottom:3px; }
.rv-h     { font-size:1.6rem; font-weight:800; color:#FCA5A5; line-height:1.1; font-family:'Inter',sans-serif; }
.rv-l     { font-size:1.6rem; font-weight:800; color:#67E8F9; line-height:1.1; font-family:'Inter',sans-serif; }
.prob-row { display:flex; align-items:baseline; gap:5px; margin-bottom:4px; position:relative; z-index:1; }
.prob-big { font-size:4rem; font-weight:800; color:#fff; line-height:1; font-family:'Inter',sans-serif; }
.prob-u   { font-size:1.1rem; color:rgba(255,255,255,.38); font-weight:600; }
.prob-cap { font-size:.72rem; color:rgba(255,255,255,.3); margin-bottom:20px; position:relative; z-index:1; }
.bar-area { position:relative; z-index:1; }
.bpin-lbl { font-size:.58rem; color:rgba(255,255,255,.35); font-weight:600; letter-spacing:.05em; margin-bottom:4px; }
.btrack   { height:8px; background:rgba(255,255,255,.07); border-radius:999px; position:relative; overflow:visible; }
.bfill-h  { height:100%; border-radius:999px; background:linear-gradient(90deg,#EF4444,#FF6B6B); box-shadow:0 0 10px rgba(239,68,68,.4); }
.bfill-l  { height:100%; border-radius:999px; background:linear-gradient(90deg,#3B82F6,#06B6D4); box-shadow:0 0 10px rgba(59,130,246,.4); }
.bpin     { position:absolute; top:-7px; left:53%; width:2px; height:22px; background:rgba(255,255,255,.38); border-radius:1px; }
.baxis    { display:flex; justify-content:space-between; font-size:.58rem; color:rgba(255,255,255,.2); margin-top:6px; font-weight:600; }
.mgrid    { display:grid; grid-template-columns:repeat(4,1fr); gap:8px; margin-top:20px; position:relative; z-index:1; }
.mcell    { background:rgba(255,255,255,.04); border:1px solid rgba(255,255,255,.07); border-radius:10px; padding:12px 8px; text-align:center; }
.mcell-l  { font-size:.57rem; color:rgba(255,255,255,.28); font-weight:700; text-transform:uppercase; letter-spacing:.08em; margin-bottom:4px; }
.mcell-v  { font-size:1rem; font-weight:800; color:#fff; font-family:'Inter',sans-serif; }

/* ── RISK PANEL ── */
.rp        { background:rgba(255,255,255,.03); border:1px solid rgba(255,255,255,.07); border-radius:15px; overflow:hidden; }
.rp-h      { padding:12px 18px; border-bottom:1px solid rgba(255,255,255,.05); background:rgba(255,255,255,.02); font-size:.68rem; font-weight:800; color:rgba(255,255,255,.45); letter-spacing:.1em; text-transform:uppercase; display:flex; align-items:center; gap:8px; }
.rp-row    { display:flex; align-items:flex-start; gap:10px; padding:11px 18px; border-bottom:1px solid rgba(255,255,255,.04); }
.rp-row:last-child { border-bottom:none; }
.dot-r     { width:7px; height:7px; border-radius:50%; background:#EF4444; flex-shrink:0; margin-top:5px; box-shadow:0 0 5px rgba(239,68,68,.5); }
.dot-y     { width:7px; height:7px; border-radius:50%; background:#F59E0B; flex-shrink:0; margin-top:5px; box-shadow:0 0 5px rgba(245,158,11,.4); }
.rp-txt    { font-size:.8rem; color:rgba(255,255,255,.48); line-height:1.55; }
.rp-txt strong { color:rgba(255,255,255,.8); font-weight:700; }
.rp-empty  { padding:20px; text-align:center; font-size:.8rem; color:rgba(255,255,255,.2); }

/* ── RECOMMENDATION ── */
.rec-h { background:rgba(239,68,68,.06); border:1px solid rgba(239,68,68,.16); border-left:3px solid #EF4444; border-radius:12px; padding:15px 17px; margin-top:12px; }
.rec-l { background:rgba(16,185,129,.05); border:1px solid rgba(16,185,129,.15); border-left:3px solid #10B981; border-radius:12px; padding:15px 17px; margin-top:12px; }
.rec-lbl-h { font-size:.6rem; font-weight:800; letter-spacing:.12em; text-transform:uppercase; color:#FCA5A5; margin-bottom:6px; }
.rec-lbl-l { font-size:.6rem; font-weight:800; letter-spacing:.12em; text-transform:uppercase; color:#6EE7B7; margin-bottom:6px; }
.rec-body  { font-size:.8rem; color:rgba(255,255,255,.48); line-height:1.7; }
.rec-body strong { color:rgba(255,255,255,.76); }
.discl     { background:rgba(245,158,11,.04); border:1px solid rgba(245,158,11,.12); border-radius:11px; padding:12px 16px; margin-top:12px; font-size:.71rem; color:rgba(255,255,255,.28); line-height:1.65; display:flex; gap:8px; }

/* ── FOOTER ── */
.ftr       { background:rgba(255,255,255,.02); border-top:1px solid rgba(255,255,255,.06); margin:60px -5% 0; padding:24px 5%; display:flex; justify-content:space-between; align-items:center; }
.ftr-l     { font-size:.72rem; color:rgba(255,255,255,.2); line-height:1.85; }
.ftr-l strong { color:rgba(255,255,255,.4); }
.ftr-r     { font-size:.66rem; color:rgba(255,255,255,.15); text-align:right; line-height:1.85; }
</style>
""", unsafe_allow_html=True)


@st.cache_resource
def load_bundle():
    path = r"C:\Users\Ahmed A. Almansour\Documents\Final_Project _Submission\Graduation_Project_Files\Streamlit_App\full_pipeline_bundle.pkl"
    if not os.path.exists(path):
        return None
    with open(path, "rb") as f:
        return pickle.load(f)

def engineer_features(df_in):
    d = df_in.copy()
    d["CompositeRiskScore"]  = d["HighBP"]+d["HighChol"]+d["Smoker"]+d["Stroke"]+d["HeartDiseaseorAttack"]+d["DiffWalk"]
    d["BMI_Underweight"]     = (d["BMI"]<18.5).astype(int)
    d["BMI_Normal"]          = ((d["BMI"]>=18.5)&(d["BMI"]<25)).astype(int)
    d["BMI_Overweight"]      = ((d["BMI"]>=25)&(d["BMI"]<30)).astype(int)
    d["BMI_Obese"]           = (d["BMI"]>=30).astype(int)
    d["BMI_SevereObese"]     = (d["BMI"]>=35).astype(int)
    d["BMI_x_PhysActivity"]  = d["BMI"]*d["PhysActivity"]
    d["Age_x_BMI"]           = d["Age"]*d["BMI"]
    d["GenHlth_x_BMI"]       = d["GenHlth"]*d["BMI"]
    d["CardioRisk"]          = d["HighBP"]*d["HighChol"]+d["HeartDiseaseorAttack"]+d["Stroke"]
    d["LifestyleScore"]      = d["PhysActivity"]+d["Fruits"]+d["Veggies"]-d["Smoker"]-d["HvyAlcoholConsump"]
    d["HealthAccess"]        = d["AnyHealthcare"]-d["NoDocbcCost"]
    d["HealthBurden"]        = (d["MentHlth"]+d["PhysHlth"])/60.0
    d["GenHlth_Sq"]          = d["GenHlth"]**2
    d["BMI_Sq"]              = d["BMI"]**2
    d["Age_Sq"]              = d["Age"]**2
    d["SocioEconomic"]       = d["Income"]*d["Education"]
    d["AgeGroup_Senior"]     = (d["Age"]>=9).astype(int)
    d["AgeGroup_Middle"]     = ((d["Age"]>=5)&(d["Age"]<9)).astype(int)
    d["AgeGroup_Young"]      = (d["Age"]<5).astype(int)
    d["HighRiskFlag"]        = ((d["HighBP"]==1)&(d["HighChol"]==1)&(d["BMI_Obese"]==1)).astype(int)
    d["AlcSmoke"]            = d["HvyAlcoholConsump"]+d["Smoker"]
    d["UncheckedRisk"]       = ((d["CholCheck"]==0)&(d["CompositeRiskScore"]>2)).astype(int)
    d["MentalPhysRatio"]     = d["MentHlth"]/(d["PhysHlth"]+1)
    return d

def run_predict(bundle, inp, threshold=0.53):
    df   = pd.DataFrame([inp])
    dfe  = engineer_features(df)
    X    = dfe[bundle["features_used"]]
    Xsc  = bundle["scaler"].transform(X)
    prob = bundle["model"].predict_proba(Xsc)[:,1][0]
    return prob, int(prob >= threshold)


# ── NAVBAR ────────────────────────────────────────────────────────
st.markdown("""<div class="navbar">
  <div class="nb-left">
    <div class="nb-icon">🩺</div>
    <div><div class="nb-name">DiabetesAI</div><div class="nb-sub">Risk Assessment System</div></div>
  </div>
  <div class="nb-right">
    <div class="pill pill-b">LightGBM</div>
    <div class="pill pill-c">BRFSS 2015</div>
  </div>
</div>""", unsafe_allow_html=True)

# ── HERO ─────────────────────────────────────────────────────────
st.markdown("""<div class="hero">
  <div class="hero-tag">⚕ Clinical Decision Support Tool</div>
  <div class="hero-h1">Early Diabetes<br><span class="ac">Risk Prediction</span></div>
  <div class="hero-p">A machine learning pipeline trained on 253,680 BRFSS behavioral health records — engineered to achieve a minimum clinical sensitivity of 90.6%, identifying at-risk individuals before any laboratory testing is required.</div>
</div>""", unsafe_allow_html=True)

# ── STATS ─────────────────────────────────────────────────────────
st.markdown("""<div class="stats-grid">
  <div class="stat-cell s1"><div class="stat-n">90.64%</div><div class="stat-l">Clinical Recall</div></div>
  <div class="stat-cell s2"><div class="stat-n">0.8186</div><div class="stat-l">ROC-AUC Score</div></div>
  <div class="stat-cell s3"><div class="stat-n">0.4447</div><div class="stat-l">PR-AUC Score</div></div>
  <div class="stat-cell s4"><div class="stat-n">253,680</div><div class="stat-l">Training Records</div></div>
</div>""", unsafe_allow_html=True)

# ── LOAD ─────────────────────────────────────────────────────────
bundle = load_bundle()
if bundle is None:
    st.error("⚠️ Bundle not found. Place full_pipeline_bundle.pkl in the same folder as app.py.")
    st.stop()

# ── SECTION 1 HEADER ─────────────────────────────────────────────
st.markdown("""<div class="sec-head">
  <div class="sec-badge">📋 Patient Information</div>
  <div class="sec-title">Complete the Assessment Form</div>
  <div class="sec-desc">Fill all 21 fields below. No laboratory tests required — uses self-reported behavioral and demographic data only.</div>
</div>""", unsafe_allow_html=True)

# ── FORM COLUMNS ─────────────────────────────────────────────────
c1, c2, c3 = st.columns(3, gap="medium")

with c1:
    st.markdown('<div class="fcard"><div class="fcard-head"><div class="fcard-icon fi-b">📏</div><div class="fcard-title">Demographics & Physical</div><div class="fcard-cnt">5 Fields</div></div><div class="fcard-body">', unsafe_allow_html=True)
    Age       = st.selectbox("Age Group", list(range(1,14)), format_func=lambda x:{1:"18–24",2:"25–29",3:"30–34",4:"35–39",5:"40–44",6:"45–49",7:"50–54",8:"55–59",9:"60–64",10:"65–69",11:"70–74",12:"75–79",13:"80 or older"}[x])
    Sex       = st.selectbox("Biological Sex", [0,1], format_func=lambda x:"Female" if x==0 else "Male")
    BMI       = st.slider("Body Mass Index (BMI)", 10, 98, 27, help="Normal 18.5–24.9 | Overweight 25–29.9 | Obese ≥30")
    Education = st.selectbox("Education Level", list(range(1,7)), format_func=lambda x:{1:"Never attended school",2:"Elementary",3:"Some high school",4:"High school graduate",5:"Some college",6:"College graduate"}[x])
    Income    = st.selectbox("Annual Household Income", list(range(1,9)), format_func=lambda x:{1:"Less than $10,000",2:"$10,000–$14,999",3:"$15,000–$19,999",4:"$20,000–$24,999",5:"$25,000–$34,999",6:"$35,000–$49,999",7:"$50,000–$74,999",8:"$75,000 or more"}[x])
    st.markdown("</div></div>", unsafe_allow_html=True)

with c2:
    st.markdown('<div class="fcard"><div class="fcard-head"><div class="fcard-icon fi-r">💉</div><div class="fcard-title">Health Conditions</div><div class="fcard-cnt">7 Fields</div></div><div class="fcard-body">', unsafe_allow_html=True)
    HighBP               = st.selectbox("High Blood Pressure",  [0,1], format_func=lambda x:"No" if x==0 else "Yes")
    HighChol             = st.selectbox("High Cholesterol",     [0,1], format_func=lambda x:"No" if x==0 else "Yes")
    CholCheck            = st.selectbox("Cholesterol Check (Last 5 Years)", [0,1], format_func=lambda x:"No" if x==0 else "Yes")
    Stroke               = st.selectbox("History of Stroke",    [0,1], format_func=lambda x:"No" if x==0 else "Yes")
    HeartDiseaseorAttack = st.selectbox("Heart Disease or Attack", [0,1], format_func=lambda x:"No" if x==0 else "Yes")
    DiffWalk             = st.selectbox("Difficulty Walking / Climbing Stairs", [0,1], format_func=lambda x:"No" if x==0 else "Yes")
    GenHlth              = st.selectbox("General Health Self-Rating", list(range(1,6)), format_func=lambda x:{1:"Excellent",2:"Very Good",3:"Good",4:"Fair",5:"Poor"}[x])
    st.markdown("</div></div>", unsafe_allow_html=True)

with c3:
    st.markdown('<div class="fcard"><div class="fcard-head"><div class="fcard-icon fi-g">🌿</div><div class="fcard-title">Lifestyle & Healthcare</div><div class="fcard-cnt">9 Fields</div></div><div class="fcard-body">', unsafe_allow_html=True)
    PhysActivity      = st.selectbox("Physical Activity (Last 30 Days)", [0,1], format_func=lambda x:"No" if x==0 else "Yes", help="Any activity outside regular job in the past 30 days?")
    Fruits            = st.selectbox("Daily Fruit Consumption",     [0,1], format_func=lambda x:"No" if x==0 else "Yes")
    Veggies           = st.selectbox("Daily Vegetable Consumption", [0,1], format_func=lambda x:"No" if x==0 else "Yes")
    HvyAlcoholConsump = st.selectbox("Heavy Alcohol Consumption",   [0,1], format_func=lambda x:"No" if x==0 else "Yes", help="Men >14 drinks/week | Women >7 drinks/week")
    Smoker            = st.selectbox("Smoker (≥100 Cigarettes Lifetime)", [0,1], format_func=lambda x:"No" if x==0 else "Yes")
    AnyHealthcare     = st.selectbox("Health Insurance Coverage",   [0,1], format_func=lambda x:"No" if x==0 else "Yes")
    NoDocbcCost       = st.selectbox("Skipped Doctor Due to Cost",  [0,1], format_func=lambda x:"No" if x==0 else "Yes")
    MentHlth          = st.slider("Poor Mental Health Days (Last 30)", 0, 30, 0)
    PhysHlth          = st.slider("Poor Physical Health Days (Last 30)", 0, 30, 0)
    st.markdown("</div></div>", unsafe_allow_html=True)

# ── BUTTON ───────────────────────────────────────────────────────
st.markdown('<div class="hdiv"></div>', unsafe_allow_html=True)
st.markdown("""<div class="sec-head">
  <div class="sec-badge">🔍 Run Assessment</div>
  <div class="sec-title">Assess Diabetes Risk</div>
  <div class="sec-desc">All fields complete? Click the button to run the LightGBM inference pipeline.</div>
</div>""", unsafe_allow_html=True)

_, bc, _ = st.columns([1,2,1])
with bc:
    predict_btn = st.button("🔍  Assess Diabetes Risk Now", use_container_width=True, type="primary")

# ── RESULTS ──────────────────────────────────────────────────────
if predict_btn:
    inp = {
        "HighBP":HighBP,"HighChol":HighChol,"CholCheck":CholCheck,"BMI":float(BMI),
        "Smoker":Smoker,"Stroke":Stroke,"HeartDiseaseorAttack":HeartDiseaseorAttack,
        "PhysActivity":PhysActivity,"Fruits":Fruits,"Veggies":Veggies,
        "HvyAlcoholConsump":HvyAlcoholConsump,"AnyHealthcare":AnyHealthcare,
        "NoDocbcCost":NoDocbcCost,"GenHlth":float(GenHlth),"MentHlth":float(MentHlth),
        "PhysHlth":float(PhysHlth),"Sex":Sex,"Age":float(Age),
        "Education":float(Education),"Income":float(Income),"DiffWalk":DiffWalk
    }
    with st.spinner("Running LightGBM inference..."):
        prob, pred = run_predict(bundle, inp, 0.53)

    pct = prob * 100
    bar = min(int(pct), 100)

    st.markdown('<div class="hdiv"></div>', unsafe_allow_html=True)
    st.markdown("""<div class="sec-head">
      <div class="sec-badge">📊 Assessment Result</div>
      <div class="sec-title">Risk Prediction Output</div>
      <div class="sec-desc">Review the model prediction, probability score, identified risk factors, and clinical recommendation below.</div>
    </div>""", unsafe_allow_html=True)

    rc, dc = st.columns([1.15, 0.85], gap="large")

    with rc:
        if pred == 1:
            cc,bc2,em = "rc-high","bfill-h","⚠️"
            vtxt,vcls = "HIGH RISK DETECTED","rv-h"
        else:
            cc,bc2,em = "rc-low","bfill-l","✅"
            vtxt,vcls = "LOW RISK","rv-l"

        st.markdown(f"""<div class="{cc}">
  <div class="rc-hdr">
    <div class="rc-em">{em}</div>
    <div><div class="rc-tag">Clinical Assessment</div><div class="{vcls}">{vtxt}</div></div>
  </div>
  <div class="prob-row"><div class="prob-big">{pct:.1f}</div><div class="prob-u">%</div></div>
  <div class="prob-cap">Predicted probability of diabetes or prediabetes</div>
  <div class="bar-area">
    <div class="bpin-lbl">Decision threshold at 53%</div>
    <div class="btrack"><div class="{bc2}" style="width:{bar}%;"></div><div class="bpin"></div></div>
    <div class="baxis"><span>0%</span><span>100%</span></div>
  </div>
  <div class="mgrid">
    <div class="mcell"><div class="mcell-l">Recall</div><div class="mcell-v">90.6%</div></div>
    <div class="mcell"><div class="mcell-l">ROC-AUC</div><div class="mcell-v">0.8186</div></div>
    <div class="mcell"><div class="mcell-l">PR-AUC</div><div class="mcell-v">0.4447</div></div>
    <div class="mcell"><div class="mcell-l">MCC</div><div class="mcell-v">0.3114</div></div>
  </div>
</div>""", unsafe_allow_html=True)

    with dc:
        rh, rm = [], []
        if BMI>=30:              rh.append(f"BMI {BMI} — <strong>Obese category</strong> (WHO ≥ 30)")
        elif BMI>=25:            rm.append(f"BMI {BMI} — <strong>Overweight category</strong> (25–29.9)")
        if HighBP==1:            rh.append("<strong>High blood pressure</strong> — primary T2DM risk factor")
        if HighChol==1:          rh.append("<strong>High cholesterol</strong> — linked to metabolic syndrome")
        if HeartDiseaseorAttack==1: rh.append("<strong>Heart disease history</strong> — elevated cardio-metabolic risk")
        if Stroke==1:            rh.append("<strong>Stroke history</strong> — associated with insulin resistance")
        if GenHlth>=4:           rm.append(f"Self-rated health: <strong>{'Fair' if GenHlth==4 else 'Poor'}</strong> — strong behavioral predictor")
        if PhysActivity==0:      rm.append("<strong>Physical inactivity</strong> — increases insulin resistance")
        if Smoker==1:            rm.append("<strong>Smoking history</strong> — associated with diabetes risk")
        if Age>=9:               rm.append("<strong>Age group 60+</strong> — significantly elevated T2DM prevalence")
        if CholCheck==0:         rm.append("<strong>No cholesterol check</strong> — undetected dyslipidemia possible")
        if MentHlth>14:          rm.append(f"<strong>{MentHlth} poor mental health days</strong> — stress-related metabolic risk")

        rows  = "".join(f'<div class="rp-row"><div class="dot-r"></div><div class="rp-txt">{r}</div></div>' for r in rh)
        rows += "".join(f'<div class="rp-row"><div class="dot-y"></div><div class="rp-txt">{r}</div></div>' for r in rm)
        if not rows:
            rows = '<div class="rp-empty">No significant individual risk factors detected.</div>'

        st.markdown(f'<div class="rp"><div class="rp-h">🔎 &nbsp; Key Risk Factors Identified</div>{rows}</div>', unsafe_allow_html=True)

        if pred==1:
            st.markdown('<div class="rec-h"><div class="rec-lbl-h">Clinical Recommendation</div><div class="rec-body">This assessment indicates <strong>elevated diabetes risk</strong>. Consult a healthcare provider for confirmatory laboratory testing — specifically fasting plasma glucose and HbA1c. Early lifestyle intervention can substantially reduce progression to Type 2 diabetes.</div></div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="rec-l"><div class="rec-lbl-l">Clinical Recommendation</div><div class="rec-body">This assessment indicates <strong>low current diabetes risk</strong>. Maintaining healthy weight, regular physical activity, and a balanced diet remain the most effective preventive measures. Routine periodic screening is still advised.</div></div>', unsafe_allow_html=True)

        st.markdown('<div class="discl"><span>⚠️</span><span><strong>Disclaimer:</strong> For clinical decision support only. Does not constitute a medical diagnosis. All high-risk results must be confirmed by a licensed healthcare professional through standard diagnostic testing.</span></div>', unsafe_allow_html=True)

# ── FOOTER ───────────────────────────────────────────────────────
st.markdown("""<div class="ftr">
  <div class="ftr-l"><strong>Smart Diabetes Monitoring and Prediction System</strong><br>University of Basrah — Computer Engineering Department<br>Ahmad Azhar Almansoor &nbsp;|&nbsp; Ibrahim Madian Fadhil</div>
  <div class="ftr-r">Supervisor: Asst. Dr. Sarah Aziz Hafidh<br>Academic Year 2024–2025<br>Dataset: BRFSS 2015 &nbsp;·&nbsp; Threshold: 0.53</div>
</div>""", unsafe_allow_html=True)