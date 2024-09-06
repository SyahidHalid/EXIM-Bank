import streamlit as st
import pandas as pd
import numpy as np

#warnings.filterwarnings('ignore')
pd.set_option("display.max_columns", None) 
pd.set_option("display.max_colwidth", 1000) #huruf dlm column
pd.set_option("display.max_rows", 100)
pd.set_option("display.precision", 2) #2 titik perpuluhan

st.set_page_config(page_title = 'File Uploader')

st.write('Testing for income statement')

df1 = st.file_uploader(label= "Upload your dataset 1:")
if df1:
  df1 = pd.read_excel(df1, header=5)
  st.write(df1.head())
  
df2 = st.file_uploader(label= "Upload your dataset 2:")
if df2:
  df2 = pd.read_excel(df2, header=5)
  st.write(df2.head())

df3 = st.file_uploader(label= "Upload your dataset 3:")
if df3:
  df3 = pd.read_excel(df3, header=5)
  df3.rename(columns={"C":"Unnamed:_1",
                            "Comp":"Item",
                            "Bus.":"Account",
                            "Texts":"GL_no.",
                            "Unnamed:_5":"Mapped_to",
                            "Unnamed:_6":"Unnamed:_6",
                            "Unnamed:_7":"Unnamed:_7",
                            "Unnamed:_8":"GL_Category",
                            "Reporting_period":"RM",
                            "Unnamed:_10":"Unnamed:_10"}, inplace=True)
  st.write(df3.head())
  #st.write()
