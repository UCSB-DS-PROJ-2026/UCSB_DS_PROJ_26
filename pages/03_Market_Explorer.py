import streamlit as st
import pandas as pd


# Title and subtitle of the webpage
st.title("Market Explorer")
st.write(
    "Explore rent trends, neighborhoods, and pricing patterns in Santa Barbara."
)

st.set_page_config(layout="wide")
left_col, right_col = st.columns([1, 2])
with left_col:
    with st.container(border=True):
        st.subheader("Preferences")

    # Use a form so inputs don't trigger reruns until the button is clicked
    with st.form("preferences_form"):
            # index=2 means select the element at position 2 as default
            bedrooms = st.selectbox("Bedrooms", [0, 1, 2, 3, 4, 5], index=2)
            bathrooms = st.selectbox("Bathrooms", [1, 1.5, 2, 2.5, 3], index=2)
            # (min, max, default, step size)
            dist_min, dist_max = st.slider(
                "Distance from campus (miles)",
                min_value=0.0,
                max_value=5.0,
                value=(1.0, 3.0),   # tuple = range slider
                step=0.1
            )
            budget_min, budget_max = st.slider(
                "Budget ($/month)",
                min_value=500,
                max_value=5000,
                value=(1200, 2500),   # <- tuple = range slider
                step=50
            )
            # Primary call-to-action button
            predict_clicked = st.form_submit_button("Explore Market")

with right_col:
    # Create table that displays the units that the user is looking for
    demo_df = pd.read_csv("data/demo_display_table.csv") # going to replace with the data set that we are actually going to use
    st.dataframe(demo_df, height=500)