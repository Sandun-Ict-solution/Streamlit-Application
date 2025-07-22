import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Data Visualizer")

uploaded_file = st.file_uploader("Upload a CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

    column = st.selectbox("Select a column to plot", df.columns)

    fig, ax = plt.subplots()
    df[column].value_counts().plot(kind='bar', ax=ax)
    st.pyplot(fig)
