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
  page_title = 'Management Account - Automation',
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
    <h1>Balance Sheet YTD</h1>
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

#----------------------------Upload--------------------------------------------------------------------

df1 = form.file_uploader(label= "Upload EXIB:")

if df1:
  EXIB = pd.read_excel(df1, header=5)
  #st.write(df1.head(1))

df2 = form.file_uploader(label= "Upload EXIM:")

if df2:
  EXIM = pd.read_excel(df2, header=5) # sheet_name="Sheet1" usecols='B:D'
  #st.write(df2.head(1))

df3 = form.file_uploader(label= "Upload EXTF:")

if df3:
  EXTF = pd.read_excel(df3, header=5)
  #st.write(df3.head(1))

df4 = form.file_uploader(label= "Upload Intangible Asset Template:")

if df4:
  dic_Intangible = pd.read_excel(df4, sheet_name='BS11.Intangibl Asset', header=5)
  dic_Intangible.columns = dic_Intangible.columns.str.replace("\n", "_").str.replace(" ", "_")
  #st.write(df3.head(1))

#Current_Year_Conv = form.text_input("Input Amount Currenct Year Profits (Conventional):")

#Current_Year_Isl = form.text_input("Input Amount Currenct Year Profits (Islamic):")

submitted = form.form_submit_button("Submit")
if submitted:
  #st.write("Submitted")
  #st.write(year, month)

  st.write(f"All file submitted for : "+str(year)+"-"+str(month))

  #Location_dic = r"C:\\Users\\syahidhalid\\Syahid_PC\\Analytics - FAD\\06. Management Account\\Working"
  #file_dic = "Balance Sheet - Dictionary"

  dic_Cash = pd.read_excel("Balance Sheet - Dictionary.xlsx", sheet_name='Cash Bank', header=0)
  dic_Cash.columns = dic_Cash.columns.str.replace("\n", "_").str.replace(" ", "_")

  dic_Depo = pd.read_excel("Balance Sheet - Dictionary.xlsx", sheet_name='Deposit Placement', header=0)
  dic_Depo.columns = dic_Depo.columns.str.replace("\n", "_").str.replace(" ", "_")

  dic_InvSec = pd.read_excel("Balance Sheet - Dictionary.xlsx", sheet_name='Investment Securities', header=0)
  dic_InvSec.columns = dic_InvSec.columns.str.replace("\n", "_").str.replace(" ", "_")

  dic_ECR = pd.read_excel("Balance Sheet - Dictionary.xlsx", sheet_name='ECR', header=0)
  dic_ECR.columns = dic_ECR.columns.str.replace("\n", "_").str.replace(" ", "_")

  dic_LAF = pd.read_excel("Balance Sheet - Dictionary.xlsx", sheet_name='LAF', header=0)
  dic_LAF.columns = dic_LAF.columns.str.replace("\n", "_").str.replace(" ", "_")

  dic_InsReceivables = pd.read_excel("Balance Sheet - Dictionary.xlsx", sheet_name='Insurance receivables', header=0)
  dic_InsReceivables.columns = dic_InsReceivables.columns.str.replace("\n", "_").str.replace(" ", "_")

  dic_Deriv = pd.read_excel("Balance Sheet - Dictionary.xlsx", sheet_name='Derivative Asset', header=0)
  dic_Deriv.columns = dic_Deriv.columns.str.replace("\n", "_").str.replace(" ", "_")

  dic_Other = pd.read_excel("Balance Sheet - Dictionary.xlsx", sheet_name='Other Assets', header=0)
  dic_Other.columns = dic_Other.columns.str.replace("\n", "_").str.replace(" ", "_")

  dic_InvSub = pd.read_excel("Balance Sheet - Dictionary.xlsx", sheet_name='Investment Subsidaries', header=0)
  dic_InvSub.columns = dic_InvSub.columns.str.replace("\n", "_").str.replace(" ", "_")

  dic_InvShare = pd.read_excel("Balance Sheet - Dictionary.xlsx", sheet_name='Investment in Share', header=0)
  dic_InvShare.columns = dic_InvShare.columns.str.replace("\n", "_").str.replace(" ", "_")

  dic_InvProp = pd.read_excel("Balance Sheet - Dictionary.xlsx", sheet_name='Inv Properties', header=0)
  dic_InvProp.columns = dic_InvProp.columns.str.replace("\n", "_").str.replace(" ", "_")

  #dic_Intangible = pd.read_excel(str(Location_dic)+"\\Balance Sheet - Intangible Asset - 202408.xlsx", sheet_name='BS11.Intangibl Asset', header=5)
  #dic_Intangible.columns = dic_Intangible.columns.str.replace("\n", "_").str.replace(" ", "_")

  dic_PropEQ = pd.read_excel("Balance Sheet - Dictionary.xlsx", sheet_name='Property & equipment', header=0)
  dic_PropEQ.columns = dic_PropEQ.columns.str.replace("\n", "_").str.replace(" ", "_")

  dic_ROU = pd.read_excel("Balance Sheet - Dictionary.xlsx", sheet_name='Right of use Assets', header=0)
  dic_ROU.columns = dic_ROU.columns.str.replace("\n", "_").str.replace(" ", "_")

  dic_Bor = pd.read_excel("Balance Sheet - Dictionary.xlsx", sheet_name='Borrowings', header=0)
  dic_Bor.columns = dic_Bor.columns.str.replace("\n", "_").str.replace(" ", "_")

  dic_Oth_Pay = pd.read_excel("Balance Sheet - Dictionary.xlsx", sheet_name='Other Payables', header=0)
  dic_Oth_Pay.columns = dic_Oth_Pay.columns.str.replace("\n", "_").str.replace(" ", "_")

  #B289, GL_Description, Reclassified from Property & Equipment
  #B332, Total Cost as per 110115
  #B373, Total Accumulated Depreciation as per 110115

  #Testing
  #EXIB_name = "EXIB_July2024"
  #EXIM_name = "EXIM_July2024"
  #EXTF_name = "EXTF_July2024"
  #date_file = 202407
  #Income_curr = "07. Income statement Jul 2024"
  Invesment_Properties_Cost = -62999998
  Invesment_Properties_Accumulated_Depreciation = 9570000+(55000*int(month))
  #=(1650000+(55000*12)+(55000*12)+(55000*12)+(55000*12)+(55000*12)+(55000*12)+(55000*12)+(55000*12)+(55000*12)+(55000*12)+(55000*12)+(55000*12)+(55000*Number of Month))
  #Location = r"C:\Users\syahidhalid\Syahid_PC\Analytics - FAD\06. Management Account\\"+str(date_file)

  #EXIB = pd.read_excel(str(Location)+"\\Source\\"+str(EXIB_name)+".xlsx", sheet_name=EXIB_name, header=5)
  EXIB.columns = EXIB.columns.str.replace("\n", "_").str.replace(" ", "_")

  #EXIM = pd.read_excel(str(Location)+"\\Source\\"+str(EXIM_name)+".xlsx", sheet_name=EXIM_name, header=5)
  EXIM.columns = EXIM.columns.str.replace("\n", "_").str.replace(" ", "_")

  #EXTF = pd.read_excel(str(Location)+"\\Source\\"+str(EXTF_name)+".xlsx", sheet_name=EXTF_name, header=5)
  EXTF.columns = EXTF.columns.str.replace("\n", "_").str.replace(" ", "_")

  EXIB1 = EXIB.rename(columns={"C":"Unnamed:_1",
                              "Comp":"Item",
                              "Bus.":"Account",
                              "Texts":"GL_no.",
                              "Unnamed:_5":"Mapped_to",
                              "Unnamed:_6":"Unnamed:_6",
                              "Unnamed:_7":"Unnamed:_7",
                              "Unnamed:_8":"GL_Category",
                              "Reporting_period":"RM",
                              "Unnamed:_10":"Unnamed:_10"})

  EXIM1 = EXIM.rename(columns={"C":"Unnamed:_1",
                              "Comp":"Item",
                              "Bus.":"Account",
                              "Texts":"GL_no.",
                              "Unnamed:_5":"Mapped_to",
                              "Unnamed:_6":"Unnamed:_6",
                              "Unnamed:_7":"Unnamed:_7",
                              "Unnamed:_8":"GL_Category",
                              "Reporting_period":"RM",
                              "Unnamed:_10":"Unnamed:_10"})

  EXTF1 = EXTF.rename(columns={"C":"Unnamed:_1",
                              "Comp":"Item",
                              "Bus.":"Account",
                              "Texts":"GL_no.",
                              "Unnamed:_5":"Mapped_to",
                              "Unnamed:_6":"Unnamed:_6",
                              "Unnamed:_7":"Unnamed:_7",
                              "Unnamed:_8":"GL_Category",
                              "Reporting_period":"RM",
                              "Unnamed:_10":"Unnamed:_10"})

  Income_curr_raw = pd.concat([EXIB1, EXIM1, EXTF1])

  #print(EXIB1.shape)
  #print(EXIM1.shape)
  #print(EXTF1.shape)

  # library
  # Raw

  Income_curr_raw1 = Income_curr_raw.iloc[np.where(~Income_curr_raw['GL_no.'].isna())]

  Income_curr_raw1 = Income_curr_raw1[['Item','GL_no.','Unnamed:_7','Unnamed:_10']].\
      rename(columns={'GL_no.': 'GL_Code_',\
                      'Unnamed:_10':'YTD '+str(year)+"-"+str(month),\
                      'Unnamed:_7':'GL_Category'}).fillna(0)

  Income_curr_raw1.GL_Code_ = Income_curr_raw1.GL_Code_.astype(str)
  Income_curr_raw1.GL_Category = Income_curr_raw1.GL_Category.astype(str)
  Income_curr_raw1['YTD '+str(year)+"-"+str(month)] = Income_curr_raw1['YTD '+str(year)+"-"+str(month)].astype(float)

  #---------------------------------------------Cash Bank------------------------------------------------------------

  dic_op_rev1 = dic_Cash.iloc[np.where(~dic_Cash['GL_Code_'].isna())].fillna(0)

  dic_op_rev1.GL_Code_ = dic_op_rev1.GL_Code_.astype(int)
  dic_op_rev1.GL_Code_ = dic_op_rev1.GL_Code_.astype(str)

  dic_op_rev1 = dic_op_rev1.drop_duplicates('GL_Code_', keep='first')

  Cash = dic_op_rev1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(month)]],on=['GL_Code_'],how='left',suffixes=("_Excel","_SAP")).fillna(0)

  #OpRev['YTD '+str(Income_curr[21:])] = OpRev['YTD '+str(Income_curr[21:])]*-1

  Cash["Balance_Sheet"] = "Asset"

  Cash1 = Cash.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index() #,'Business_Unit'

  #print(sum(Cash1['YTD '+str(Income_curr[21:])]))

  #-----------------------------------------Deposit Placement------------------------------------------------------------

  dic_Depo1 = dic_Depo.iloc[np.where(~dic_Depo['GL_Code_'].isna())].fillna(0)

  dic_Depo1.GL_Code_ = dic_Depo1.GL_Code_.astype(int)
  dic_Depo1.GL_Code_ = dic_Depo1.GL_Code_.astype(str)

  dic_Depo1 = dic_Depo1.drop_duplicates('GL_Code_', keep='first')

  Depo = dic_Depo1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(month)]],on=['GL_Code_'],how='left',suffixes=("_Excel","_SAP")).fillna(0)

  #OpRev['YTD '+str(Income_curr[21:])] = OpRev['YTD '+str(Income_curr[21:])]*-1

  Depo["Balance_Sheet"] = "Asset"
  
  Depo1 = Depo.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index() #,'Business_Unit'

  #print(sum(Depo1['YTD '+str(Income_curr[21:])]))

  #-----------------------------------------Invesment Security------------------------------------------------------------

  dic_InvSec1 = dic_InvSec.iloc[np.where(~dic_InvSec['GL_Code_'].isna())].fillna(0)

  dic_InvSec1.GL_Code_ = dic_InvSec1.GL_Code_.astype(int)
  dic_InvSec1.GL_Code_ = dic_InvSec1.GL_Code_.astype(str)

  dic_InvSec1 = dic_InvSec1.drop_duplicates('GL_Code_', keep='first')

  InvSec = dic_InvSec1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(month)]],on=['GL_Code_'],how='left',suffixes=("_Excel","_SAP")).fillna(0)

  #OpRev['YTD '+str(Income_curr[21:])] = OpRev['YTD '+str(Income_curr[21:])]*-1
  InvSec["Balance_Sheet"] = "Asset"
  InvSec1 = InvSec.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index() #,'Business_Unit'

  #print(sum(InvSec1['YTD '+str(Income_curr[21:])]))

  #-----------------------------------------ECR------------------------------------------------------------

  dic_ECR1 = dic_ECR.iloc[np.where(~dic_ECR['GL_Code_'].isna())].fillna(0)

  dic_ECR1.GL_Code_ = dic_ECR1.GL_Code_.astype(int)
  dic_ECR1.GL_Code_ = dic_ECR1.GL_Code_.astype(str)

  dic_ECR1 = dic_ECR1.drop_duplicates('GL_Code_', keep='first')

  ECR = dic_ECR1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(month)]],on=['GL_Code_'],how='left',suffixes=("_Excel","_SAP")).fillna(0)

  #OpRev['YTD '+str(Income_curr[21:])] = OpRev['YTD '+str(Income_curr[21:])]*-1
  ECR["Balance_Sheet"] = "Asset"
  ECR1 = ECR.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index() #,'Business_Unit'

  #print(sum(ECR1['YTD '+str(Income_curr[21:])]))

  #-----------------------------------------LAF------------------------------------------------------------

  dic_LAF1 = dic_LAF.iloc[np.where(~dic_LAF['GL_Code_'].isna())].fillna(0)

  dic_LAF1.GL_Code_ = dic_LAF1.GL_Code_.astype(int)
  dic_LAF1.GL_Code_ = dic_LAF1.GL_Code_.astype(str)

  dic_LAF1 = dic_LAF1.drop_duplicates('GL_Code_', keep='first')

  LAF = dic_LAF1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(month)]],on=['GL_Code_'],how='left',suffixes=("_Excel","_SAP")).fillna(0)

  #OpRev['YTD '+str(Income_curr[21:])] = OpRev['YTD '+str(Income_curr[21:])]*-1
  LAF["Balance_Sheet"] = "Asset"
  LAF1 = LAF.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index() #,'Business_Unit'

  #print(sum(LAF1['YTD '+str(Income_curr[21:])]))

  #-----------------------------------------Insurance receivables------------------------------------------------------------

  dic_InsReceivables1 = dic_InsReceivables.iloc[np.where(~dic_InsReceivables['GL_Code_'].isna())].fillna(0)

  dic_InsReceivables1.GL_Code_ = dic_InsReceivables1.GL_Code_.astype(int)
  dic_InsReceivables1.GL_Code_ = dic_InsReceivables1.GL_Code_.astype(str)

  dic_InsReceivables1 = dic_InsReceivables1.drop_duplicates('GL_Code_', keep='first')

  InsRecei = dic_InsReceivables1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(month)]],on=['GL_Code_'],how='left',suffixes=("_Excel","_SAP")).fillna(0)

  #OpRev['YTD '+str(Income_curr[21:])] = OpRev['YTD '+str(Income_curr[21:])]*-1
  InsRecei["Balance_Sheet"] = "Asset"
  InsRecei1 = InsRecei.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index() #,'Business_Unit'

  #print(sum(InsRecei1['YTD '+str(Income_curr[21:])]))

  #-----------------------------------------Derivative Asset------------------------------------------------------------

  dic_Deriv1 = dic_Deriv.iloc[np.where(~dic_Deriv['GL_Code_'].isna())].fillna(0)

  dic_Deriv1.GL_Code_ = dic_Deriv1.GL_Code_.astype(int)
  dic_Deriv1.GL_Code_ = dic_Deriv1.GL_Code_.astype(str)

  dic_Deriv1 = dic_Deriv1.drop_duplicates('GL_Code_', keep='first')

  Deriv = dic_Deriv1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(month)]],on=['GL_Code_'],how='left',suffixes=("_Excel","_SAP")).fillna(0)

  #OpRev['YTD '+str(Income_curr[21:])] = OpRev['YTD '+str(Income_curr[21:])]*-1
  Deriv["Balance_Sheet"] = "Asset"
  Deriv1 = Deriv.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index() #,'Business_Unit'

  #print(sum(Deriv1['YTD '+str(Income_curr[21:])]))

  #-----------------------------------------Other Assets------------------------------------------------------------

  dic_Other1 = dic_Other.iloc[np.where(~dic_Other['GL_Code_'].isna())].fillna(0)

  dic_Other1.GL_Code_ = dic_Other1.GL_Code_.astype(int)
  dic_Other1.GL_Code_ = dic_Other1.GL_Code_.astype(str)

  dic_Other1 = dic_Other1.drop_duplicates('GL_Code_', keep='first')

  Other = dic_Other1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(month)]],on=['GL_Code_'],how='left',suffixes=("_Excel","_SAP")).fillna(0)

  #OpRev['YTD '+str(Income_curr[21:])] = OpRev['YTD '+str(Income_curr[21:])]*-1
  Other["Balance_Sheet"] = "Asset"
  Other1 = Other.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index() #,'Business_Unit'

  #print(sum(Other1['YTD '+str(Income_curr[21:])]))

  #-----------------------------------------Investment Subsidaries------------------------------------------------------------

  dic_InvSub1 = dic_InvSub.iloc[np.where(~dic_InvSub['GL_Code_'].isna())].fillna(0)

  dic_InvSub1.GL_Code_ = dic_InvSub1.GL_Code_.astype(int)
  dic_InvSub1.GL_Code_ = dic_InvSub1.GL_Code_.astype(str)

  dic_InvSub1 = dic_InvSub1.drop_duplicates('GL_Code_', keep='first')

  InvSub = dic_InvSub1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(month)]],on=['GL_Code_'],how='left',suffixes=("_Excel","_SAP")).fillna(0)

  #OpRev['YTD '+str(Income_curr[21:])] = OpRev['YTD '+str(Income_curr[21:])]*-1
  InvSub["Balance_Sheet"] = "Asset"
  InvSub1 = InvSub.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index() #,'Business_Unit'

  #print(sum(InvSub1['YTD '+str(Income_curr[21:])]))

  #-----------------------------------------Investment Share------------------------------------------------------------

  dic_InvShare1 = dic_InvShare.iloc[np.where(~dic_InvShare['GL_Code_'].isna())].fillna(0)

  dic_InvShare1.GL_Code_ = dic_InvShare1.GL_Code_.astype(int)
  dic_InvShare1.GL_Code_ = dic_InvShare1.GL_Code_.astype(str)

  dic_InvShare1 = dic_InvShare1.drop_duplicates('GL_Code_', keep='first')

  InvShare = dic_InvShare1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(month)]],on=['GL_Code_'],how='left',suffixes=("_Excel","_SAP")).fillna(0)

  #OpRev['YTD '+str(Income_curr[21:])] = OpRev['YTD '+str(Income_curr[21:])]*-1
  InvShare["Balance_Sheet"] = "Asset"
  InvShare1 = InvShare.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index() #,'Business_Unit'

  #print(sum(InvShare1['YTD '+str(Income_curr[21:])]))

  #-----------------------------------------Investment Properties------------------------------------------------------------

  dic_InvProp1 = dic_InvProp.iloc[np.where(~dic_InvProp['GL_Code_'].isna())].fillna(0)

  dic_InvProp1.GL_Code_ = dic_InvProp1.GL_Code_.astype(int)
  dic_InvProp1.GL_Code_ = dic_InvProp1.GL_Code_.astype(str)

  dic_InvProp1 = dic_InvProp1.drop_duplicates('GL_Code_', keep='first')

  InvProp = dic_InvProp1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(month)]],on=['GL_Code_'],how='left',suffixes=("_Excel","_SAP")).fillna(0)

  #OpRev['YTD '+str(Income_curr[21:])] = OpRev['YTD '+str(Income_curr[21:])]*-1

  df_add_BS10_1 = pd.DataFrame([['Cost of Building',
                          '1',
                          'Cost',
                          'Reclassified into Property & Equipment',
                          'Investment properties',
                          'EXIM',
                          Invesment_Properties_Cost]], columns=['GL_Description','GL_Code_','GL_Category','GL_Description_2','Class','Item','YTD '+str(year)+"-"+str(month)])

  df_add_BS10_2 = pd.DataFrame([['Accumulated depreciation of Building',
                          '2',
                          'Accumulated depreciation',
                          'Reclassified into Property & Equipment',
                          'Investment properties',
                          'EXIM',
                          Invesment_Properties_Accumulated_Depreciation]], columns=['GL_Description','GL_Code_','GL_Category','GL_Description_2','Class','Item','YTD '+str(year)+"-"+str(month)])

  InvProp = pd.concat([InvProp, df_add_BS10_1, df_add_BS10_2])
  InvProp["Balance_Sheet"] = "Asset"
  InvProp1 = InvProp.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index() #,'Business_Unit'

  #print(sum(InvProp1['YTD '+str(Income_curr[21:])]))


  #-----------------------------------------Intangable Asset------------------------------------------------------------

  dic_Intangible1 = dic_Intangible.iloc[np.where(~(dic_Intangible['GL_Description'].isna())&~(dic_Intangible['YTD'].isna()))]

  dic_Intangible1['Item'] = 'EXIM'
  
  dic_Intangible1.rename(columns={'YTD':'YTD '+str(year)+"-"+str(month)},inplace=True)

  dic_Intangible1 = dic_Intangible1[['GL_Description',
                                    'GL_Code_',
                                    'GL_Category',
                                    'GL_Description_2',
                                    'Class',
                                    'Item',
                                    'YTD '+str(year)+"-"+str(month)]]

  dic_Intangible1['GL_Code_'].fillna('NA',inplace=True)
  dic_Intangible1["Balance_Sheet"] = "Asset"

  dic_Intangible1 = dic_Intangible1.iloc[np.where(~dic_Intangible1['GL_Category'].isna())]

  Intangible1 = dic_Intangible1.iloc[np.where(dic_Intangible1['GL_Description'].isin(['Reclassified from Property & Equipment','Total Cost as per 110115','Total Accumulated Depreciation as per 110115']))].fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index() #,'Business_Unit'

  #print(sum(Intangible1['YTD']))

  #-----------------------------------------Property & Equipment------------------------------------------------------------

  dic_PropEQ1 = dic_PropEQ.iloc[np.where(~dic_PropEQ['GL_Code_'].isna())].fillna(0)

  dic_PropEQ1.GL_Code_ = dic_PropEQ1.GL_Code_.astype(int)
  dic_PropEQ1.GL_Code_ = dic_PropEQ1.GL_Code_.astype(str)

  dic_PropEQ1 = dic_PropEQ1.iloc[np.where(~(dic_PropEQ1['GL_Code_'].isin(['110115','110213'])))]

  dic_PropEQ1 = dic_PropEQ1.drop_duplicates('GL_Code_', keep='first')

  PropEQ = dic_PropEQ1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(month)]],on=['GL_Code_'],how='left',suffixes=("_Excel","_SAP")).fillna(0)

  df_add_BS11_1 = pd.DataFrame([['Cost of Building',
                          '3',
                          'Cost',
                          'Reclassified into Property & Equipment',
                          'Property & equipment',
                          'EXIM',
                          -Invesment_Properties_Cost]], columns=['GL_Description','GL_Code_','GL_Category','GL_Description_2','Class','Item','YTD '+str(year)+"-"+str(month)])

  df_add_BS11_2 = pd.DataFrame([['Accumulated depreciation of Building',
                          '4',
                          'Accumulated depreciation',
                          'Reclassified into Property & Equipment',
                          'Property & equipment',
                          'EXIM',
                          -Invesment_Properties_Accumulated_Depreciation]], columns=['GL_Description','GL_Code_','GL_Category','GL_Description_2','Class','Item','YTD '+str(year)+"-"+str(month)])
  
  
  df_add_BS11_3 = dic_Intangible1.iloc[np.where(dic_Intangible1['GL_Description'].isin(['Reclassified from Property & Equipment']) )]
  
  df_add_BS11_3['YTD '+str(year)+"-"+str(month)] = df_add_BS11_3['YTD '+str(year)+"-"+str(month)]*-1
  
  df_add_BS11_3.loc[df_add_BS11_3['GL_Description']=='Reclassified from Property & Equipment', "Class"] = 'Property & equipment'
  
  #st.write(df_add_BS11_3)

  PropEQ = pd.concat([PropEQ, df_add_BS11_1, df_add_BS11_2, df_add_BS11_3]) #
  PropEQ["Balance_Sheet"] = "Asset"
  PropEQ1 = PropEQ.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index() #,'Business_Unit'

  #-----------------------------------------Right of use Assets------------------------------------------------------------

  
  dic_ROU1 = dic_ROU.iloc[np.where(~dic_ROU['GL_Code_'].isna())].fillna(0)

  dic_ROU1.GL_Code_ = dic_ROU1.GL_Code_.astype(int)
  dic_ROU1.GL_Code_ = dic_ROU1.GL_Code_.astype(str)

  dic_ROU1 = dic_ROU1.drop_duplicates('GL_Code_', keep='first')

  ROU = dic_ROU1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(month)]],on=['GL_Code_'],how='left',suffixes=("_Excel","_SAP")).fillna(0)

  #OpRev['YTD '+str(Income_curr[21:])] = OpRev['YTD '+str(Income_curr[21:])]*-1
  ROU["Balance_Sheet"] = "Asset"
  ROU1 = ROU.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index() #,'Business_Unit'

  #-----------------------------------------Total Assets------------------------------------------------------------


  #Cash1.columns=Depo1.columns=InvSec1.columns=ECR1,LAF1.columns=InsRecei1.columns=Deriv1.columns=Other1.columns=InvSub1.columns=InvShare1.columns=InvProp1.columns=Intangible1.columns=PropEQ1.columns
  
  AppendR = pd.concat([Cash1,Depo1,InvSec1,ECR1,LAF1,InsRecei1,Deriv1,Other1,InvSub1,InvShare1,InvProp1,Intangible1,PropEQ1,ROU1])

  AppendR.set_index('Class', inplace=True)

  b = AppendR.T
  b['Total Asset'] = b['Cash & bank balances'] +\
                      b['Deposits & placements with banks & financial institutions']+\
                      b['Investment securities']+\
                      b['Amount due from ECR debtors']+\
                      b['Loans, advances and financing']+\
                      b['Insurance receivables']+\
                      b['Derivative financial instruments']+\
                      b['Other assets']+\
                      b['Investment in subsidiaries']+\
                      b['Investment in share']+\
                      b['Investment properties']+\
                      b['Intangible assets']+\
                      b['Property & equipment']+\
                      b['Right of use Assets']

  #st.write(b['Total Asset'])

  c = b.T
  newdf =c.reset_index()
  
  #-----------------------------------------Borrowings------------------------------------------------------------
  
  dic_Bor1 = dic_Bor.iloc[np.where(~dic_Bor['GL_Code_'].isna())].fillna(0)

  dic_Bor1.GL_Code_ = dic_Bor1.GL_Code_.astype(int)
  dic_Bor1.GL_Code_ = dic_Bor1.GL_Code_.astype(str)

  dic_Bor1 = dic_Bor1.drop_duplicates('GL_Code_', keep='first')

  BORROW = dic_Bor1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(month)]],on=['GL_Code_'],how='left',suffixes=("_Excel","_SAP")).fillna(0)

  BORROW['YTD '+str(year)+"-"+str(month)] = BORROW['YTD '+str(year)+"-"+str(month)]*-1
  
  BORROW["Balance_Sheet"] = "Liabilities"
  BORROW1 = BORROW.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index() #,'Business_Unit'

  BORROW1.loc[BORROW1['Class']=="Medium term notes / Sukuk","Class"]="Borrowings"
  BORROW1.loc[BORROW1['Class']=="Term loans","Class"]="Borrowings"

  BORROW1 = BORROW1.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index() #,'Business_Unit'

  #st.write(BORROW1)
  
  #-----------------------------------------Other payables & accruals------------------------------------------------------------
  
  dic_Oth_Pay1 = dic_Oth_Pay.iloc[np.where(~dic_Oth_Pay['GL_Code_'].isna())].fillna(0)

  dic_Oth_Pay1.GL_Code_ = dic_Oth_Pay1.GL_Code_.astype(int)
  dic_Oth_Pay1.GL_Code_ = dic_Oth_Pay1.GL_Code_.astype(str)

  dic_Oth_Pay1 = dic_Oth_Pay1.drop_duplicates('GL_Code_', keep='first')

  Oth_Payable = dic_Oth_Pay1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(month)]],on=['GL_Code_'],how='left',suffixes=("_Excel","_SAP")).fillna(0)

  Oth_Payable['YTD '+str(year)+"-"+str(month)] = Oth_Payable['YTD '+str(year)+"-"+str(month)]*-1

  Oth_Payable["Balance_Sheet"] = "Liabilities"
  Oth_Payable1 = Oth_Payable.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index() #,'Business_Unit'

  #st.write(sum(Oth_Payable1['YTD '+str(year)+"-"+str(month)]))

  #-----------------------------------------Lease liability------------------------------------------------------------
    
  dic_LL = pd.read_excel("Balance Sheet - Dictionary.xlsx", sheet_name='LeaseLiab', header=0)
  dic_LL.columns = dic_LL.columns.str.replace("\n", "_").str.replace(" ", "_")

  dic_LL1 = dic_LL.iloc[np.where(~dic_LL['GL_Code_'].isna())].fillna(0)

  dic_LL1.GL_Code_ = dic_LL1.GL_Code_.astype(int)
  dic_LL1.GL_Code_ = dic_LL1.GL_Code_.astype(str)

  dic_LL1 = dic_LL1.drop_duplicates('GL_Code_', keep='first')

  LL = dic_LL1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(month)]],on=['GL_Code_'],how='left',suffixes=("_Excel","_SAP")).fillna(0)

  LL['YTD '+str(year)+"-"+str(month)] = LL['YTD '+str(year)+"-"+str(month)]*-1

  LL["Balance_Sheet"] = "Liabilities"
  LL1 = LL.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index() #,'Business_Unit'

  #st.write(sum(LL1['YTD '+str(year)+"-"+str(month)]))
    
  #-----------------------------------------Derivative financial instruments------------------------------------------------------------
      
  dic_Deriv_Fin_Ins = pd.read_excel("Balance Sheet - Dictionary.xlsx", sheet_name='DerivFinIns', header=0)
  dic_Deriv_Fin_Ins.columns = dic_Deriv_Fin_Ins.columns.str.replace("\n", "_").str.replace(" ", "_")

  dic_Deriv_Fin_Ins1 = dic_Deriv_Fin_Ins.iloc[np.where(~dic_Deriv_Fin_Ins['GL_Code_'].isna())].fillna(0)

  dic_Deriv_Fin_Ins1.GL_Code_ = dic_Deriv_Fin_Ins1.GL_Code_.astype(int)
  dic_Deriv_Fin_Ins1.GL_Code_ = dic_Deriv_Fin_Ins1.GL_Code_.astype(str)

  dic_Deriv_Fin_Ins1 = dic_Deriv_Fin_Ins1.drop_duplicates('GL_Code_', keep='first')

  Deriv_Fin_Ins = dic_Deriv_Fin_Ins1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(month)]],on=['GL_Code_'],how='left',suffixes=("_Excel","_SAP")).fillna(0)

  Deriv_Fin_Ins['YTD '+str(year)+"-"+str(month)] = Deriv_Fin_Ins['YTD '+str(year)+"-"+str(month)]*-1

  Deriv_Fin_Ins["Balance_Sheet"] = "Liabilities"
  Deriv_Fin_Ins1 = Deriv_Fin_Ins.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index() #,'Business_Unit'


  #st.write(sum(Deriv_Fin_Ins1['YTD '+str(year)+"-"+str(month)]))
  #st.write(Deriv_Fin_Ins)
  #-----------------------------------------Deferred income------------------------------------------------------------
        
  dic_DefInc = pd.read_excel("Balance Sheet - Dictionary.xlsx", sheet_name='DefInc', header=0)
  dic_DefInc.columns = dic_DefInc.columns.str.replace("\n", "_").str.replace(" ", "_")

  dic_DefInc1 = dic_DefInc.iloc[np.where(~dic_DefInc['GL_Code_'].isna())].fillna(0)

  dic_DefInc1.GL_Code_ = dic_DefInc1.GL_Code_.astype(int)
  dic_DefInc1.GL_Code_ = dic_DefInc1.GL_Code_.astype(str)

  dic_DefInc1 = dic_DefInc1.drop_duplicates('GL_Code_', keep='first')

  DefInc = dic_DefInc1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(month)]],on=['GL_Code_'],how='left',suffixes=("_Excel","_SAP")).fillna(0)

  DefInc['YTD '+str(year)+"-"+str(month)] = DefInc['YTD '+str(year)+"-"+str(month)]*-1

  DefInc["Balance_Sheet"] = "Liabilities"
  DefInc1 = DefInc.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index() #,'Business_Unit'

  #st.write(sum(DefInc1['YTD '+str(year)+"-"+str(month)]))
  
  #st.write(DefInc1)
  #-----------------------------------------Provision for guarantee & claims------------------------------------------------------------
          
  dic_ProvGuarClaim = pd.read_excel("Balance Sheet - Dictionary.xlsx", sheet_name='ProvGuarClaim', header=0)
  dic_ProvGuarClaim.columns = dic_ProvGuarClaim.columns.str.replace("\n", "_").str.replace(" ", "_")

  dic_ProvGuarClaim1 = dic_ProvGuarClaim.iloc[np.where(~dic_ProvGuarClaim['GL_Code_'].isna())].fillna(0)

  dic_ProvGuarClaim1.GL_Code_ = dic_ProvGuarClaim1.GL_Code_.astype(int)
  dic_ProvGuarClaim1.GL_Code_ = dic_ProvGuarClaim1.GL_Code_.astype(str)

  dic_ProvGuarClaim1 = dic_ProvGuarClaim1.drop_duplicates('GL_Code_', keep='first')

  ProvGuarClaim = dic_ProvGuarClaim1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(month)]],on=['GL_Code_'],how='left',suffixes=("_Excel","_SAP")).fillna(0)

  ProvGuarClaim['YTD '+str(year)+"-"+str(month)] = ProvGuarClaim['YTD '+str(year)+"-"+str(month)]*-1

  ProvGuarClaim["Balance_Sheet"] = "Liabilities"
  ProvGuarClaim1 = ProvGuarClaim.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index() #,'Business_Unit'

  #st.write(sum(ProvGuarClaim1['YTD '+str(year)+"-"+str(month)]))
  
  #st.write(ProvGuarClaim1)
  #-----------------------------------------Provision for commitment & contingencies------------------------------------------------------------
            
  dic_CnC = pd.read_excel("Balance Sheet - Dictionary.xlsx", sheet_name='CnC', header=0)
  dic_CnC.columns = dic_CnC.columns.str.replace("\n", "_").str.replace(" ", "_")

  dic_CnC1 = dic_CnC.iloc[np.where(~dic_CnC['GL_Code_'].isna())].fillna(0)

  dic_CnC1.GL_Code_ = dic_CnC1.GL_Code_.astype(int)
  dic_CnC1.GL_Code_ = dic_CnC1.GL_Code_.astype(str)

  dic_CnC1 = dic_CnC1.drop_duplicates('GL_Code_', keep='first')

  CnC = dic_CnC1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(month)]],on=['GL_Code_'],how='left',suffixes=("_Excel","_SAP")).fillna(0)

  CnC['YTD '+str(year)+"-"+str(month)] = CnC['YTD '+str(year)+"-"+str(month)]*-1

  CnC["Balance_Sheet"] = "Liabilities"
  CnC1 = CnC.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index() #,'Business_Unit'

  #st.write(sum(CnC1['YTD '+str(year)+"-"+str(month)]))
  
  #st.write(CnC1)
  #-----------------------------------------Amount due to subsidiaries------------------------------------------------------------
  
  dic_DuetoSub = pd.read_excel("Balance Sheet - Dictionary.xlsx", sheet_name='DuetoSub', header=0)
  dic_DuetoSub.columns = dic_DuetoSub.columns.str.replace("\n", "_").str.replace(" ", "_")

  dic_DuetoSub1 = dic_DuetoSub.iloc[np.where(~dic_DuetoSub['GL_Code_'].isna())].fillna(0)

  dic_DuetoSub1.GL_Code_ = dic_DuetoSub1.GL_Code_.astype(int)
  dic_DuetoSub1.GL_Code_ = dic_DuetoSub1.GL_Code_.astype(str)

  dic_DuetoSub1 = dic_DuetoSub1.drop_duplicates('GL_Code_', keep='first')

  DuetoSub = dic_DuetoSub1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(month)]],on=['GL_Code_'],how='left',suffixes=("_Excel","_SAP")).fillna(0)

  DuetoSub['YTD '+str(year)+"-"+str(month)] = DuetoSub['YTD '+str(year)+"-"+str(month)]*-1

  DuetoSub["Balance_Sheet"] = "Liabilities"
  DuetoSub1 = DuetoSub.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index() #,'Business_Unit'

  #st.write(sum(DuetoSub1['YTD '+str(year)+"-"+str(month)]))
  
  #st.write(DuetoSub1)
  #-----------------------------------------Total Liabilities------------------------------------------------------------
  
  AppendR_1 = pd.concat([BORROW1,Oth_Payable1,LL1,Deriv_Fin_Ins1,DefInc1,ProvGuarClaim1,CnC1,DuetoSub1])

  AppendR_1.set_index('Class', inplace=True)

  b_1 = AppendR_1.T

  b_1['Total Liabilities'] = b_1['Borrowings'] +\
                      b_1['Other payables & accruals']+\
                      b_1['Lease liability']+\
                      b_1['Derivative financial instruments']+\
                      b_1['Deferred income']+\
                      b_1['Provision for guarantee & claims']+\
                      b_1['Provision for commitment & contingencies']+\
                      b_1['Amount due to subsidiaries']

  #st.write(b['Total Asset'])

  c_1 = b_1.T
  newdf_1 = c_1.reset_index()

  newdf['Balance_Sheet'] = "Asset"
  newdf_1['Balance_Sheet'] = "Liabilities"

  newdf_2 = pd.concat([newdf,newdf_1])
  
  #-----------------------------------------Shareholder Fund------------------------------------------------------------
  
  dic_Share = pd.read_excel("Balance Sheet - Dictionary.xlsx", sheet_name='ShareCap', header=0)
  dic_Share.columns = dic_Share.columns.str.replace("\n", "_").str.replace(" ", "_")

  dic_Share1 = dic_Share.iloc[np.where(~dic_Share['GL_Code_'].isna())].fillna(0)

  dic_Share1.GL_Code_ = dic_Share1.GL_Code_.astype(int)
  dic_Share1.GL_Code_ = dic_Share1.GL_Code_.astype(str)

  dic_Share1 = dic_Share1.drop_duplicates('GL_Code_', keep='first')

  Share = dic_Share1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(month)]],on=['GL_Code_'],how='left',suffixes=("_Excel","_SAP")).fillna(0)


  Current_Year_Conv = sum(EXIM.iloc[np.where(EXIM.Texts=="PROFIT BEFORE TAXATION")][['Unnamed:_10']].sum())
  #st.write(a)

  df_add_BS13_1 = pd.DataFrame([['Current year profits Conventional',
                          '5',
                          'Current year profits',
                          'Current year profits',
                          'Retained earnings',
                          'EXIM',
                          float(Current_Year_Conv)]], columns=['GL_Description','GL_Code_','GL_Category','GL_Description_2','Class','Item','YTD '+str(year)+"-"+str(month)])
  
  Current_Year_Isl = sum(EXIB.iloc[np.where(EXIB.Texts=="PROFIT BEFORE TAXATION")][['Unnamed:_10']].sum())
  #st.write(EXIB_1000)

  df_add_BS13_2 = pd.DataFrame([['Current year profits Islamic',
                          '6',
                          'Current year profits',
                          'Current year profits',
                          'Retained earnings',
                          'EXIB',
                          float(Current_Year_Isl)]], columns=['GL_Description','GL_Code_','GL_Category','GL_Description_2','Class','Item','YTD '+str(year)+"-"+str(month)])

  Share = pd.concat([Share, df_add_BS13_1, df_add_BS13_2])

  Share['YTD '+str(year)+"-"+str(month)] = Share['YTD '+str(year)+"-"+str(month)]*-1
  Share["Balance_Sheet"] = "Shareholders' fund"
  
  Share = Share.iloc[np.where(Share['Item']!='EXTF')]

  Share1 = Share.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index() #,'Business_Unit'

  #st.write(sum(Share1['YTD '+str(year)+"-"+str(month)]))
  
  #st.write(Share1)
  #-----------------------------------------------------------------------------------------------------
  
  #AppendR_2 = pd.concat([BORROW1,Oth_Payable1,LL1,Deriv_Fin_Ins1,DefInc1,ProvGuarClaim1,CnC1,DuetoSub1])

  Share2 = Share1.set_index('Class')

  b_2 = Share2.T

  b_2["Total Shareholders' fund"] = b_2['RCCPS shares'] +\
                      b_2['Share capital']+\
                      b_2['Reserves']+\
                      b_2['Retained earnings']
  #st.write(b['Total Asset'])

  c_2 = b_2.T
  newdf_3 = c_2.reset_index()

  newdf_3['Balance_Sheet'] = "Shareholders' fund"

  newdf_4 = pd.concat([newdf_2,newdf_3])
  
  #-----------------------------------------Shareholder Fund------------------------------------------------------------
  
  EXTF_1000 = sum(EXTF.iloc[np.where(EXTF.Texts=="PROFIT BEFORE TAXATION")][['Unnamed:_10']].sum())
  #st.write(EXTF_1000)
  
  df_add_BS14_1 = pd.DataFrame([['Movement in retained earnings',
                          '7',
                          'Movement in retained earnings',
                          'Movement in retained earnings',
                          'Takaful participants fund',
                          'EXTF',
                          float(EXTF_1000)]], columns=['GL_Description','GL_Code_','GL_Category','GL_Description_2','Class','Item','YTD '+str(year)+"-"+str(month)])

  EXTF_1001 = sum(EXTF.iloc[np.where(EXTF.Texts==399999)][['Unnamed:_10']].sum())
  #st.write(EXTF_1000)
  #st.write(EXTF_1001)

  df_add_BS14_2 = pd.DataFrame([['Retained earnings',
                          '8',
                          'Retained earnings',
                          'Retained earnings',
                          'Takaful participants fund',
                          'EXTF',
                          float(EXTF_1001)]], columns=['GL_Description','GL_Code_','GL_Category','GL_Description_2','Class','Item','YTD '+str(year)+"-"+str(month)])


  Tak = pd.concat([df_add_BS14_1, df_add_BS14_2])

  Tak['YTD '+str(year)+"-"+str(month)] = Tak['YTD '+str(year)+"-"+str(month)]*-1
  Tak["Balance_Sheet"] = "Takaful participants fund"
  
  Tak1 = Tak.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index() #,'Business_Unit'

  #Tak2 = Tak1.set_index('Class')

  #d_2 = Tak2.T

  #d_2["Total Shareholders' fund"] = d_2['RCCPS shares'] +\
  #                    d_2['Share capital']

  #e_2 = d_2.T
  #newdf_5 = e_2.reset_index()

  Tak1['Balance_Sheet'] = "Takaful participants fund"

  newdf_5 = pd.concat([newdf_4,Tak1])

  newdf_5_a = newdf_5.set_index('Class')

  newdf_5_b = newdf_5_a.T

  newdf_5_b["Total Balance Sheet"] = newdf_5_b['Total Liabilities'] +\
                      newdf_5_b["Total Shareholders' fund"]+\
                      newdf_5_b['Takaful participants fund']

  newdf_5_c = newdf_5_b.T
  newdf_6 = newdf_5_c.reset_index()

  newdf_6.loc[newdf_6['Class']=="Total Balance Sheet","Balance_Sheet"] = "Total"
  #-----------------------------------------Download------------------------------------------------------------
  
  st.write("")
  st.write("Balance Sheet - Overall (Bank): ")
  st.write(newdf_6)

  st.write("")
  st.download_button("Download CSV",
                   newdf_4.to_csv(index=False),
                   file_name='Balance Sheet - Overall '+str(year)+"-"+str(month)+'.csv',
                   mime='text/csv')
  
  InvSec_Combined = InvSec.drop('Class_2',axis=1)
  Details_Combined = pd.concat([Cash,Depo,InvSec_Combined,ECR,LAF,InsRecei,Deriv,Other,InvSub,InvShare,InvProp,dic_Intangible1,PropEQ,ROU,BORROW,Oth_Payable,LL,Deriv_Fin_Ins,DefInc,ProvGuarClaim,CnC,DuetoSub,Share,Tak])
  

  st.write("")
  st.write("Balance Sheet - Details (Overall): ")
  st.write(Details_Combined)
  
  st.write("")
  st.download_button("Download CSV",
                   Details_Combined.to_csv(index=False),
                   file_name='Balance Sheet - Details '+str(year)+"-"+str(month)+'.csv',
                   mime='text/csv')

  


