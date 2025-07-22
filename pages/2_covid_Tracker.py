import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="🦠 COVID-19 Tracker", layout="wide")
st.sidebar.title("COVID Dashboard")
st.title("🦠 COVID-19 Tracker")

country = st.text_input("Enter country name:", "Pakistan")

if st.button("Get Data"):
    url = f"https://disease.sh/v3/covid-19/countries/{country}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        st.metric("Total Cases", data["cases"])
        st.metric("Deaths", data["deaths"])
        st.metric("Recovered", data["recovered"])
    else:
        st.error("Country not found!")
