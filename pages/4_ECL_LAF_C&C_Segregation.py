import pandas as pd
import numpy as np
import streamlit as st
import datetime as dt

st.set_page_config(
  page_title = 'ECL - Automation',
  page_icon = "EXIM.png",
  layout="wide"
  )

html_template = """
<div style="display: flex; align-items: center;">
    <img src="https://www.exim.com.my/wp-content/uploads/2022/07/video-thumbnail-preferred-financier.png" alt="EXIM Logo" style="width: 200px; height: 72px; margin-right: 10px;">
    <h1>ECL LAF and C&C Segregation</h1>
</div>
"""
st.markdown(html_template, unsafe_allow_html=True)
st.subheader("Start: Please unprotect all uploaded file")
#st.header('asd')

#st.write('# Income Statement')
st.write('Please **fill** in the form below to auto run **ECL** **Computation** by uploading **ECL** **report** received in xlsx format below:')

#year = st.slider("Year", min_value=2020, max_value=2030, step=1)
#month = st.slider("Month", min_value=1, max_value=12, step=1)

date = st.date_input("Input Reporting Date", value=dt.date.today())

df_latest_laf = st.file_uploader(label= "Upload **ECL LAF Latest**:")
df_latest_cnc = st.file_uploader(label= "Upload **ECL C&C Latest**:")

df_latest_laf1 = st.file_uploader(label= "Upload **ECL LAF DEC FY**:")
df_latest_cnc1 = st.file_uploader(label= "Upload **ECL C&C DEC FY**:")

#sambubng sini unlock kn
df1 = st.file_uploader(label= "Upload Latest Loan Database:")

