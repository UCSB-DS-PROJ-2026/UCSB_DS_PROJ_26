import streamlit as st
import pandas as pd
import altair as alt
from pathlib import Path

st.set_page_config(layout="wide")

# Title and subtitle of the webpage
st.title("Rent Predictor")
st.write("Enter your housing preferences to estimate rent.")

# Placeholder for the prediction result — updates dynamically after form submit
result_placeholder = st.empty()

left_col, right_col = st.columns([1, 2])

# Preferences card
with left_col:
    # Form wraps subheader + all inputs so they group visually and don't rerun on change
    with st.form("preferences_form"):
        st.subheader("Preferences")

        bedrooms = st.selectbox("Bedrooms", [0, 1, 2, 3, 4, 5], index=2)
        bathrooms = st.selectbox("Bathrooms", [1, 1.5, 2, 2.5, 3], index=2)
        distance = st.slider(
            "Distance from campus (miles)",
            min_value=0.0,
            max_value=5.0,
            value=1.0,
            step=0.1
        )
        school_year = st.selectbox(
            "School year",
            ["2026-27", "2027-28", "2028-29", "2029-30"]
        )

        predict_clicked = st.form_submit_button("Predict Rent")

# Handle prediction when button is clicked
if predict_clicked:
    # TODO: replace this block with your trained model once it's integrated
    # Example: predicted_rent = model.predict([[bedrooms, bathrooms, distance]])[0]
    predicted_rent = None  # placeholder — model not yet integrated

    if predicted_rent is not None:
        result_placeholder.markdown(
            f"""
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
                Estimated Monthly Rent: <span style="color:#ff4b4b;">${predicted_rent:,.0f}</span>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        result_placeholder.info("Model not yet integrated — prediction coming soon.")
else:
    # Default display before any prediction is made
    result_placeholder.markdown(
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
            Estimated Monthly Rent: <span style="color:#ff4b4b;">—</span>
        </div>
        """,
        unsafe_allow_html=True
    )

# Median rent over time chart
# Resolve CSV path relative to this file so it works regardless of where Streamlit is launched from
data_path = Path(__file__).parent / "data" / "median_rent_south_coast_2016_2025.csv"
median_rent_df = pd.read_csv(data_path)

with right_col:
    housing_type = st.selectbox(
        "Select Housing Type:",
        median_rent_df["Housing Type"].unique()
    )

    filtered = median_rent_df[median_rent_df["Housing Type"] == housing_type].copy()

    year_cols = [col for col in filtered.columns if col.isdigit()]

    long_df = filtered.melt(
        id_vars=["Bedrooms"],
        value_vars=year_cols,
        var_name="Year",
        value_name="Rent"
    )

    long_df["Rent"] = pd.to_numeric(long_df["Rent"], errors="coerce")
    long_df["Year"] = long_df["Year"].astype(str)
    long_df = long_df.dropna()

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
