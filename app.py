import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="CQD column search",
    page_icon="🧊",
    layout="wide",
)

@st.cache_data
def read_in_data():
    print("Reading in data")
    return pd.read_csv('schema.csv')

df = read_in_data()


text = st.text_input('Enter a search term:')
st.dataframe(df[df['friendlyName'].str.lower().str.contains(text)],width=1000,height=1000)

