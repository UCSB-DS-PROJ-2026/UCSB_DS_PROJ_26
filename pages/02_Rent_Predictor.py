import streamlit as st
import pandas as pd
import altair as alt
import os

st.set_page_config(
    page_title="Rent Predictor · SB Housing",
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
.main .block-container { padding-top: 2rem; max-width: 1100px; }

.page-label {
    font-size: 11px; font-weight: 700; letter-spacing: 2px;
    text-transform: uppercase; color: #2a7fd4; margin-bottom: 6px;
}
.page-title {
    font-family: 'DM Serif Display', serif;
    font-size: 42px; color: #0a2342; margin: 0 0 6px 0; line-height: 1.1;
}
.page-subtitle {
    font-size: 16px; color: #6b8ba4; margin: 0 0 28px 0; font-weight: 300;
}

.prediction-banner {
    background: linear-gradient(135deg, #0a2342 0%, #1a5c96 100%);
    border-radius: 18px;
    padding: 32px 40px;
    margin-bottom: 32px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}
.banner-label {
    color: #7ec8f5;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 8px;
}
.banner-amount {
    font-family: 'DM Serif Display', serif;
    font-size: 58px;
    color: white;
    line-height: 1;
}
.banner-sub {
    color: #7ec8f5;
    font-size: 14px;
    margin-top: 6px;
}
.banner-right {
    text-align: right;
    color: rgba(255,255,255,0.6);
    font-size: 13px;
    line-height: 1.8;
}

.panel-card {
    background: white;
    border: 1px solid #dbedf9;
    border-radius: 16px;
    padding: 0 24px;          
    height: 55px;             

    display: flex;            
    align-items: center;
    margin-bottom: 14px;
}

.panel-title {
    font-family: 'DM Serif Display', serif;
    font-size: 22px;
    color: #0a2342;
    margin: 0;
}

/* Override Streamlit form submit button */
[data-testid="stFormSubmitButton"] > button {
    background: #2a7fd4 !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    font-size: 15px !important;
    padding: 12px 0 !important;
    width: 100% !important;
    margin-top: 8px;
    transition: background 0.2s !important;
}
[data-testid="stFormSubmitButton"] > button:hover {
    background: #1a5c96 !important;
}
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="page-label">Rent Predictor</div>
<h1 class="page-title">How much will you pay?</h1>
<p class="page-subtitle">Set your preferences and get a data-driven estimate for your next lease.</p>
""", unsafe_allow_html=True)

# ── Prediction result state ───────────────────────────────────────────────────
if "prediction" not in st.session_state:
    st.session_state.prediction = None
    st.session_state.pred_inputs = {}

# ── Banner ────────────────────────────────────────────────────────────────────
if st.session_state.prediction:
    p = st.session_state.prediction
    inp = st.session_state.pred_inputs
    st.markdown(f"""
    <div class="prediction-banner">
        <div>
            <div class="banner-label">Estimated Monthly Rent</div>
            <div class="banner-amount">${p:,.0f}</div>
            <div class="banner-sub">per month · {inp.get('school_year','')}</div>
        </div>
        <div class="banner-right">
            {inp.get('bedrooms','–')} bed · {inp.get('bathrooms','–')} bath<br>
            {inp.get('distance','–')} mi from campus<br>
            <span style="color:#60b4ff;font-weight:600;">ML Estimate</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="prediction-banner">
        <div>
            <div class="banner-label">Estimated Monthly Rent</div>
            <div class="banner-amount" style="opacity:0.35;">$–,–––</div>
            <div class="banner-sub">Fill in your preferences and click Predict Rent</div>
        </div>
        <div class="banner-right" style="opacity:0.5;">
            Calculated by Ridge Regression<br>Santa Barbara data
        </div>
    </div>
    """, unsafe_allow_html=True)

# ── Two-column layout ─────────────────────────────────────────────────────────
left_col, right_col = st.columns([1, 1.8], gap="large")

with left_col:
    st.markdown("""
    <div class="panel-card">
        <p class="panel-title">Your Preferences</p>
    """, unsafe_allow_html=True)

    with st.form("preferences_form"):
        bedrooms = st.selectbox("Bedrooms", ["select", 0, 1, 2, 3, 4, 5], index=0)
        bathrooms = st.selectbox("Bathrooms", ["select", 1, 1.5, 2, 2.5, 3], index=0)
        distance = st.slider(
            "Distance from campus (miles)",
            min_value=0.0, max_value=5.0, value=0.0, step=0.1,
        )
        school_year = st.selectbox(
            "School year",
            ["select", "2026-27", "2027-28", "2028-29", "2029-30"]
        )
        predict_clicked = st.form_submit_button("Predict Rent", use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)


# ── Right column: trend chart ─────────────────────────────────────────────────
with right_col:
    st.markdown("""
    <div class="panel-card">
        <p class="panel-title">Rent Trends by Bedroom Count</p>
    """, unsafe_allow_html=True)

    # Load data — handle both local and cloud paths
    data_paths = [
        "data/median_rent_south_coast_2016_2025.csv",
        "pages/data/median_rent_south_coast_2016_2025.csv",
        os.path.join(os.path.dirname(__file__), "../data/median_rent_south_coast_2016_2025.csv"),
    ]
    median_rent_df = None
    for path in data_paths:
        if os.path.exists(path):
            median_rent_df = pd.read_csv(path)
            break

    if median_rent_df is not None:
        housing_type = st.selectbox(
            "Housing type",
            median_rent_df["Housing Type"].unique()
        )
        filtered = median_rent_df[median_rent_df["Housing Type"] == housing_type].copy()
        year_cols = [col for col in filtered.columns if col.isdigit()]
        long_df = filtered.melt(id_vars=["Bedrooms"], value_vars=year_cols, var_name="Year", value_name="Rent")
        long_df["Rent"] = pd.to_numeric(long_df["Rent"], errors="coerce")
        long_df["Year"] = long_df["Year"].astype(str)
        long_df = long_df.dropna()

        chart = alt.Chart(long_df).mark_line(point=True, strokeWidth=2.5).encode(
            x=alt.X("Year:O", title="Year", axis=alt.Axis(labelFontSize=12, titleFontSize=13)),
            y=alt.Y("Rent:Q", title="Median Rent (USD)", axis=alt.Axis(labelFontSize=12, titleFontSize=13, format="$,.0f")),
            color=alt.Color("Bedrooms:N", title="Bedrooms",
                scale=alt.Scale(scheme="blues")),
            tooltip=[
                alt.Tooltip("Year", title="Year"),
                alt.Tooltip("Bedrooms", title="Bedrooms"),
                alt.Tooltip("Rent:Q", title="Median Rent", format="$,.0f")
            ]
        ).properties(height=380).configure_view(
            strokeWidth=0
        ).configure_axis(
            grid=True, gridColor="#f0f4f8", gridOpacity=1,
            domainColor="#dbedf9", tickColor="#dbedf9"
        )
        st.altair_chart(chart, use_container_width=True)
    else:
        st.info("📂 Add `data/median_rent_south_coast_2016_2025.csv` to your repo to enable trend charts.")

    st.markdown('</div>', unsafe_allow_html=True)