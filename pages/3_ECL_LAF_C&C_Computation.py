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
    <h1>ECL LAF and C&C Computation</h1>
</div>
"""
st.markdown(html_template, unsafe_allow_html=True)
st.subheader("Start:")
#st.header('asd')

#st.write('# Income Statement')
st.write('Please **fill** in the form below to auto run **ECL** **Computation** by uploading **ECL** **report** received in xlsx format below:')
st.write('**Computation Failed**')

#year = st.slider("Year", min_value=2020, max_value=2030, step=1)
#month = st.slider("Month", min_value=1, max_value=12, step=1)

date = st.date_input("Date", value=dt.date.today())

df = st.file_uploader(label= "Upload **ECL** **Computation**:")

if df:
  #++++++++++++++++++++++2023+++++++++++++++++++++++++++
  PD = pd.read_excel(df, sheet_name='Lifetime PD', header=55, usecols="B:FZ") #
  #PD.columns = PD.columns.str.replace("\n", " ")#.str.replace(" ", " ")
  #PD.columns = PD.columns.str.strip()
  
  FL_PD = pd.read_excel(df, sheet_name='FL PD', header=59, usecols="B:FZ")

  Active = pd.read_excel(df, sheet_name='Active', header=6, usecols="B:W")
  Active.columns = Active.columns.str.replace("\n", " ")#.str.replace(" ", " ")
  Active.columns = Active.columns.str.strip()

  #st.write(Active.dtypes)
  #st.dataframe(Active)
  #st.write(PD)

  Active=Active.iloc[np.where(~(Active["Finance (SAP) Number"].isna()))]
  Active['Reporting date'] = date
  
  #Date
  Active["First Released Date"] = pd.to_datetime(Active["First Released Date"], errors='coerce')
  Active["Maturity date"] = pd.to_datetime(Active["Maturity date"], errors='coerce')
  Active["Availability period"] = pd.to_datetime(Active["Availability period"], errors='coerce')
  Active["Reporting date"] = pd.to_datetime(Active["Reporting date"], errors='coerce')


  #YOB
  Active["YOB"] = ((Active["Maturity date"].dt.year - Active["Reporting date"].dt.year)*12+(Active["Maturity date"].dt.month - Active["Reporting date"].dt.month))#+1
  
  def extend_row(row):
      # Create a new DataFrame for the row repeated `Value + 1` times
      repeated_rows = pd.DataFrame([row] * (row['YOB'] + 1))
      # Add a new column for the sequence
      repeated_rows['Sequence'] = range(row['YOB'] + 1)
      return repeated_rows
  # Apply the extend_row function for each row and concatenate the results
  extended_Active = pd.concat([extend_row(row) for index, row in Active.iterrows()], ignore_index=True)


  #Principal
  extended_Active.loc[extended_Active["Principal payment (base currency)"]=="-","Principal payment (base currency)"] = 0
  extended_Active["Principal payment (base currency)"] = extended_Active["Principal payment (base currency)"].astype(float)
  extended_Active.loc[extended_Active["Sequence"]==0,"Cal_Principal_payment"] = 0

  extended_Active.loc[(extended_Active["Sequence"]!=0)&(extended_Active["Principal payment frequency"].isin(["Annually"]))&((extended_Active["Sequence"]%12)>0),"Cal_Principal_payment"] = 0
  extended_Active.loc[(extended_Active["Sequence"]!=0)&(extended_Active["Principal payment frequency"].isin(["Annually"]))&((extended_Active["Sequence"]%12)==0),"Cal_Principal_payment"] = extended_Active["Principal payment (base currency)"]

  extended_Active.loc[(extended_Active["Sequence"]!=0)&(extended_Active["Principal payment frequency"].isin(["Semi Annually"]))&((extended_Active["Sequence"]%6)>0),"Cal_Principal_payment"] = 0
  extended_Active.loc[(extended_Active["Sequence"]!=0)&(extended_Active["Principal payment frequency"].isin(["Semi Annually"]))&((extended_Active["Sequence"]%6)==0),"Cal_Principal_payment"] = extended_Active["Principal payment (base currency)"]
  
  extended_Active.loc[(extended_Active["Sequence"]!=0)&(extended_Active["Principal payment frequency"].isin(["Quarterly"]))&((extended_Active["Sequence"]%3)>0),"Cal_Principal_payment"] = 0
  extended_Active.loc[(extended_Active["Sequence"]!=0)&(extended_Active["Principal payment frequency"].isin(["Quarterly"]))&((extended_Active["Sequence"]%3)==0),"Cal_Principal_payment"] = extended_Active["Principal payment (base currency)"]
  
  extended_Active.loc[(extended_Active["Sequence"]!=0)&(extended_Active["Principal payment frequency"].isin(["Bullet"]))&(extended_Active["Sequence"]!=extended_Active["YOB"]),"Cal_Principal_payment"] = 0
  extended_Active.loc[(extended_Active["Sequence"]!=0)&(extended_Active["Principal payment frequency"].isin(["Bullet"]))&(extended_Active["Sequence"]==extended_Active["YOB"]),"Cal_Principal_payment"] = extended_Active["Principal payment (base currency)"]
  
  extended_Active.loc[(extended_Active["Sequence"]!=0)&~(extended_Active["Principal payment frequency"].isin(["Bullet","Quarterly","Semi Annually","Annually"])),"Cal_Principal_payment"] = extended_Active["Principal payment (base currency)"]


  #Interest
  extended_Active.loc[extended_Active["Interest payment (base currency)"]=="-","Interest payment (base currency)"] = 0
  extended_Active["Interest payment (base currency)"] = extended_Active["Interest payment (base currency)"].astype(float)
  extended_Active.loc[extended_Active["Sequence"]==0,"Cal_Interest_payment"] = 0

  extended_Active.loc[(extended_Active["Sequence"]!=0)&(extended_Active["Interest payment frequency"].isin(["Annually"]))&((extended_Active["Sequence"]%12)>0),"Cal_Interest_payment"] = 0
  extended_Active.loc[(extended_Active["Sequence"]!=0)&(extended_Active["Interest payment frequency"].isin(["Annually"]))&((extended_Active["Sequence"]%12)==0),"Cal_Interest_payment"] = extended_Active["Interest payment (base currency)"]

  extended_Active.loc[(extended_Active["Sequence"]!=0)&(extended_Active["Interest payment frequency"].isin(["Semi Annually"]))&((extended_Active["Sequence"]%6)>0),"Cal_Interest_payment"] = 0
  extended_Active.loc[(extended_Active["Sequence"]!=0)&(extended_Active["Interest payment frequency"].isin(["Semi Annually"]))&((extended_Active["Sequence"]%6)==0),"Cal_Interest_payment"] = extended_Active["Interest payment (base currency)"]
  
  extended_Active.loc[(extended_Active["Sequence"]!=0)&(extended_Active["Interest payment frequency"].isin(["Quarterly"]))&((extended_Active["Sequence"]%3)>0),"Cal_Interest_payment"] = 0
  extended_Active.loc[(extended_Active["Sequence"]!=0)&(extended_Active["Interest payment frequency"].isin(["Quarterly"]))&((extended_Active["Sequence"]%3)==0),"Cal_Interest_payment"] = extended_Active["Interest payment (base currency)"]
  
  extended_Active.loc[(extended_Active["Sequence"]!=0)&(extended_Active["Interest payment frequency"].isin(["Bullet"]))&(extended_Active["Sequence"]!=extended_Active["YOB"]),"Cal_Interest_payment"] = 0
  extended_Active.loc[(extended_Active["Sequence"]!=0)&(extended_Active["Interest payment frequency"].isin(["Bullet"]))&(extended_Active["Sequence"]==extended_Active["YOB"]),"Cal_Interest_payment"] = extended_Active["Interest payment (base currency)"]
  
  extended_Active.loc[(extended_Active["Sequence"]!=0)&~(extended_Active["Interest payment frequency"].isin(["Bullet","Quarterly","Semi Annually","Annually"])),"Cal_Interest_payment"] = extended_Active["Interest payment (base currency)"]


  #Installment & its C&C
  extended_Active["Instalment Amount"] = extended_Active["Cal_Principal_payment"]+extended_Active["Cal_Interest_payment"]
  
  extended_Active["Instalment Amount (C&C)"] = extended_Active["Cal_Principal_payment"]+extended_Active["Cal_Interest_payment"]
  extended_Active.loc[extended_Active["Sequence"]==1,"Instalment Amount (C&C)"] = 0


  #Undrawn & its C&C
  extended_Active.loc[extended_Active["Sequence"]==0,"Undrawn_balance"] = 0
  extended_Active.loc[extended_Active["Undrawn amount (base currency)"]==0,"Undrawn_balance"] = 0
  #extended_Active.loc[extended_Active["Sequence"]!=0,"Undrawn_balance"] = extended_Active["Undrawn amount (base currency)"]/extended_Active["YOB"]
  extended_Active.loc[(extended_Active["Revolving/Non-revolving"]=="Non-revolving")&(extended_Active["Sequence"]<=extended_Active["YOB"]),"Undrawn_balance"] = extended_Active["Undrawn amount (base currency)"]/extended_Active["YOB"]
  extended_Active.loc[(extended_Active["Revolving/Non-revolving"]=="Revolving")&(extended_Active["Sequence"]<=12)&(extended_Active["YOB"]>12),"Undrawn_balance"] = extended_Active["Undrawn amount (base currency)"]/(extended_Active["YOB"])
  extended_Active.loc[(extended_Active["Revolving/Non-revolving"]=="Revolving")&(extended_Active["Sequence"]<=extended_Active["YOB"]-1)&(extended_Active["YOB"]<=12),"Undrawn_balance"] = extended_Active["Undrawn amount (base currency)"]/(extended_Active["YOB"]-1)
  extended_Active["Undrawn_balance"].fillna(0, inplace=True)

  #C&C
  #extended_Active.loc[extended_Active["Sequence"]==0,"Undrawn_balance (C&C)"] = 0
  #extended_Active.loc[extended_Active["Sequence"]!=0,"Undrawn_balance (C&C)"] = extended_Active["Undrawn amount (base currency)"]/extended_Active["YOB"]
  #extended_Active.loc[extended_Active["Sequence"]==extended_Active["YOB"],"Undrawn_balance (C&C)"] = extended_Active["Undrawn amount (base currency)"]/extended_Active["YOB"]


  #ori EAD
  #extended_Active["OS + Undisbursed"] = extended_Active["Total outstanding (base currency)"] + extended_Active["Undrawn_balance"] - extended_Active["Instalment Amount"]
  
  #EAD = "OS + (Undisbursed * CCF)
  extended_Active["OS + Undisbursed + CCF"] = extended_Active["Total outstanding (base currency)"] + ((extended_Active["Undrawn_balance"] - extended_Active["Instalment Amount"])*extended_Active["Sequence"])
  extended_Active["OS + Undisbursed + CCF (C&C)"] = extended_Active["Instalment Amount (C&C)"] + ((extended_Active["Undrawn_balance"] - extended_Active["Instalment Amount (C&C)"])*extended_Active["Sequence"])
  
  #==========================Special Case

  #Installment & its C&C 2
  extended_Active["(1) OS + Undisbursed + CCF"] = extended_Active["OS + Undisbursed + CCF"].shift(1)
  extended_Active["(1) OS + Undisbursed + CCF (C&C)"] = extended_Active["OS + Undisbursed + CCF (C&C)"].shift(1)

  extended_Active.loc[extended_Active["Instalment Amount"]>extended_Active["(1) OS + Undisbursed + CCF"],"Instalment Amount"]= extended_Active["(1) OS + Undisbursed + CCF"]
  extended_Active.loc[extended_Active["Instalment Amount (C&C)"]>extended_Active["(1) OS + Undisbursed + CCF (C&C)"],"Instalment Amount (C&C)"]= extended_Active["(1) OS + Undisbursed + CCF (C&C)"]

  extended_Active.loc[extended_Active["Sequence"]==extended_Active["YOB"],"Instalment Amount"]= extended_Active["(1) OS + Undisbursed + CCF"]
  extended_Active.loc[extended_Active["Sequence"]==extended_Active["YOB"],"Instalment Amount (C&C)"]= extended_Active["(1) OS + Undisbursed + CCF (C&C)"]

  extended_Active = extended_Active.drop(["OS + Undisbursed + CCF","OS + Undisbursed + CCF (C&C)","(1) OS + Undisbursed + CCF","(1) OS + Undisbursed + CCF (C&C)"],axis=1)

  extended_Active["OS + Undisbursed + CCF"] = extended_Active["Total outstanding (base currency)"] + ((extended_Active["Undrawn_balance"] - extended_Active["Instalment Amount"])*extended_Active["Sequence"])
  extended_Active["OS + Undisbursed + CCF (C&C)"] = extended_Active["Instalment Amount (C&C)"] + ((extended_Active["Undrawn_balance"] - extended_Active["Instalment Amount (C&C)"])*extended_Active["Sequence"])

  extended_Active.loc[extended_Active["Sequence"]==extended_Active["YOB"],"OS + Undisbursed + CCF"]= 0
  extended_Active.loc[extended_Active["Sequence"]==extended_Active["YOB"],"OS + Undisbursed + CCF (C&C)"]= 0
  
  #==========================Special Case

  PD.PD = PD.PD.str.upper()
  FL_PD.PD = FL_PD.PD.str.upper()

  Pivoted_PD = PD.melt(id_vars="PD",value_vars=[1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,11 ,12 ,13	,14	,15	,16	,17	,18	,19	,20	,21	,22	,23	,24	,25	,26	,27	,28	,29	,30	,31	,32	,33	,34	,35	,36	,37	,38	,39	,40	,41	,42	,43	,44	,45	,46	,47	,48	,49	,50	,51	,52	,53	,54	,55	,56	,57	,58	,59	,60	,61	,62	,63	,64	,65	,66	,67	,68	,69	,70	,71	,72	,73	,74	,75	,76	,77	,78	,79	,80	,81	,82	,83	,84	,85	,86	,87	,88	,89	,90	,91	,92	,93	,94	,95	,96	,97	,98	,99	,100	,101	,102	,103	,104	,105	,106	,107	,108	,109	,110 ,111	,112	,113	,114	,115	,116	,117	,118	,119	,120	,121	,122	,123	,124	,125	,126	,127	,128	,129	,130	,131	,132	,133	,134	,135	,136	,137	,138	,139	,140	,141	,142	,143	,144	,145	,146	,147	,148	,149	,150	,151	,152	,153	,154	,155	,156	,157	,158	,159	,160	,161	,162	,163	,164	,165	,166	,167	,168	,169	,170	,171	,172	,173	,174	,175	,176	,177	,178	,179,180],var_name="Year",value_name="PD%")
  Pivoted_FL_PD = FL_PD.melt(id_vars="PD",value_vars=[1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10 ,11 ,12 ,13	,14	,15	,16	,17	,18	,19	,20	,21	,22	,23	,24	,25	,26	,27	,28	,29	,30	,31	,32	,33	,34	,35	,36	,37	,38	,39	,40	,41	,42	,43	,44	,45	,46	,47	,48	,49	,50	,51	,52	,53	,54	,55	,56	,57	,58	,59	,60	,61	,62	,63	,64	,65	,66	,67	,68	,69	,70	,71	,72	,73	,74	,75	,76	,77	,78	,79	,80	,81	,82	,83	,84	,85	,86	,87	,88	,89	,90	,91	,92	,93	,94	,95	,96	,97	,98	,99	,100	,101	,102	,103	,104	,105	,106	,107	,108	,109	,110 ,111	,112	,113	,114	,115	,116	,117	,118	,119	,120	,121	,122	,123	,124	,125	,126	,127	,128	,129	,130	,131	,132	,133	,134	,135	,136	,137	,138	,139	,140	,141	,142	,143	,144	,145	,146	,147	,148	,149	,150	,151	,152	,153	,154	,155	,156	,157	,158	,159	,160	,161	,162	,163	,164	,165	,166	,167	,168	,169	,170	,171	,172	,173	,174	,175	,176	,177	,178	,179,180],var_name="Year",value_name="FL PD%")
  #st.write(Pivoted_PD)

  extended_Active_PD = extended_Active.merge(Pivoted_PD.rename(columns={"PD":"PD segment","Year":"Sequence"}),on=["PD segment","Sequence"],how="left") #,indicator=True

  #To be Review
  extended_Active_PD["EIR adj"] =1/((1+extended_Active_PD["Profit Rate/ EIR"])**((30.327*extended_Active_PD["Sequence"])/365)) #30.5 number of day in a month
  
  extended_Active_PD["Stage 1 ECL (Overall)"] = extended_Active_PD["OS + Undisbursed + CCF"]*extended_Active_PD["PD%"]*extended_Active_PD["LGD rate"]*extended_Active_PD["EIR adj"]
  
  extended_Active_PD["Stage 1 ECL (C&C)"] = extended_Active_PD["OS + Undisbursed + CCF (C&C)"]*extended_Active_PD["PD%"]*extended_Active_PD["LGD rate"]*extended_Active_PD["EIR adj"]
  
  extended_Active_FL_PD = extended_Active_PD.merge(Pivoted_FL_PD.rename(columns={"PD":"PD segment","Year":"Sequence"}),on=["PD segment","Sequence"],how="left") #,indicator=True

  extended_Active_FL_PD["Stage 2 ECL (Overall)"] = extended_Active_FL_PD["OS + Undisbursed + CCF"]*extended_Active_FL_PD["FL PD%"]*extended_Active_FL_PD["LGD rate"]*extended_Active_FL_PD["EIR adj"]
  
  extended_Active_FL_PD["Stage 2 ECL (C&C)"] = extended_Active_FL_PD["OS + Undisbursed + CCF (C&C)"]*extended_Active_FL_PD["FL PD%"]*extended_Active_FL_PD["LGD rate"]*extended_Active_FL_PD["EIR adj"]
  
  ECL_Filter = extended_Active_FL_PD.iloc[np.where((extended_Active_FL_PD["Watchlist (Yes/No)"]=="No")&((extended_Active_FL_PD["Sequence"]<=12))|(extended_Active_FL_PD["Watchlist (Yes/No)"]=="Yes"))]
  #.fillna(0)

  ECL_Group = ECL_Filter.groupby(["Finance (SAP) Number","Borrower name"])[["Stage 1 ECL (Overall)",
                                                                            "Stage 2 ECL (Overall)",
                                                                            "Stage 1 ECL (C&C)",
                                                                            "Stage 2 ECL (C&C)"]].sum().reset_index()
  #.fillna(0).groupby(["Finance (SAP) Number"])[[]].sum().reset_index()
  #esok sambung group kn by finance number


  #,"Year":""
  #st.write(extended_Active_PD._merge.value_counts())
  #st.write(extended_Active_PD.iloc[np.where(extended_Active_PD._merge=="left_only")])
  st.write(ECL_Filter)
  #st.write(PD)
  #extended_df = extended_df.drop(columns=['YOB'])


  st.write("")

  from io import BytesIO

  def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')

    ECL_Group.to_excel(writer, index=False, sheet_name='Group')
    ECL_Filter.to_excel(writer, index=False, sheet_name='Ori')
    
    #writer.save() 
    writer.close() 
    processed_data = output.getvalue()
    return processed_data
  
  excel_data = to_excel(Active)
  
  st.write("")
  #st.write('Application:')
  st.download_button("Download CSV",
                     data=excel_data,
                     file_name="ECL_Computation.xlsx",
                     mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')