import streamlit as st
import pandas as pd

st.write('Hello World!')

st.set_page_config(page_title = 'File Uploader')

df = st.file_uploader(label= "Upload your dataset:")

if df:
  df = pd.read_csv(df)

st.write(df.head(5))
  