if df_latest_laf and df_latest_cnc and df_latest_laf1 and df_latest_cnc1 and df1:
  #df_latest_laf.columns = df_latest_laf.columns.str.replace("\n", " ")#.str.replace(" ", " ")
  df_latest_laf = pd.read_excel(df_latest_laf, sheet_name='Active', header=6, usecols="B:AQ") 
  df_latest_laf = df_latest_laf.iloc[np.where(~df_latest_laf["Finance (SAP) Number"].isna())]

  df_latest_cnc = pd.read_excel(df_latest_cnc, sheet_name='Active', header=6, usecols="B:AQ")
  df_latest_cnc = df_latest_cnc.iloc[np.where(~df_latest_cnc["Finance (SAP) Number"].isna())]

  df_latest_laf1 = pd.read_excel(df_latest_laf1, sheet_name='Active', header=6, usecols="B:AQ")
  df_latest_laf1 = df_latest_laf1.iloc[np.where(~df_latest_laf1["Finance (SAP) Number"].isna())]
  
  df_latest_cnc1 = pd.read_excel(df_latest_cnc1, sheet_name='Active', header=6, usecols="B:AQ")
  df_latest_cnc1 = df_latest_cnc1.iloc[np.where(~df_latest_cnc1["Finance (SAP) Number"].isna())]
  #PD.columns = PD.columns.str.strip()

  df1 = pd.read_excel(df1, sheet_name="Loan Database", header=1)

  LDB1 = df1.iloc[np.where(~df1['CIF Number'].isna())][["Finance(SAP) Number","Customer Name","Type of Financing","Nature of Account","Status"]]
  LDB1.columns = LDB1.columns.str.strip()
  LDB1.columns = LDB1.columns.str.replace("\n", "")
  LDB1["Initial"] = LDB1["Customer Name"].str[:15].str.title()

  LDB1["Finance(SAP) Number"] = LDB1["Finance(SAP) Number"].astype(str)



  df_latest_laf["Finance (SAP) Number"] = df_latest_laf["Finance (SAP) Number"].astype(str)
  df_latest_laf1["Finance (SAP) Number"] = df_latest_laf1["Finance (SAP) Number"].astype(str)
  df_latest_cnc["Finance (SAP) Number"] = df_latest_cnc["Finance (SAP) Number"].astype(str)
  df_latest_cnc1["Finance (SAP) Number"] = df_latest_cnc1["Finance (SAP) Number"].astype(str)

  #4 Merge
  df_latest_laf_merge = df_latest_laf.merge(df_latest_cnc[["Finance (SAP) Number","Total.1"]],on="Finance (SAP) Number",how="left", suffixes=("_TOTAL_ECL_BRU","_CNC_BRU")).merge(df_latest_laf1[["Finance (SAP) Number","Total.1"]],on="Finance (SAP) Number",how="left", suffixes=("","_TOTAL_LAF_LAMA")).merge(df_latest_cnc1[["Finance (SAP) Number","Total.1"]],on="Finance (SAP) Number",how="left", suffixes=("","_CNC_LAMA")).merge(LDB1.rename(columns={"Finance(SAP) Number":"Finance (SAP) Number"}),on="Finance (SAP) Number",how="left")
  df_latest_laf_merge.rename(columns={'Total.1':'Total.1_TOTAL_ECL_LAMA'},inplace=True)

  #OM MATERIAL
  df_latest_laf_merge.loc[(df_latest_laf_merge["Finance (SAP) Number"].isin(["500724","500640","500642"])),"Total.1_CNC_BRU"] = 0
  df_latest_laf_merge.loc[(df_latest_laf_merge["Finance (SAP) Number"].isin(["500724","500640","500642"])),"Total.1_CNC_LAMA"] = 0
  
  #st.write(df_latest_laf_merge)

  df_latest_laf_merge["Total.1_LAF_BRU"] = df_latest_laf_merge["Total.1_TOTAL_ECL_BRU"] - df_latest_laf_merge["Total.1_CNC_BRU"]
  df_latest_laf_merge["Total.1_LAF_LAMA"] = df_latest_laf_merge["Total.1_TOTAL_ECL_LAMA"] - df_latest_laf_merge["Total.1_CNC_LAMA"]

  df_latest_laf_merge["Initial"] = df_latest_laf_merge["Borrower name"].str[:15].str.title()
  df_latest_laf_merge = df_latest_laf_merge.merge(LDB1.iloc[np.where(LDB1.Status.isin(["Active","Active-Overdue","Active-Watchlist","Active-Watchlist-Overdue","Impaired"]))][["Initial","Type of Financing"]].drop_duplicates("Initial"),on="Initial",how="left", suffixes=("_Baru","_Lama"))
  df_latest_laf_merge.loc[~(df_latest_laf_merge["Type of Financing_Baru"].isin(["Islamic","Conventional"])),"Type of Financing_Baru"] = df_latest_laf_merge["Type of Financing_Lama"]

  df_latest_laf_merge["Nature of Account"].fillna("Trade", inplace=True)
  
  df_latest_laf_filter = df_latest_laf_merge.fillna(0)[["Finance (SAP) Number",
                                        "Borrower name",
                                        "Nature of Account",
                                        "Type of Financing_Baru",
                                        "Currency",
                                        "Watchlist (Yes/No)",
                                        "Total.1_LAF_BRU",
                                        "Total.1_CNC_BRU",
                                        "Total.1_TOTAL_ECL_BRU",
                                        "Total.1_LAF_LAMA",
                                        "Total.1_CNC_LAMA",
                                        "Total.1_TOTAL_ECL_LAMA"]]

  #st.write(df_latest_laf_filter)

  
  df_latest_laf_filter.loc[(df_latest_laf_filter["Watchlist (Yes/No)"]=="No")&(df_latest_laf_filter["Type of Financing_Baru"]=="Conventional"),"Balance Sheet Stage 1 Conventional (LAF)"] = df_latest_laf_filter["Total.1_LAF_BRU"]
  df_latest_laf_filter.loc[(df_latest_laf_filter["Watchlist (Yes/No)"]=="Yes")&(df_latest_laf_filter["Type of Financing_Baru"]=="Conventional"),"Balance Sheet Stage 2 Conventional (LAF)"] = df_latest_laf_filter["Total.1_LAF_BRU"]
  df_latest_laf_filter.loc[(df_latest_laf_filter["Watchlist (Yes/No)"]=="No")&(df_latest_laf_filter["Type of Financing_Baru"]=="Islamic"),"Balance Sheet Stage 1 Islamic (LAF)"] = df_latest_laf_filter["Total.1_LAF_BRU"]
  df_latest_laf_filter.loc[(df_latest_laf_filter["Watchlist (Yes/No)"]=="Yes")&(df_latest_laf_filter["Type of Financing_Baru"]=="Islamic"),"Balance Sheet Stage 2 Islamic (LAF)"] = df_latest_laf_filter["Total.1_LAF_BRU"]

  df_latest_laf_filter.loc[(df_latest_laf_filter["Watchlist (Yes/No)"]=="No")&(df_latest_laf_filter["Type of Financing_Baru"]=="Conventional"),"Profit & Loss Stage 1 Conventional (LAF)"] = df_latest_laf_filter["Total.1_LAF_BRU"] - df_latest_laf_filter["Total.1_LAF_LAMA"]
  df_latest_laf_filter.loc[(df_latest_laf_filter["Watchlist (Yes/No)"]=="Yes")&(df_latest_laf_filter["Type of Financing_Baru"]=="Conventional"),"Profit & Loss Stage 2 Conventional (LAF)"] = df_latest_laf_filter["Total.1_LAF_BRU"] - df_latest_laf_filter["Total.1_LAF_LAMA"]
  df_latest_laf_filter.loc[(df_latest_laf_filter["Watchlist (Yes/No)"]=="No")&(df_latest_laf_filter["Type of Financing_Baru"]=="Islamic"),"Profit & Loss Stage 1 Islamic (LAF)"] = df_latest_laf_filter["Total.1_LAF_BRU"] - df_latest_laf_filter["Total.1_LAF_LAMA"]
  df_latest_laf_filter.loc[(df_latest_laf_filter["Watchlist (Yes/No)"]=="Yes")&(df_latest_laf_filter["Type of Financing_Baru"]=="Islamic"),"Profit & Loss Stage 2 Islamic (LAF)"] = df_latest_laf_filter["Total.1_LAF_BRU"] - df_latest_laf_filter["Total.1_LAF_LAMA"]

  df_latest_laf_filter.loc[(df_latest_laf_filter["Watchlist (Yes/No)"]=="No")&(df_latest_laf_filter["Type of Financing_Baru"]=="Conventional"),"Balance Sheet Stage 1 Conventional (CNC)"] = df_latest_laf_filter["Total.1_CNC_BRU"]
  df_latest_laf_filter.loc[(df_latest_laf_filter["Watchlist (Yes/No)"]=="Yes")&(df_latest_laf_filter["Type of Financing_Baru"]=="Conventional"),"Balance Sheet Stage 2 Conventional (CNC)"] = df_latest_laf_filter["Total.1_CNC_BRU"]
  df_latest_laf_filter.loc[(df_latest_laf_filter["Watchlist (Yes/No)"]=="No")&(df_latest_laf_filter["Type of Financing_Baru"]=="Islamic"),"Balance Sheet Stage 1 Islamic (CNC)"] = df_latest_laf_filter["Total.1_CNC_BRU"]
  df_latest_laf_filter.loc[(df_latest_laf_filter["Watchlist (Yes/No)"]=="Yes")&(df_latest_laf_filter["Type of Financing_Baru"]=="Islamic"),"Balance Sheet Stage 2 Islamic (CNC)"] = df_latest_laf_filter["Total.1_CNC_BRU"]

  df_latest_laf_filter.loc[(df_latest_laf_filter["Watchlist (Yes/No)"]=="No")&(df_latest_laf_filter["Type of Financing_Baru"]=="Conventional"),"Profit & Loss Stage 1 Conventional (CNC)"] = df_latest_laf_filter["Total.1_CNC_BRU"] - df_latest_laf_filter["Total.1_CNC_LAMA"]
  df_latest_laf_filter.loc[(df_latest_laf_filter["Watchlist (Yes/No)"]=="Yes")&(df_latest_laf_filter["Type of Financing_Baru"]=="Conventional"),"Profit & Loss Stage 2 Conventional (CNC)"] = df_latest_laf_filter["Total.1_CNC_BRU"] - df_latest_laf_filter["Total.1_CNC_LAMA"]
  df_latest_laf_filter.loc[(df_latest_laf_filter["Watchlist (Yes/No)"]=="No")&(df_latest_laf_filter["Type of Financing_Baru"]=="Islamic"),"Profit & Loss Stage 1 Islamic (CNC)"] = df_latest_laf_filter["Total.1_CNC_BRU"] - df_latest_laf_filter["Total.1_CNC_LAMA"]
  df_latest_laf_filter.loc[(df_latest_laf_filter["Watchlist (Yes/No)"]=="Yes")&(df_latest_laf_filter["Type of Financing_Baru"]=="Islamic"),"Profit & Loss Stage 2 Islamic (CNC)"] = df_latest_laf_filter["Total.1_CNC_BRU"] - df_latest_laf_filter["Total.1_CNC_LAMA"]

  df_latest_laf_filter_LAF = df_latest_laf_filter.fillna(0)[["Finance (SAP) Number",
                                        "Borrower name",
                                        "Nature of Account",
                                        "Type of Financing_Baru",
                                        "Currency",
                                        "Balance Sheet Stage 1 Conventional (LAF)",
                                        "Balance Sheet Stage 2 Conventional (LAF)",
                                        "Balance Sheet Stage 1 Islamic (LAF)",
                                        "Balance Sheet Stage 2 Islamic (LAF)",
                                        "Profit & Loss Stage 1 Conventional (LAF)",
                                        "Profit & Loss Stage 2 Conventional (LAF)",
                                        "Profit & Loss Stage 1 Islamic (LAF)",
                                        "Profit & Loss Stage 2 Islamic (LAF)",
                                        "Watchlist (Yes/No)"]]
  
  df_latest_laf_filter_CNC = df_latest_laf_filter.fillna(0)[["Finance (SAP) Number",
                                        "Borrower name",
                                        "Nature of Account",
                                        "Type of Financing_Baru",
                                        "Currency",
                                        "Balance Sheet Stage 1 Conventional (CNC)",
                                        "Balance Sheet Stage 2 Conventional (CNC)",
                                        "Balance Sheet Stage 1 Islamic (CNC)",
                                        "Balance Sheet Stage 2 Islamic (CNC)",
                                        "Profit & Loss Stage 1 Conventional (CNC)",
                                        "Profit & Loss Stage 2 Conventional (CNC)",
                                        "Profit & Loss Stage 1 Islamic (CNC)",
                                        "Profit & Loss Stage 2 Islamic (CNC)",
                                        "Watchlist (Yes/No)"]]



  #df_latest_cnc_merge = df_latest_cnc.merge(df_latest_cnc1[["Finance (SAP) Number","Total.1"]],on="Finance (SAP) Number",how="left", suffixes=("_New","_Old")).merge(LDB1.rename(columns={"Finance(SAP) Number":"Finance (SAP) Number"}),on="Finance (SAP) Number",how="left")

  #df_latest_cnc_merge["Initial"] = df_latest_cnc_merge["Borrower name"].str[:15].str.title()
  #df_latest_cnc_merge = df_latest_cnc_merge.merge(LDB1.iloc[np.where(LDB1.Status.isin(["Active","Active-Overdue","Active-Watchlist","Active-Watchlist-Overdue","Impaired"]))][["Initial","Type of Financing"]].drop_duplicates("Initial"),on="Initial",how="left", suffixes=("_Baru","_Lama"))

  #df_latest_cnc_filter = df_latest_cnc_merge[["Finance (SAP) Number",
  #                                      "Borrower name",
  #                                      "Nature of Account",
  #                                      "Type of Financing_Baru",
  #                                      "Currency",
  #                                      "Watchlist (Yes/No)",
  #                                      "Status",
  #                                      "Total.1_New",
  #                                      "Total.1_Old",
  #                                      "Initial",
  #                                      "Type of Financing_Lama"]]

  #df_latest_cnc_filter.loc[~(df_latest_cnc_filter["Type of Financing_Baru"].isin(["Islamic","Conventional"])),"Type of Financing_Baru"] = df_latest_cnc_filter["Type of Financing_Lama"]

  #df_latest_cnc_filter.loc[(df_latest_cnc_filter["Watchlist (Yes/No)"]=="No")&(df_latest_cnc_filter["Type of Financing_Baru"]=="Conventional"),"Balance Sheet Stage 1 Conventional"] = df_latest_cnc_filter["Total.1_New"]
  #df_latest_cnc_filter.loc[(df_latest_cnc_filter["Watchlist (Yes/No)"]=="Yes")&(df_latest_cnc_filter["Type of Financing_Baru"]=="Conventional"),"Balance Sheet Stage 2 Conventional"] = df_latest_cnc_filter["Total.1_New"]
  #df_latest_cnc_filter.loc[(df_latest_cnc_filter["Watchlist (Yes/No)"]=="No")&(df_latest_cnc_filter["Type of Financing_Baru"]=="Islamic"),"Balance Sheet Stage 1 Islamic"] = df_latest_cnc_filter["Total.1_New"]
  #df_latest_cnc_filter.loc[(df_latest_cnc_filter["Watchlist (Yes/No)"]=="Yes")&(df_latest_cnc_filter["Type of Financing_Baru"]=="Islamic"),"Balance Sheet Stage 2 Islamic"] = df_latest_cnc_filter["Total.1_New"]

  #df_latest_cnc_filter.loc[(df_latest_cnc_filter["Watchlist (Yes/No)"]=="No")&(df_latest_cnc_filter["Type of Financing_Baru"]=="Conventional"),"Profit & Loss Stage 1 Conventional"] = df_latest_cnc_filter["Total.1_New"] - df_latest_cnc_filter["Total.1_Old"]
  #df_latest_cnc_filter.loc[(df_latest_cnc_filter["Watchlist (Yes/No)"]=="Yes")&(df_latest_cnc_filter["Type of Financing_Baru"]=="Conventional"),"Profit & Loss Stage 2 Conventional"] = df_latest_cnc_filter["Total.1_New"] - df_latest_cnc_filter["Total.1_Old"]
  #df_latest_cnc_filter.loc[(df_latest_cnc_filter["Watchlist (Yes/No)"]=="No")&(df_latest_cnc_filter["Type of Financing_Baru"]=="Islamic"),"Profit & Loss Stage 1 Islamic"] = df_latest_cnc_filter["Total.1_New"] - df_latest_cnc_filter["Total.1_Old"]
  #df_latest_cnc_filter.loc[(df_latest_cnc_filter["Watchlist (Yes/No)"]=="Yes")&(df_latest_cnc_filter["Type of Financing_Baru"]=="Islamic"),"Profit & Loss Stage 2 Islamic"] = df_latest_cnc_filter["Total.1_New"] - df_latest_cnc_filter["Total.1_Old"]

  #df_latest_cnc_filter["Nature of Account"].fillna("Trade", inplace=True)

  #df_latest_cnc_filter = df_latest_cnc_filter[["Finance (SAP) Number",
  #                                      "Borrower name",
  #                                      "Nature of Account",
  #                                      "Type of Financing_Baru",
  #                                      "Currency",
  #                                      "Balance Sheet Stage 1 Conventional",
  #                                      "Balance Sheet Stage 2 Conventional",
  #                                      "Balance Sheet Stage 1 Islamic",
  #                                      "Balance Sheet Stage 2 Islamic",
  #                                      "Profit & Loss Stage 1 Conventional",
  #                                      "Profit & Loss Stage 2 Conventional",
  #                                      "Profit & Loss Stage 1 Islamic",
  #                                      "Profit & Loss Stage 2 Islamic"]]



  #LDB1['Customer Name'] = LDB1['Customer Name'].str.title()
  #df_latest_cnc_filter["Borrower name"] = df_latest_cnc_filter["Borrower name"].str.title()
  #df_latest_cnc_filter['matched_value'] = df_latest_cnc_filter['Borrower name'].apply(lambda x: LDB1['Customer Name'][LDB1['Customer Name'].apply(lambda y: y in x)].values[0] if LDB1['Customer Name'].apply(lambda y: y in x).any() else None)

  st.write(df_latest_laf_filter)
  st.write(df_latest_laf_filter.shape)
  st.write(df_latest_laf.shape)
  st.write("SAP Duplication Validation:")
  st.write(df_latest_laf_filter["Finance (SAP) Number"].value_counts())
  
  #st.write(df_latest_cnc_filter.shape)
  #st.write(df_latest_cnc.shape)



  from io import BytesIO

  def to_excel():
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')

    df_latest_laf_filter.to_excel(writer, index=False, sheet_name='Source', header=2)
    df_latest_laf_filter_LAF.to_excel(writer, index=False, sheet_name='LAF (2)', header=2)
    df_latest_laf_filter_CNC.to_excel(writer, index=False, sheet_name='C&C (2)', header=2)
    
    #writer.save() 
    writer.close() 
    processed_data = output.getvalue()
    return processed_data
  
  excel_data = to_excel()
  
  st.write("")
  #st.write('Application:')
  st.download_button("Download CSV",
                     data=excel_data,
                     file_name="ECL_to_MIS "+str(date)+".xlsx",
                     mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')