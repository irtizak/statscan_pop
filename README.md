[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/irtizak/statscan_pop)

# 📊 Canada Census Data Processing & Visualization

This project provides a streamlined pipeline to process Canadian census data and generate population metrics summaries for various geographic regions (age distributions, population totals, growth rates, median household income, and unemployment rates). It is designed to support further analysis, reporting, and dashboard development using tools such as **Streamlit**.

---

## 📌 Introduction

The objective of this project is to automate the processing of structured census data and make insights accessible through visualizations. It focuses on:

- Age-wise population segmentation  
- Population growth analysis between census years  
- Economic indicators such as median household income and unemployment rates  
- Generating clean, structured outputs for analytics or reporting workflows

An interactive **Streamlit** application is included, allowing users to upload a `.csv` file and view region-specific insights with a dropdown interface.

> 📘 **Note**: The entire preprocessing pipeline—including data cleaning, transformation, and output generation—is demonstrated in the `technical_test.ipynb` notebook. Read further below to run Streamlit application.

---

## 📁 Features

- ✅ Data ingestion from CSV files  
- ✅ Population metrics breakdown by geographic region  
- ✅ Automatic calculation of population growth rates  
- ✅ Age distribution and income statistics  
- ✅ Streamlit dashboard for interactive data exploration  
- ✅ Pivoted view for clear, user-friendly outputs  

---

## ⚙️ Technologies Used

- Python 3.9.6  
- Pandas  
- Streamlit  
- OpenPyXL (optional Excel support)  
- [`uv`](https://github.com/astral-sh/uv) (optional, for faster dependency installation)  

---

## 🚀 Getting Started

1. Clone this repository  
2. Install dependencies (optionally using [`uv`](https://github.com/astral-sh/uv))  
   ```bash
   pip install -r requirements.txt
   # or
   uv pip install -r requirements.txt
3. Run the Streamlit application locally with the following command:
   ```bash
   streamlit run streamlit_app.py
4. Alternatively, you can access the cloud-deployed app on [Streamlit Cloud](https://statscanpop-urnpvza6axlra6wtpspmtx.streamlit.app/) or [HuggingFace Spaces](https://huggingface.co/spaces/irtizak/statscan-pop).
