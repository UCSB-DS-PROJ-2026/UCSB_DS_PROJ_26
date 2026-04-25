import streamlit as st

st.set_page_config(
    page_title="SB Housing Predictor",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)
 
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500;600&display=swap');
 
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}
 
/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0a2342 0%, #1a3a5c 100%);
}
[data-testid="stSidebar"] * {
    color: #e8f4fd !important;
}
[data-testid="stSidebarNav"] a {
    color: #b8d9f0 !important;
    font-size: 15px;
    font-weight: 400;
    border-radius: 8px;
    padding: 6px 12px;
    transition: background 0.2s;
}
[data-testid="stSidebarNav"] a:hover {
    background: rgba(255,255,255,0.1) !important;
}
[data-testid="stSidebarNav"] a[aria-current="page"] {
    background: rgba(96, 180, 255, 0.2) !important;
    color: #60b4ff !important;
    font-weight: 600;
}
 
/* Main background */
.main .block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1100px;
}
 
/* Hero section */
.hero-badge {
    display: inline-block;
    background: #e8f4fd;
    color: #1a5c96;
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    padding: 6px 14px;
    border-radius: 20px;
    margin-bottom: 20px;
}
.hero-title {
    font-family: 'DM Serif Display', serif;
    font-size: 56px;
    line-height: 1.1;
    color: #0a2342;
    margin: 0 0 18px 0;
}
.hero-title span {
    color: #2a7fd4;
    font-style: italic;
}
.hero-subtitle {
    font-size: 18px;
    color: #4a6580;
    line-height: 1.7;
    max-width: 560px;
    margin-bottom: 36px;
    font-weight: 300;
}
 
/* Stat cards */
.stat-row {
    display: flex;
    gap: 16px;
    margin: 40px 0;
    flex-wrap: wrap;
}
.stat-card {
    background: white;
    border: 1px solid #dbedf9;
    border-radius: 14px;
    padding: 22px 26px;
    flex: 1;
    min-width: 160px;
    box-shadow: 0 2px 12px rgba(42,127,212,0.07);
}
.stat-card .stat-num {
    font-family: 'DM Serif Display', serif;
    font-size: 36px;
    color: #0a2342;
    line-height: 1;
    margin-bottom: 6px;
}
.stat-card .stat-label {
    font-size: 13px;
    color: #6b8ba4;
    font-weight: 500;
    letter-spacing: 0.3px;
}
.stat-card .stat-accent {
    color: #2a7fd4;
}
 
/* Feature cards */
.feature-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 18px;
    margin: 10px 0 40px 0;
}
.feature-card {
    background: white;
    border: 1px solid #dbedf9;
    border-radius: 16px;
    padding: 28px 24px;
    transition: box-shadow 0.2s, transform 0.2s;
    cursor: pointer;
}
.feature-card:hover {
    box-shadow: 0 8px 30px rgba(42,127,212,0.12);
    transform: translateY(-2px);
}
.feature-icon {
    font-size: 28px;
    margin-bottom: 14px;
}
.feature-title {
    font-family: 'DM Serif Display', serif;
    font-size: 20px;
    color: #0a2342;
    margin: 0 0 8px 0;
}
.feature-desc {
    font-size: 14px;
    color: #6b8ba4;
    line-height: 1.6;
    margin: 0;
}
 
/* How it works */
.section-label {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #2a7fd4;
    margin-bottom: 10px;
}
.section-title {
    font-family: 'DM Serif Display', serif;
    font-size: 34px;
    color: #0a2342;
    margin: 0 0 10px 0;
}
 
.step-row {
    display: flex;
    gap: 0;
    margin: 28px 0 0 0;
    position: relative;
}
.step-item {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    padding-right: 24px;
}
.step-num {
    width: 38px;
    height: 38px;
    border-radius: 50%;
    background: #2a7fd4;
    color: white;
    font-weight: 700;
    font-size: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 14px;
    flex-shrink: 0;
}
.step-title {
    font-size: 15px;
    font-weight: 600;
    color: #0a2342;
    margin: 0 0 6px 0;
}
.step-desc {
    font-size: 13px;
    color: #6b8ba4;
    line-height: 1.6;
    margin: 0;
}
 
