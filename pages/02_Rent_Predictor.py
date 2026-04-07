import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(layout="wide")

# Title and subtitle of the webpage
st.title("Rent Predictor")
st.write(
    "Enter your housing preferences to estimate rent."
)

st.markdown(
    """
    <div style="
        text-align: center;
        margin-top: 30px;
        margin-bottom: 40px;
        padding: 25px;
        border-radius: 15px;
        background-color: rgba(255,255,255,0.05);
        font-size: 32px;
        font-weight: 600;
    ">
        Estimated Monthly Rent: <span style="color:#ff4b4b;">$0,000</span>
    </div>
    """,
    unsafe_allow_html=True
)

left_col, right_col = st.columns([1, 2])
# Preferences card
with left_col:
    with st.container(border=True):
        st.subheader("Preferences")

    # Use a form so inputs don't trigger reruns until the button is clicked
    with st.form("preferences_form"):
        # index=2 means select the element at position 2 as default
        bedrooms = st.selectbox("Bedrooms", [0, 1, 2, 3, 4, 5], index=2)
        bathrooms = st.selectbox("Bathrooms", [1, 1.5, 2, 2.5, 3], index=2)
        # (min, max, default, step size)
        distance = st.slider(
            "Distance from campus (miles)",
            min_value=0.0,
            max_value=5.0,
            value=(1.0),   # tuple = range slider
            step=0.1
        )
        school_year = st.selectbox(
            "School year",
            ["2026-27", "2027-28", "2028-29", "2029-30"]
        )
        # Primary call-to-action button
        predict_clicked = st.form_submit_button("Predict Rent")


# Median rent over time
# Load CSV
median_rent_df = pd.read_csv("data/median_rent_south_coast_2016_2025.csv")

with right_col:
    # Dropdown: choose housing type
    housing_type = st.selectbox(
        "Select Housing Type:",
        median_rent_df["Housing Type"].unique()
    )

    # Filter dataset
    filtered = median_rent_df[median_rent_df["Housing Type"] == housing_type].copy()

    # Year columns (2016–2025)
    year_cols = [col for col in filtered.columns if col.isdigit()]

    # Reshape wide → long
    long_df = filtered.melt(
        id_vars=["Bedrooms"],
        value_vars=year_cols,
        var_name="Year",
        value_name="Rent"
    )

    # Convert to numeric (NSD becomes NaN)
    long_df["Rent"] = pd.to_numeric(long_df["Rent"], errors="coerce")

    # Convert year to int
    long_df["Year"] = long_df["Year"].astype(str)

    # Drop missing values
    long_df = long_df.dropna()

    # Altair line chart with axis labels
    chart = alt.Chart(long_df).mark_line(point=True).encode(
        x=alt.X("Year:O", title="Year"),
        y=alt.Y("Rent:Q", title="Median Rent (USD)"),
        color=alt.Color("Bedrooms:N", title="Bedrooms"),
        tooltip=["Year", "Bedrooms", "Rent"]
    ).properties(
        width=700,
        height=400,
        title=f"Median Rent vs Time ({housing_type})"
    )

    st.altair_chart(chart, use_container_width=True)