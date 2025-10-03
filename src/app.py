import streamlit as st
import pandas as pd

# Title
st.title("Area Wise Average Price Dashboard")

# File uploader
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

# Load file: uploaded OR fallback
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("CSV file uploaded successfully.")
else:
    st.info("No file uploaded. Loading default CSV from data/cal/avg_price.csv")
    try:
        df = pd.read_csv("data/cal/avg_price.csv")
    except FileNotFoundError:
        st.error("Default file not found. Please upload a CSV.")
        st.stop()

# ---- Process Data ----
try:
    # Normalize column names
    df.columns = [col.strip().lower() for col in df.columns]

    # Validate required columns
    required_columns = {"area name", "avg price"}
    if not required_columns.issubset(set(df.columns)):
        st.error("CSV must contain 'area name' and 'avg price' columns.")
        st.stop()

    # Show DataFrame
    st.subheader("Data Preview")
    st.dataframe(df)

    # Convert avg price to numeric
    df["avg price"] = pd.to_numeric(df["avg price"], errors="coerce")
    df = df.dropna(subset=["avg price"])

    # Show summary stats
    st.subheader("Summary Statistics")
    st.write(df.describe())

    # Plot chart
    st.subheader("Average Price by Area")
    st.bar_chart(data=df.set_index("area name")["avg price"])

except Exception as e:
    st.error(f"Error processing file: {e}")
