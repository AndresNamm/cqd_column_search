import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="CQD column search",
    page_icon="🧊",
    layout="wide",
)

@st.cache_data
def read_in_data():
    path = 'https://raw.githubusercontent.com/AndresNamm/cqd_column_search/main/schema.csv'
    print(f"Reading in data from path {path}")
    return pd.read_csv(path)

df = read_in_data()


text = st.text_input('Enter a search term:')
if len(text) > 0:
    filtered_df = df[df['friendlyName'].str.lower().str.contains(text.lower())]
    st.dataframe(filtered_df, use_container_width=True, hide_index=True,height=len(filtered_df)*50)
else:
    st.dataframe(df, use_container_width=True, hide_index=True,height=3000)

