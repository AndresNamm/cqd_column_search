import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="CQD column search",
    page_icon="🧊",
    layout="wide",
)

@st.cache_data
def read_in_data():
    path = 'https://raw.githubusercontent.com/AndresNamm/cqd_column_search/main/updated_schema.csv'
    print(f"Reading in data from path {path}")
    return pd.read_csv(path)

df = read_in_data()


text = st.text_input('Enter a search term:')


choice = st.selectbox(
    'Choose a category:',
    ('Dimension', 'Measurement', 'All'), index=2)

if len(text) > 0 or choice != "All":
    if choice =="All":
        filtered_df = df[df['Name'].str.lower().str.contains(text.lower())]
    else:
        filtered_df = df[(df['Name'].str.lower().str.contains(text.lower())) & (df['Type'] == choice)]

    st.dataframe(filtered_df, use_container_width=True, hide_index=True)
    values_list = filtered_df['Name'].tolist()
    values_str = ', '.join([f'"{val}"' for val in values_list])
    st.code(values_str, language="python")
else:
    st.dataframe(df, use_container_width=True, hide_index=True,height=3000)

