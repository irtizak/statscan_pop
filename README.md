# 📊 Canada Census Data Processing & Visualization

This project provides a streamlined pipeline to process Canadian census data and generate comprehensive population metrics summaries for various geographic regions. The pipeline calculates and visualizes age distributions, population totals, growth rates, median household income, and unemployment rates. It is designed to support further analysis, reporting, and dashboard development using tools such as **Streamlit**.

---

## 📌 Introduction

The objective of this project is to automate the processing of structured census data and make insights accessible through interactive visualizations. It focuses on:

- Age-wise population segmentation  
- Population growth analysis between census years  
- Economic indicators such as median household income and unemployment rates  
- Generating clean, structured outputs for analytics or reporting workflows

An interactive **Streamlit** application is included, allowing users to upload a `.csv` file and view region-specific insights with an intuitive dropdown interface.

---

## 📁 Features

- ✅ Data ingestion from CSV files  
- ✅ Population metrics breakdown by geographic region  
- ✅ Automatic calculation of population growth rates  
- ✅ Age distribution and income statistics  
- ✅ Streamlit dashboard for interactive data exploration  
- ✅ Pivoted view for clear, user-friendly outputs  
- ✅ Basic error handling for missing or malformed inputs

---

## ⚙️ Technologies Used

- Python 3.x  
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