/* Footer note */
.footer-note {
    text-align: center;
    font-size: 13px;
    color: #9ab3c8;
    margin-top: 48px;
    padding-top: 24px;
    border-top: 1px solid #e8f0f8;
}
</style>
""", unsafe_allow_html=True)
 
# ── Hero ──────────────────────────────────────────────────────────────────────
col1, col2 = st.columns([1.1, 1])
 
with col1:
    st.markdown("""
    <div class="hero-badge">UCSB Data Science Club · 2026</div>
    <h1 class="hero-title">Santa Barbara<br><span>Housing</span><br>Intelligence</h1>
    <p class="hero-subtitle">
        Data-driven rent estimates and neighborhood insights built specifically for 
        UCSB students navigating the Isla Vista housing market.
    </p>
    """, unsafe_allow_html=True)
 
    c1, c2 = st.columns(2)
    with c1:
        if st.button("→ Predict My Rent", use_container_width=True, type="primary"):
            st.switch_page("pages/02_Rent_Predictor.py")
    with c2:
        if st.button("Explore the Market", use_container_width=True):
            st.switch_page("pages/03_Market_Explorer.py")
 
with col2:
    st.markdown("""
    <div class="stat-row">
        <div class="stat-card">
            <div class="stat-num"><span class="stat-accent">200+</span></div>
            <div class="stat-label">Listings Analyzed</div>
        </div>
        <div class="stat-card">
            <div class="stat-num"><span class="stat-accent">10</span></div>
            <div class="stat-label">Years of Data</div>
        </div>
    </div>
    <div class="stat-row" style="margin-top:0">
        <div class="stat-card">
            <div class="stat-num"><span class="stat-accent">IV</span></div>
            <div class="stat-label">Isla Vista Focus</div>
        </div>
        <div class="stat-card">
            <div class="stat-num"><span class="stat-accent">ML</span></div>
            <div class="stat-label">Powered Predictions</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
 
st.markdown("<br>", unsafe_allow_html=True)
 
# ── Feature Cards ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="feature-grid">
    <div class="feature-card">
        <div class="feature-icon">🏠</div>
        <p class="feature-title">Rent Predictor</p>
        <p class="feature-desc">Enter your preferences — bedrooms, distance from campus, school year — and get an instant ML-powered estimate.</p>
    </div>
    <div class="feature-card">
        <div class="feature-icon">📊</div>
        <p class="feature-title">Market Explorer</p>
        <p class="feature-desc">Browse real listings filtered by budget, location, and unit size. See how prices have shifted from 2016 to today.</p>
    </div>
    <div class="feature-card">
        <div class="feature-icon">📈</div>
        <p class="feature-title">Trend Analysis</p>
        <p class="feature-desc">Visualize 10 years of Santa Barbara rent trends broken down by housing type and number of bedrooms.</p>
    </div>
</div>
""", unsafe_allow_html=True)
 
# ── How it works ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="section-label">How it works</div>
<h2 class="section-title">From preferences to prediction</h2>
<div class="step-row">
    <div class="step-item">
        <div class="step-num">1</div>
        <p class="step-title">Set your preferences</p>
        <p class="step-desc">Choose bedrooms, bathrooms, distance from campus, and your target school year.</p>
    </div>
    <div class="step-item">
        <div class="step-num">2</div>
        <p class="step-title">Model runs instantly</p>
        <p class="step-desc">Our Ridge Regression model trained on Santa Barbara rental data returns a price estimate in milliseconds.</p>
    </div>
    <div class="step-item">
        <div class="step-num">3</div>
        <p class="step-title">Explore the market</p>
        <p class="step-desc">Cross-reference with real listings in the Market Explorer to validate and compare options.</p>
    </div>
    <div class="step-item">
        <div class="step-num">4</div>
        <p class="step-title">Make a decision</p>
        <p class="step-desc">Use trend charts and neighborhood data to confidently choose your next place to live.</p>
    </div>
</div>
""", unsafe_allow_html=True)
 
st.markdown("""
<p class="footer-note">Built by the UCSB Data Science Club · Data sourced from Santa Barbara County rental listings</p>
""", unsafe_allow_html=True)