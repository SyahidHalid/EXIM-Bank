import streamlit as st
import pandas as pd
import numpy as np
#import base64
#from PIL import Image
#import plotly.express as px

#warnings.filterwarnings('ignore')
#pd.set_option("display.max_columns", None) 
#pd.set_option("display.max_colwidth", 1000) #huruf dlm column
#pd.set_option("display.max_rows", 100)
#pd.set_option("display.precision", 2) #2 titik perpuluhan

#----------------------nama kat web atas yg newtab (png sahajer)--------------------
st.set_page_config(
  page_title = 'Syahid - Automation',
  page_icon = "EXIM.png",
  layout="wide"
  )

#to show code kat website

#with st.echo():
#  def sum(a, b):
#    return a + b

#----------------------header

html_template = """
<div style="display: flex; align-items: center;">
    <img src="https://www.exim.com.my/wp-content/uploads/2022/07/video-thumbnail-preferred-financier.png" alt="EXIM Logo" style="width: 200px; height: 72px; margin-right: 10px;">
    <h1>Income Statement</h1>
</div>
"""
st.markdown(html_template, unsafe_allow_html=True)
#st.header('asd')
st.subheader("Start:")
#----------------------------Title--------------------------------------------------------------------

#st.write('# Income Statement')
st.write('Please fill in the form below to auto run income statement by uploading trial balance received in xlsx format below:')

#----------------------------Input--------------------------------------------------------------------

#X = st.text_input("Input Date (i.e. 202409):")
#Y = st.text_input("Input Name (i.e. 09. Income statement Sep 2024):")

# klau nk user isi dlu bru boleh forward
#if not X:
#  st.warning("Enter Date!")
#  st.stop()
#st.success("Go ahead")

#if not Y:
#  st.warning("Enter Name!")
#  st.stop()
#st.success("Go ahead")

#----------------------------Form--------------------------------------------------------------------

form = st.form("Basic form")
#name = form.text_input("Name")

#date_format = form.text_input("Input Date (i.e. 202409):")

year = form.slider("Year", min_value=2020, max_value=2030, step=1)
month = form.slider("Month", min_value=1, max_value=12, step=1)
#name_format = form.text_input("Input File Name (ex. 01. Income Statement Jan 2024)")

#age = form.slider("Age", min_value=18, max_value=100, step=1)
#date = form.date_input("Date", value=dt.date.today())

submitted = form.form_submit_button("Submit")
if submitted:
  st.write("Submitted")
  #st.write(year, month)


#----------------------------Upload--------------------------------------------------------------------

df1 = st.file_uploader(label= "Upload EXIB:")

if df1:
  df1 = pd.read_excel(df1, header=5)
  st.write(df1.head(1))

df2 = st.file_uploader(label= "Upload EXIM:")

if df2:
  df2 = pd.read_excel(df2, header=5)
  st.write(df2.head(1))

df3 = st.file_uploader(label= "Upload EXTF:")

if df3:
  df3 = pd.read_excel(df3, header=5)
  st.write(df3.head(1))

 #if df1 and df2 and df3:
  df1.columns = df1.columns.str.replace("\n", "_").str.replace(" ", "_")

  df2.columns = df2.columns.str.replace("\n", "_").str.replace(" ", "_")
  
  df3.columns = df3.columns.str.replace("\n", "_").str.replace(" ", "_")

  st.write(f"All file submitted for : "+str(year)+"-"+str(month))
  #st.write(f"All file submitted for :{str(year)+str(month)}")
  
  df1 = df1.rename(columns={"C":"Unnamed:_1",
                            "Comp":"Item",
                            "Bus.":"Account",
                            "Texts":"GL_no.",
                            "Unnamed:_5":"Mapped_to",
                            "Unnamed:_6":"Unnamed:_6",
                            "Unnamed:_7":"Unnamed:_7",
                            "Unnamed:_8":"GL_Category",
                            "Reporting_period":"RM",
                            "Unnamed:_10":"Unnamed:_10"})
  
  df2 = df2.rename(columns={"C":"Unnamed:_1",
                            "Comp":"Item",
                            "Bus.":"Account",
                            "Texts":"GL_no.",
                            "Unnamed:_5":"Mapped_to",
                            "Unnamed:_6":"Unnamed:_6",
                            "Unnamed:_7":"Unnamed:_7",
                            "Unnamed:_8":"GL_Category",
                            "Reporting_period":"RM",
                            "Unnamed:_10":"Unnamed:_10"})
  
  df3 = df3.rename(columns={"C":"Unnamed:_1",
                            "Comp":"Item",
                            "Bus.":"Account",
                            "Texts":"GL_no.",
                            "Unnamed:_5":"Mapped_to",
                            "Unnamed:_6":"Unnamed:_6",
                            "Unnamed:_7":"Unnamed:_7",
                            "Unnamed:_8":"GL_Category",
                            "Reporting_period":"RM",
                            "Unnamed:_10":"Unnamed:_10"})
  
  Income_curr_raw = pd.concat([df1, df2, df3])

  st.write("Income Statement - Raw: ")
  st.write(Income_curr_raw)

  st.write(Income_curr_raw['Item'].value_counts())

  st.download_button("Download CSV",
                   Income_curr_raw.to_csv(),
                   file_name='Income Statement '+str(year)+"-"+str(month)+'.csv',
                   mime='text/csv')
