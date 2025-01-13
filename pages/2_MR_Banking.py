import pandas as pd
import numpy as np
import streamlit as st
from datetime import datetime

st.set_page_config(
  page_title = 'Management Report - Automation',
  page_icon = "EXIM.png",
  layout="wide"
  )

html_template = """
<div style="display: flex; align-items: center;">
    <img src="https://www.exim.com.my/wp-content/uploads/2022/07/video-thumbnail-preferred-financier.png" alt="EXIM Logo" style="width: 200px; height: 72px; margin-right: 10px;">
    <h1>Banking Aprroval & Acceptance</h1>
</div>
"""
st.markdown(html_template, unsafe_allow_html=True)
st.subheader("Start:")
#st.header('asd')

#st.write('# Income Statement')
st.write('Please **fill** in the form below to auto run **management** **report** by uploading **banking** **report** received in xlsx format below:')

#year = st.slider("Year", min_value=2020, max_value=2030, step=1)
#month = st.slider("Month", min_value=1, max_value=12, step=1)

df = st.file_uploader(label= "Upload **Banking** **Report**:")

if df:
  #++++++++++++++++++++++2023+++++++++++++++++++++++++++
  banking23 = pd.read_excel(df, sheet_name='Applications BF 2023', header=14)
  banking23.columns = banking23.columns.str.replace("\n", " ").str.replace(" ", " ")
  
  banking23["Page"] = "2023"
  banking23.loc[banking23["Date Approved"].isin(["-","0"]),"Date Approved"] = ""
  banking23["Date Approved"] = banking23["Date Approved"].astype(str)
  banking23["Date Approved"] = banking23["Date Approved"].str.strip()
  banking23["Date Approved"] = banking23["Date Approved"].str[:10]
  banking23["Date Approved"] = pd.to_datetime(banking23["Date Approved"], errors='coerce')

  f_b23 = banking23[["CCRIS Application Date",
                     "Date Approved",
                     "Date of Acceptance ",
                     "Date Withdrawal/ Cancellation",
                     "Date Rejected",
                     "Customer Name",
                     "Corporate Status",
                     "BNM Main Sector",
                     "Nature of Account2",
                     "Type of Financing2",
                     "Facility Type / Product Type2",
                     "Currency3",
                     "Application Amount (FX Currency )",
                     "Application Amount (RM)",
                     "Page"]].sort_values("Date Approved",ascending=False)

  f_b23.loc[~(f_b23["Facility Type / Product Type2"].isin(["Forward Foreign Exchange-i","Bank Guarantee-i","Bank Guarantee","Forward Foreign Exchange"])),"LN"]=f_b23["Application Amount (FX Currency )"]
  f_b23.loc[(f_b23["Facility Type / Product Type2"].isin(["Forward Foreign Exchange-i","Bank Guarantee-i","Bank Guarantee","Forward Foreign Exchange"])),"BG"]=f_b23["Application Amount (RM)"]

  #++++++++++++++++++++++2024+++++++++++++++++++++++++++
  banking24 = pd.read_excel(df, sheet_name='Applications 2024', header=14)
  banking24.columns = banking24.columns.str.replace("\n", " ").str.replace(" ", " ")

  banking24["Page"] = "2024"
  banking24.loc[banking24["Date Approved"].isin(["-","0"]),"Date Approved"] = ""
  banking24["Date Approved"] = banking24["Date Approved"].astype(str)
  banking24["Date Approved"] = banking24["Date Approved"].str.strip()
  banking24["Date Approved"] = banking24["Date Approved"].str[:10]
  banking24["Date Approved"] = pd.to_datetime(banking24["Date Approved"], errors='coerce')

  #st.write(banking24.head(1))
  #st.write(banking24["Date Approved"].dtypes)
  #st.write(banking24["Date Approved"].value_counts())

  f_b24 = banking24[["CCRIS Application Date",
                     "Date Approved",
                     "Date of Acceptance ",
                     "Date Withdrawal/ Cancellation",
                     "Date Rejected",
                     "Customer Name",
                     "Corporate Status",
                     "BNM Main Sector",
                     "Nature of Account2",
                     "Type of Financing2",
                     "Facility Type / Product Type2",
                     "Currency3",
                     "Application Amount  (FX Currency )",
                     "Application Amount  (RM)",
                     "Page"]].sort_values("Date Approved",ascending=False)

  f_b24.loc[~(f_b24["Facility Type / Product Type2"].isin(["Forward Foreign Exchange-i","Bank Guarantee-i","Bank Guarantee","Forward Foreign Exchange"])),"LN"]=f_b24["Application Amount  (FX Currency )"]
  f_b24.loc[(f_b24["Facility Type / Product Type2"].isin(["Forward Foreign Exchange-i","Bank Guarantee-i","Bank Guarantee","Forward Foreign Exchange"])),"BG"]=f_b24["Application Amount  (RM)"]

  #++++++++++++++++++++++Process+++++++++++++++++++++++++++
  f_b24.columns = f_b23.columns

  appendR = pd.concat([f_b23, f_b24])

  appendR = appendR.iloc[np.where(~(appendR["Customer Name"].isna()))][["CCRIS Application Date",
                     "Date Approved",
                     "Date of Acceptance ",
                     "Date Withdrawal/ Cancellation",
                     "Date Rejected",
                     "Customer Name",
                     "Corporate Status",
                     "BNM Main Sector",
                     "Nature of Account2",
                     "Type of Financing2",
                     "Facility Type / Product Type2",
                     "Currency3",
                     "Application Amount (FX Currency )",
                     "Application Amount (RM)",
                     "Page",
                     "LN",
                     "BG"]].sort_values("Date Approved",ascending=False)
  
  appendR["No."] = range(1, len(appendR)+1)
  
  from io import BytesIO

  def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    df.to_excel(writer, index=False, sheet_name='Sheet2')
    #writer.save() 
    writer.close() 
    processed_data = output.getvalue()
    return processed_data
  
  excel_data = to_excel(appendR)
  
  st.write("")
  st.write('Application:')
  st.download_button("Download CSV",
                     data=excel_data,
                     file_name="MR - Banking.xlsx",
                     mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
  
  # '+str(year)+"-"+str(month)+
  #st.write(appendR)

  #++++++++++++++++++++++Process+++++++++++++++++++++++++++
