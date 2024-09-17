#cari add filter kt graph 
#cari cari extract excel
import streamlit as st
import pandas as pd
import numpy as np

#warnings.filterwarnings('ignore')
pd.set_option("display.max_columns", None) 
pd.set_option("display.max_colwidth", 1000) #huruf dlm column
pd.set_option("display.max_rows", 100)
pd.set_option("display.precision", 2) #2 titik perpuluhan


#st.set_page_config(page_title='Title Dashboard') #, page_icon=r'EXIM-Bank//BP_EXIM_SME.jpg' ,layout='wide'
#st.set_page_config(page_title = 'File Uploader')

#----------------------------Title--------------------------------------------------------------------

st.write('## Income Statement')
st.write('To upload trial balance received')

#----------------------------Input--------------------------------------------------------------------

X = st.text_input("Input Date (i.e. 202409):")
Y = st.text_input("Input Name (i.e. 09. Income statement Sep 2024):")

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

#----------------------------Export--------------------------------------------------------------------


st.link_button("Youtube",url="https://www.youtube.com/watch?v=D0D4Pa22iG0")

#https://github.com/pixegami/streamlit-demo-app

 #data = pd.read_excel("Income Statement - Dictionary.xlsx", sheet_name='Keyin', header=0)
 #st.write(data)
