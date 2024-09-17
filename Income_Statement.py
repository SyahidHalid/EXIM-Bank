#cari add filter kt graph 
#cari cari extract excel
import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt 
import base64

#warnings.filterwarnings('ignore')
pd.set_option("display.max_columns", None) 
pd.set_option("display.max_colwidth", 1000) #huruf dlm column
pd.set_option("display.max_rows", 100)
pd.set_option("display.precision", 2) #2 titik perpuluhan

#----------------------nama kat web atas yg newtab
#png sahajer
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
name_format = form.text_input("Input File Name (ex. 01. Income Statement Jan 2024)")

#age = form.slider("Age", min_value=18, max_value=100, step=1)
#date = form.date_input("Date", value=dt.date.today())

submitted = form.form_submit_button("Submit")
if submitted:
  st.write("Submitted")
  #st.write(year, month)


#----------------------------Upload--------------------------------------------------------------------

df1 = st.file_uploader(label= "Upload EXIB:")
df2 = st.file_uploader(label= "Upload EXIM:")
df3 = st.file_uploader(label= "Upload EXTF:")

if df1:
  df1 = pd.read_excel(df1, header=5)
  st.write(f"Your favorite movie is:{X}")
  st.write(df1.head())
  

if df2:
  df2 = pd.read_excel(df2, header=5)
  st.write(df2.head())


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

#----------------------------Run--------------------------------------------------------------------

is_clicked = st.button("Run")




#----------------------------Testing Graph--------------------------------------------------------------

chart_data = pd.DataFrame(np.random.randn(20,3),columns=["a","b","c"])

st.bar_chart(chart_data)
st.line_chart(chart_data)

#st.write('Dataset')
st.dataframe(chart_data.head(5))
        #csv_Tasks_at_CPDF = convert_df(Tasks_at_CPDF)
st.download_button("Download CSV",
                   chart_data.to_csv(),
                   file_name='Test.csv',
                   mime='text/csv')

#----------------------------Export--------------------------------------------------------------------


#st.link_button("Youtube",url="https://www.youtube.com/watch?v=D0D4Pa22iG0")

#https://github.com/pixegami/streamlit-demo-app

 #data = pd.read_excel("Income Statement - Dictionary.xlsx", sheet_name='Keyin', header=0)
 #st.write(data)
