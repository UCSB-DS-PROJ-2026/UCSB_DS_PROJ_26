import streamlit as st
import pandas as pd
from numpy.random import default_rng as rng
import pydeck as pdk

st.set_page_config(
    page_title="About · SB Housing",
    page_icon="🏠",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500;600&display=swap');

html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0a2342 0%, #1a3a5c 100%);
}
[data-testid="stSidebar"] * { color: #e8f4fd !important; }
[data-testid="stSidebarNav"] a {
    color: #b8d9f0 !important; font-size: 15px; font-weight: 400;
    border-radius: 8px; padding: 6px 12px;
}
[data-testid="stSidebarNav"] a[aria-current="page"] {
    background: rgba(96,180,255,0.2) !important;
    color: #60b4ff !important; font-weight: 600;
}
.main .block-container { padding-top: 2rem; max-width: 900px; }

.page-label {
    font-size: 11px; font-weight: 700; letter-spacing: 2px;
    text-transform: uppercase; color: #2a7fd4; margin-bottom: 6px;
}
.page-title {
    font-family: 'DM Serif Display', serif;
    font-size: 42px; color: #0a2342; margin: 0 0 16px 0; line-height: 1.1;
}
.body-text {
    font-size: 16px; color: #4a6580; line-height: 1.8; font-weight: 300;
    max-width: 680px;
}

.divider { border: none; border-top: 1px solid #dbedf9; margin: 36px 0; }

.section-title {
    font-family: 'DM Serif Display', serif;
    font-size: 28px; color: #0a2342; margin: 0 0 18px 0;
}

/* Team cards */
.team-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 16px;
    margin-bottom: 36px;
}
.team-card {
    background: white;
    border: 1px solid #dbedf9;
    border-radius: 14px;
    padding: 22px 18px;
    text-align: center;
}
.team-avatar {
    width: 52px; height: 52px; border-radius: 50%;
    background: #e8f4fd;
    color: #2a7fd4;
    font-weight: 600; font-size: 18px;
    display: flex; align-items: center; justify-content: center;
    margin: 0 auto 12px auto;
}
.team-name {
    font-weight: 600; font-size: 15px; color: #0a2342; margin: 0 0 4px 0;
}
.team-role {
    font-size: 12px; color: #6b8ba4;
}

/* Tech stack pills */
.tech-row {
    display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 36px;
}
.tech-pill {
    background: #e8f4fd;
    color: #1a5c96;
    font-size: 13px; font-weight: 500;
    padding: 7px 16px; border-radius: 20px;
}

/* Data source cards */
.source-card {
    background: white;
    border: 1px solid #dbedf9;
    border-radius: 14px;
    padding: 20px 22px;
    margin-bottom: 12px;
    display: flex; align-items: center; gap: 16px;
}
.source-icon {
    font-size: 24px; flex-shrink: 0;
}
.source-title {
    font-weight: 600; font-size: 15px; color: #0a2342; margin: 0 0 4px 0;
}
.source-desc {
    font-size: 13px; color: #6b8ba4; margin: 0;
}

.banner {
    background: linear-gradient(135deg, #0a2342 0%, #1a5c96 100%);
    border-radius: 16px; padding: 32px 36px; margin-bottom: 8px;
    display: flex; align-items: center; gap: 24px;
}
.banner-text { color: white; }
.banner-text h3 {
    font-family: 'DM Serif Display', serif;
    font-size: 26px; color: white; margin: 0 0 8px 0;
}
.banner-text p {
    color: #7ec8f5; font-size: 14px; margin: 0; font-weight: 300;
}
</style>
""", unsafe_allow_html=True)

# ── Load data ─────────────────────────────────────
me_df = pd.read_csv("data/combined_data_me.csv")

# ── Layout ────────────────────────────────────────────────────────────────────
left_col, right_col = st.columns([1, 1], gap="large")
with left_col:
    # ── Intro ─────────────────────────────────────────────────────────────────────
    st.markdown("""
    <div class="page-label">About this project</div>
    <h1 class="page-title">Built for UCSB students,<br>by UCSB students</h1>
    <p class="body-text">
        Santa Barbara is one of the most expensive rental markets in California.
        This tool was built to give UCSB students a transparent, data-driven 
        way to understand what they should expect to pay — and to spot a good 
        deal when they see one.
    </p>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)
    # ── The model ─────────────────────────────────────────────────────────────────
    st.markdown("""
    <h2 class="section-title">How the model works</h2>
    <p class="body-text">
        The Rent Predictor uses an <strong>Ridge regression model</strong> trained on scraped 
        Santa Barbara rental listings. Features include number of bedrooms and bathrooms, 
        distance from UCSB campus, housing type, and year. 
        The model was validated using cross-validation and evaluated on held-out test data.
    </p>
    <br>
    """, unsafe_allow_html=True)

    # Tech stack
    st.markdown('<h2 class="section-title">Tech stack</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="tech-row">
        <span class="tech-pill">Python</span>
        <span class="tech-pill">Streamlit</span>
        <span class="tech-pill">Ridge Regression</span>
                <span class="tech-pill">Altair</span>
        <span class="tech-pill">scikit-learn</span>
        <span class="tech-pill">Pandas</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)


with right_col:
    # ── Isla Vista/Santa Barbara Map ──────────────────────────────────────────
    import folium
    from streamlit_folium import st_folium

    m = folium.Map(
        location=[34.432032, -119.84456],
        zoom_start=13,
        tiles="CartoDB positron",
    )

    map_df = me_df[["Latitude", "Longitude"]].dropna()

    for _, row in map_df.iterrows():
        folium.CircleMarker(
            location=[row["Latitude"], row["Longitude"]],
            radius=5,
            color="#1a5c96",
            fill=True,
            fill_color="#2a7fd4",
            fill_opacity=0.7,
        ).add_to(m)

    st_folium(m, use_container_width=True, height=400)

# ── Data sources ──────────────────────────────────────────────────────────────
st.markdown('<h2 class="section-title">Data sources</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="source-card">
    <div class="source-icon">🏘️</div>
    <div>
        <p class="source-title">Santa Barbara County Rental Listings</p>
        <p class="source-desc">Scraped listings data covering Isla Vista and surrounding neighborhoods, 2016–2025.</p>
    </div>
</div>
<div class="source-card">
    <div class="source-icon">📊</div>
    <div>
        <p class="source-title">NIDDK South Coast Median Rent Data</p>
        <p class="source-desc">Annual median rent by housing type and bedroom count for the Santa Barbara South Coast region.</p>
    </div>
</div>
<div class="source-card">
    <div class="source-icon">📍</div>
    <div>
        <p class="source-title">UCSB Campus Geolocation</p>
        <p class="source-desc">Distance from campus calculated using coordinates from the UCSB campus center point.</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="divider">', unsafe_allow_html=True)

# ── Team ──────────────────────────────────────────────────────────────────────
st.markdown('<h2 class="section-title">The team</h2>', unsafe_allow_html=True)

# Update names/roles to match your actual team
team = [
    ("AK", "Arineh Khachikian", "Frontend Dev, ML Integration, & Cloud Hosting"),
    ("AA", "Anika Achary", "ML Engineer & ML Integration"),
    ("AT", "Anugrha Tamang", "Data Cleaning & Data Analysis"),
    ("HM", "Holly Ma", "Scraping & Data Cleaning"),
    ("EO", "Emily On", "Scraping & Data Cleaning"),
]

cards_html = '<div class="team-grid">'
for initials, name, role in team:
    cards_html += f"""
    <div class="team-card">
        <div class="team-avatar">{initials}</div>
        <p class="team-name">{name}</p>
        <p class="team-role">{role}</p>
    </div>"""
cards_html += '</div>'
st.markdown(cards_html, unsafe_allow_html=True)

# ── Footer banner ─────────────────────────────────────────────────────────────
st.markdown("""
<div class="banner">
    <div style="font-size:36px;">🏠</div>
    <div class="banner-text">
        <h3>UCSB Data Science Club · Project Series 2026</h3>
        <p>Built with open data and a lot of coffee. Questions? Reach out through the UCSB Data Science Club.</p>
    </div>
</div>
""", unsafe_allow_html=True)