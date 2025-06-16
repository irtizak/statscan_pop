import os
import tempfile

# Set environment variables to fix HuggingFace Spaces permissions
os.environ['STREAMLIT_BROWSER_GATHER_USAGE_STATS'] = 'false'
os.environ['STREAMLIT_SERVER_HEADLESS'] = 'true'
os.environ['STREAMLIT_SERVER_PORT'] = '7860'
os.environ['STREAMLIT_SERVER_ADDRESS'] = '0.0.0.0'

# Set a writable directory for Streamlit config
streamlit_config_dir = os.path.join(tempfile.gettempdir(), '.streamlit')
os.environ['STREAMLIT_CONFIG_DIR'] = streamlit_config_dir

# Create the directory if it doesn't exist
os.makedirs(streamlit_config_dir, exist_ok=True)

# Now import streamlit
import streamlit as st
import pandas as pd
from preprocess import preprocess_data

# App title
st.title("🇨🇦 Canada Population Data")

# Upload CSV file
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read CSV
    df = pd.read_csv(uploaded_file)

    # Preprocess data
    df = preprocess_data(df)

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
