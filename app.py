import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("📊 Sales Forecasting Dashboard")

df = pd.read_csv("train.csv")

st.header("Dataset Preview")
st.dataframe(df.head())

st.header("Summary")

st.write("Total Records:", len(df))
st.write("Total Sales:", round(df["Sales"].sum(), 2))
st.write("Regions:", df["Region"].nunique())
st.write("Categories:", df["Category"].nunique())

st.header("Sales by Category")
category = df.groupby("Category")["Sales"].sum()
st.bar_chart(category)

st.header("Sales by Region")
region = df.groupby("Region")["Sales"].sum()
st.bar_chart(region)

st.success("Dashboard Loaded Successfully ✅")