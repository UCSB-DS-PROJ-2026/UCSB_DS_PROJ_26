import streamlit as st
import pandas as pd
import altair as alt
import os

st.set_page_config(
    page_title="Market Explorer · SB Housing",
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
.main .block-container { padding-top: 2rem; max-width: 1200px; }

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

.results-count {
    font-size: 13px; color: #6b8ba4; margin-bottom: 12px; font-weight: 400;
}
.results-count span { color: #2a7fd4; font-weight: 600; }

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
}
[data-testid="stFormSubmitButton"] > button:hover {
    background: #1a5c96 !important;
}

/* Metric row */
.metric-row {
    display: flex; gap: 14px; margin-bottom: 24px; flex-wrap: wrap;
}
.metric-pill {
    background: #e8f4fd;
    border-radius: 10px;
    padding: 14px 20px;
    flex: 1;
    min-width: 110px;
    text-align: center;
}
.metric-pill .pill-num {
    font-family: 'DM Serif Display', serif;
    font-size: 26px; color: #0a2342; line-height: 1;
}
.metric-pill .pill-label {
    font-size: 12px; color: #6b8ba4; margin-top: 4px; font-weight: 500;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="page-label">Market Explorer</div>
<h1 class="page-title">Find your next place</h1>
<p class="page-subtitle">Browse real Santa Barbara listings filtered to match your budget and lifestyle.</p>
""", unsafe_allow_html=True)

# ── Load data ─────────────────────────────────────
me_df = pd.read_csv("data/combined_data_me.csv")

# ── Layout ────────────────────────────────────────────────────────────────────
left_col, right_col = st.columns([1, 2], gap="large")

for col in me_df.columns:
    if "price" in col.lower() or "rent" in col.lower():
        me_df[col] = pd.to_numeric(me_df[col], errors="coerce")

with left_col:
    st.markdown("""
    <div class="panel-card">
        <p class="panel-title">Your Preferences</p>
    """, unsafe_allow_html=True)

    with st.form("market_form"):
        bedrooms = st.selectbox("Bedrooms", ["select", 0, 1, 2, 3, 4, 5], index=0)
        bathrooms = st.selectbox("Bathrooms", ["select", 1, 1.5, 2, 2.5, 3], index=0)
        dist_min, dist_max = st.slider(
            "Distance from campus (miles)",
            min_value=0.0, max_value=5.0, value=(0.0, 5.0), step=0.1
        )
        budget_min, budget_max = st.slider(
            "Budget ($/month)",
            min_value=500, max_value=5000, value=(500, 5000), step=50
        )
        explore_clicked = st.form_submit_button("Explore Market", use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)

with right_col:
    if me_df is not None:
        # Try to filter if columns exist
        filtered_df = me_df.copy()
        filter_cols = me_df.columns.str.lower().tolist()

        # Apply filters if matching columns exist
        if explore_clicked:
            for col_key, col_val in [("bedrooms", bedrooms), ("bathrooms", bathrooms)]:
                match = [c for c in me_df.columns if col_key in c.lower()]
                if match:
                    filtered_df = filtered_df[filtered_df[match[0]] == col_val]

            price_col = [c for c in me_df.columns if "price" in c.lower() or "rent" in c.lower()]
            if price_col:
                filtered_df = filtered_df[
                    (filtered_df[price_col[0]] >= budget_min) &
                    (filtered_df[price_col[0]] <= budget_max)
                ]

        # Summary metrics
        n = len(filtered_df)
        price_col = [c for c in me_df.columns if "price" in c.lower() or "rent" in c.lower()]
        median_price = f"${filtered_df[price_col[0]].median():,.0f}" if price_col and n > 0 else "N/A"
        min_price = f"${filtered_df[price_col[0]].min():,.0f}" if price_col and n > 0 else "N/A"

        st.markdown(f"""
        <div class="metric-row">
            <div class="metric-pill">
                <div class="pill-num">{n}</div>
                <div class="pill-label">Listings found</div>
            </div>
            <div class="metric-pill">
                <div class="pill-num">{median_price}</div>
                <div class="pill-label">Median rent</div>
            </div>
            <div class="metric-pill">
                <div class="pill-num">{min_price}</div>
                <div class="pill-label">Lowest listed</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # ── Table display — hide lat/lon columns ──────────────────────────────
        hide_cols = [c for c in filtered_df.columns if c.lower() in ["lat", "lon", "latitude", "longitude"]]
        display_df = filtered_df.drop(columns=hide_cols)
        if price_col:
            display_df = display_df.style.format({
                price_col[0]: "${:,.0f}",
                **{c: "{:.0f}" for c in display_df.columns if "bath" in c.lower()},
                **{c: "{:.1f}" for c in display_df.columns if "distance" in c.lower()},
            })

        st.dataframe(
            display_df,
            height=440,
            use_container_width=True,
            hide_index=True
        )

        # Distribution chart if price column exists
        if price_col and n > 5:
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown('<p class="panel-title" style="font-size:18px;">Price Distribution</p>', unsafe_allow_html=True)
            hist_data = filtered_df[[price_col[0]]].dropna()
            chart = alt.Chart(hist_data).mark_bar(
                color="#2a7fd4", opacity=0.8, cornerRadiusTopLeft=4, cornerRadiusTopRight=4
            ).encode(
                x=alt.X(f"{price_col[0]}:Q", bin=alt.Bin(maxbins=20),
                        title="Monthly Rent (USD)", axis=alt.Axis(format="$,.0f")),
                y=alt.Y("count()", title="Number of Listings")
            ).properties(height=220).configure_view(strokeWidth=0).configure_axis(
                grid=True, gridColor="#f0f4f8", domainColor="#dbedf9", tickColor="#dbedf9"
            )
            st.altair_chart(chart, use_container_width=True)

    else:
        st.markdown("""
        <div style="background:#e8f4fd; border-radius:14px; padding:40px 32px; text-align:center;">
            <div style="font-size:40px; margin-bottom:16px;">📂</div>
            <p style="font-family:'DM Serif Display',serif; font-size:22px; color:#0a2342; margin:0 0 10px 0;">
                Listings data not found
            </p>
            <p style="color:#6b8ba4; font-size:14px; max-width:400px; margin:0 auto;">
                Add <code>data/demo_display_table.csv</code> to your repository root. 
                The Market Explorer will populate automatically once the file is present.
            </p>
        </div>
        """, unsafe_allow_html=True)