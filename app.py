import streamlit as st
import pandas as pd

# App title
st.title("🇨🇦 Canada Population Data")

# Upload CSV file
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read CSV
    df = pd.read_csv(uploaded_file)

    # Expected columns
    expected_columns = [
        'Geographic name', '0 to 14 years', '15 to 19 years', '20 to 64 years',
        '65 years and over', 'Total Population 2021', 'Total Population 2016',
        'Population Growth (%)', 'Median total income of household in 2020',
        'Unemployment Rate (%)'
    ]

    if all(col in df.columns for col in expected_columns):
        # Dropdown for Geographic name
        geo_name = st.selectbox("Select a Geographic Region", df['Geographic name'].unique())

        # Filter row
        selected_row = df[df['Geographic name'] == geo_name].iloc[0]

        # Transpose to field-value format
        result_df = pd.DataFrame({
            "Field": selected_row.index,
            "Value": selected_row.values
        })

        # Display nicely
        st.subheader(f"Data for: {geo_name}")
        st.dataframe(result_df.reset_index(drop=True), use_container_width=True)

    else:
        st.error("Uploaded CSV does not contain the required columns.")
else:
    st.info("Please upload a CSV file to get started.")
