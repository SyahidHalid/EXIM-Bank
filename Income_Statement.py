import streamlit as st
import pandas as pd
import numpy as np
#import base64
#from PIL import Image
import plotly.express as px

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

#form = st.form("Basic form")

#name = form.text_input("Name")

#date_format = form.text_input("Input Date (i.e. 202409):")

#name_format = form.text_input("Input File Name (ex. 01. Income Statement Jan 2024)")

#age = form.slider("Age", min_value=18, max_value=100, step=1)
#date = form.date_input("Date", value=dt.date.today())

#----------------------------Upload--------------------------------------------------------------------

df1 = st.file_uploader(label= "Upload Current EXIB:")

if df1:
  df1 = pd.read_excel(df1, header=5)
  #st.write(df1.head(1))

df2 = st.file_uploader(label= "Upload Current EXIM:")

if df2:
  df2 = pd.read_excel(df2, header=5) # sheet_name="Sheet1" usecols='B:D'
  #st.write(df2.head(1))

df3 = st.file_uploader(label= "Upload Current EXTF:")

if df3:
  df3 = pd.read_excel(df3, header=5)
  #st.write(df3.head(1))

st.write("Current Date:")
year = st.slider("Year", min_value=2020, max_value=2030, step=1)
month = st.slider("Month", min_value=1, max_value=12, step=1)

df4 = st.file_uploader(label= "Upload Previous EXIB:")

if df4:
  df4 = pd.read_excel(df4, header=5)
  #st.write(df1.head(1))

df5 = st.file_uploader(label= "Upload Previous EXIM:")

if df5:
  df5 = pd.read_excel(df5, header=5) # sheet_name="Sheet1" usecols='B:D'
  #st.write(df2.head(1))

df6 = st.file_uploader(label= "Upload Previous EXTF:")

if df6:
  df6 = pd.read_excel(df6, header=5)
  #st.write(df3.head(1))

  #submitted = form.form_submit_button("Submit")
  #if submitted:
  #st.write("Submitted")
  #st.write(year, month)

  st.write(f"All file submitted for : "+str(year)+"-"+str(month))
  #st.write(f"All file submitted for :{str(year)+str(month)}")

  dic_keyin = pd.read_excel("Income Statement - Dictionary.xlsx", sheet_name='Keyin', header=0)
  dic_keyin.columns = dic_keyin.columns.str.replace("\n", "_").str.replace(" ", "_")

  dic_op_rev = pd.read_excel("Income Statement - Dictionary.xlsx", sheet_name='Operating Revenue', header=0)
  dic_op_rev.columns = dic_op_rev.columns.str.replace("\n", "_").str.replace(" ", "_")

  dic_int_inc = pd.read_excel("Income Statement - Dictionary.xlsx", sheet_name='Interest Income', header=0)
  dic_int_inc.columns = dic_int_inc.columns.str.replace("\n", "_").str.replace(" ", "_")

  dic_int_exp = pd.read_excel("Income Statement - Dictionary.xlsx", sheet_name='Interest Expense', header=0)
  dic_int_exp.columns = dic_int_exp.columns.str.replace("\n", "_").str.replace(" ", "_")

  dic_undwr_tkfl = pd.read_excel("Income Statement - Dictionary.xlsx", sheet_name='Underwriting_Takaful results', header=0)
  dic_undwr_tkfl.columns = dic_undwr_tkfl.columns.str.replace("\n", "_").str.replace(" ", "_")

  dic_inc_isl_biz = pd.read_excel("Income Statement - Dictionary.xlsx", sheet_name='Income from Islamic business', header=0)
  dic_inc_isl_biz.columns = dic_inc_isl_biz.columns.str.replace("\n", "_").str.replace(" ", "_")

  dic_oth_inc = pd.read_excel("Income Statement - Dictionary.xlsx", sheet_name='Other income', header=0)
  dic_oth_inc.columns = dic_oth_inc.columns.str.replace("\n", "_").str.replace(" ", "_")

  dic_ovh_exp = pd.read_excel("Income Statement - Dictionary.xlsx", sheet_name='Overhead expenses', header=0)
  dic_ovh_exp.columns = dic_ovh_exp.columns.str.replace("\n", "_").str.replace(" ", "_")

  dic_allw_laf = pd.read_excel("Income Statement - Dictionary.xlsx", sheet_name='Allowances for losses on LAF', header=0)
  dic_allw_laf.columns = dic_allw_laf.columns.str.replace("\n", "_").str.replace(" ", "_")

  dic_allw_dim = pd.read_excel("Income Statement - Dictionary.xlsx", sheet_name='Allowance for diminution', header=0)
  dic_allw_dim.columns = dic_allw_dim.columns.str.replace("\n", "_").str.replace(" ", "_")

  dic_allw_cnc = pd.read_excel("Income Statement - Dictionary.xlsx", sheet_name='Allowance for com and con', header=0)
  dic_allw_cnc.columns = dic_allw_cnc.columns.str.replace("\n", "_").str.replace(" ", "_")

  dic_allw_invsec = pd.read_excel("Income Statement - Dictionary.xlsx", sheet_name='Allowance on investment sec', header=0)
  dic_allw_invsec.columns = dic_allw_invsec.columns.str.replace("\n", "_").str.replace(" ", "_")

  dic_allw_sundry = pd.read_excel("Income Statement - Dictionary.xlsx", sheet_name='General allowance -Sundry debt', header=0)
  dic_allw_sundry.columns = dic_allw_sundry.columns.str.replace("\n", "_").str.replace(" ", "_")

  dic_sur_tkfl = pd.read_excel("Income Statement - Dictionary.xlsx", sheet_name='Less_ Surplus attributable', header=0)
  dic_sur_tkfl.columns = dic_sur_tkfl.columns.str.replace("\n", "_").str.replace(" ", "_")

  tax = pd.read_excel("Income Statement - Dictionary.xlsx", sheet_name='Taxation', header=0)
  tax.columns = tax.columns.str.replace("\n", "_").str.replace(" ", "_")

  conv = pd.read_excel("Income Statement - Dictionary.xlsx", sheet_name='Conventional', header=0)
  conv.columns = conv.columns.str.replace("\n", "_").str.replace(" ", "_")

  isl = pd.read_excel("Income Statement - Dictionary.xlsx", sheet_name='Islamic', header=0)
  isl.columns = isl.columns.str.replace("\n", "_").str.replace(" ", "_")

 #if df1 and df2 and df3:
  df1.columns = df1.columns.str.replace("\n", "_").str.replace(" ", "_")

  df2.columns = df2.columns.str.replace("\n", "_").str.replace(" ", "_")
  
  df3.columns = df3.columns.str.replace("\n", "_").str.replace(" ", "_")

  df4.columns = df4.columns.str.replace("\n", "_").str.replace(" ", "_")

  df5.columns = df5.columns.str.replace("\n", "_").str.replace(" ", "_")

  df6.columns = df6.columns.str.replace("\n", "_").str.replace(" ", "_")


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
  
  df4 = df4.rename(columns={"C":"Unnamed:_1",
                            "Comp":"Item",
                            "Bus.":"Account",
                            "Texts":"GL_no.",
                            "Unnamed:_5":"Mapped_to",
                            "Unnamed:_6":"Unnamed:_6",
                            "Unnamed:_7":"Unnamed:_7",
                            "Unnamed:_8":"GL_Category",
                            "Reporting_period":"RM",
                            "Unnamed:_10":"Unnamed:_10"})
  
  df5 = df5.rename(columns={"C":"Unnamed:_1",
                            "Comp":"Item",
                            "Bus.":"Account",
                            "Texts":"GL_no.",
                            "Unnamed:_5":"Mapped_to",
                            "Unnamed:_6":"Unnamed:_6",
                            "Unnamed:_7":"Unnamed:_7",
                            "Unnamed:_8":"GL_Category",
                            "Reporting_period":"RM",
                            "Unnamed:_10":"Unnamed:_10"})
  
  df6 = df6.rename(columns={"C":"Unnamed:_1",
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

  Income_prev_raw = pd.concat([df4, df5, df6])
  #st.datafreame(df1)

  # Create a sidebar section for user input
  #st.sidebar.title('Dashboard Filters')
  
  # Add a date input component (Default if user does not input any date)
  #min_date = datetime.date(2022,12,13)
  #max_date = datetime.date(2023,4,30)

  Income_curr_raw1 = Income_curr_raw.iloc[np.where(~Income_curr_raw['GL_no.'].isna())]
  Income_prev_raw1 = Income_prev_raw.iloc[np.where(~Income_prev_raw['GL_no.'].isna())]

  Income_curr_raw1 = Income_curr_raw1[['Item','GL_no.','Unnamed:_7','Unnamed:_10']].\
    rename(columns={'GL_no.': 'GL_Code_',\
                    'Unnamed:_10':'YTD '+str(year)+"-"+str(month),\
                    'Unnamed:_7':'GL_Category'}).fillna(0)
  
  Income_prev_raw1 = Income_prev_raw1[['Item','GL_no.','Unnamed:_7','Unnamed:_10']].\
    rename(columns={'GL_no.': 'GL_Code_',\
                    'Unnamed:_10':'YTD '+str(year)+"-"+str(int(month-1)),\
                    'Unnamed:_7':'GL_Category'}).fillna(0)

  Income_curr_raw1.GL_Code_ = Income_curr_raw1.GL_Code_.astype(str)
  Income_curr_raw1.GL_Category = Income_curr_raw1.GL_Category.astype(str)
  Income_curr_raw1['YTD '+str(year)+"-"+str(month)] = Income_curr_raw1['YTD '+str(year)+"-"+str(month)].astype(float)

  Income_prev_raw1.GL_Code_ = Income_prev_raw1.GL_Code_.astype(str)
  Income_prev_raw1.GL_Category = Income_prev_raw1.GL_Category.astype(str)
  Income_prev_raw1['YTD '+str(year)+"-"+str(int(month-1))] = Income_prev_raw1['YTD '+str(year)+"-"+str(int(month-1))].astype(float)


  #----------------------------------------------Keyin-------------------------------------------------------------

  dic_keyin1 = dic_keyin.iloc[np.where(~dic_keyin['GL_Code_'].isna())].fillna(0)
  dic_keyin1.GL_Code_ = dic_keyin1.GL_Code_.astype(str)
  dic_keyin1.GL_Category = dic_keyin1.GL_Category.astype(str)
  dic_keyin1 = dic_keyin1.drop_duplicates('GL_Code_', keep='first')

  keyin = dic_keyin1.merge(Income_curr_raw1[['GL_Code_','YTD '+str(year)+"-"+str(month)]],on=['GL_Code_'],how='left').fillna(0)
  keyin_p = dic_keyin1.merge(Income_prev_raw1[['GL_Code_','YTD '+str(year)+"-"+str(int(month-1))]],on=['GL_Code_'],how='left').fillna(0)
  
  #----------------------------------------------Op Rev-------------------------------------------------------------

  dic_op_rev1 = dic_op_rev.iloc[np.where(~dic_op_rev['GL_Code_'].isna())].fillna(0)
  dic_op_rev1.GL_Code_ = dic_op_rev1.GL_Code_.astype(int)
  dic_op_rev1.GL_Code_ = dic_op_rev1.GL_Code_.astype(str)
  dic_op_rev1 = dic_op_rev1.drop_duplicates('GL_Code_', keep='first')

  OpRev = dic_op_rev1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(month)]],on=['GL_Code_'],how='left',suffixes=("_Excel","_SAP")).fillna(0)
  OpRev['YTD '+str(year)+"-"+str(month)] = OpRev['YTD '+str(year)+"-"+str(month)]*-1
  OpRev1 = OpRev.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index() #,'Business_Unit'

  OpRev_P = dic_op_rev1.merge(Income_prev_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(int(month-1))]],on=['GL_Code_'],how='left',suffixes=("_Excel","_SAP")).fillna(0)
  OpRev_P['YTD '+str(year)+"-"+str(int(month-1))] = OpRev_P['YTD '+str(year)+"-"+str(int(month-1))]*-1
  OpRev1_P = OpRev_P.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(int(month-1))]].sum().reset_index() #,'Business_Unit'

  #----------------------------------------------Int Inc-------------------------------------------------------------

  dic_int_inc1 = dic_int_inc.iloc[np.where(~dic_int_inc['GL_Code_'].isna())].fillna(0)
  dic_int_inc1.GL_Code_ = dic_int_inc1.GL_Code_.astype(int)
  dic_int_inc1.GL_Code_ = dic_int_inc1.GL_Code_.astype(str)
  dic_int_inc1 = dic_int_inc1.drop_duplicates('GL_Code_', keep='first')

  IntInc = dic_int_inc1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(month)]],on=['GL_Code_'],how='left').fillna(0)
  IntInc['YTD '+str(year)+"-"+str(month)] = IntInc['YTD '+str(year)+"-"+str(month)]*-1
  IntInc1 = IntInc.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index() #,'Business_Unit'
  
  IntInc_P = dic_int_inc1.merge(Income_prev_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(int(month-1))]],on=['GL_Code_'],how='left').fillna(0)
  IntInc_P['YTD '+str(year)+"-"+str(int(month-1))] = IntInc_P['YTD '+str(year)+"-"+str(int(month-1))]*-1
  IntInc1_P = IntInc_P.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(int(month-1))]].sum().reset_index() #,'Business_Unit'
  
  #----------------------------------------------Int Exp-------------------------------------------------------------

  dic_int_exp1 = dic_int_exp.iloc[np.where(~dic_int_exp['GL_Code_'].isna())].fillna(0)
  dic_int_exp1.GL_Code_ = dic_int_exp1.GL_Code_.astype(int)
  dic_int_exp1.GL_Code_ = dic_int_exp1.GL_Code_.astype(str)
  dic_int_exp1 = dic_int_exp1.drop_duplicates('GL_Code_', keep='first')

  IntExp = dic_int_exp1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(month)]],on=['GL_Code_'],how='left').fillna(0)
  IntExp['YTD '+str(year)+"-"+str(month)] = IntExp['YTD '+str(year)+"-"+str(month)]*-1
  IntExp1 = IntExp.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index() #,'Business_Unit'

  IntExp_P = dic_int_exp1.merge(Income_prev_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(int(month-1))]],on=['GL_Code_'],how='left').fillna(0)
  IntExp_P['YTD '+str(year)+"-"+str(int(month-1))] = IntExp_P['YTD '+str(year)+"-"+str(int(month-1))]*-1
  IntExp1_P = IntExp_P.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(int(month-1))]].sum().reset_index() #,'Business_Unit'


  frames = [OpRev1, IntInc1, IntExp1] 
  appendR = pd.concat(frames)

  frames_P = [OpRev1_P, IntInc1_P, IntExp1_P] 
  appendR_P = pd.concat(frames_P)

  appendR.set_index('Class', inplace=True)
  appendR_P.set_index('Class', inplace=True)

  b = appendR.T
  b['Net Interest Income'] = b['Interest Income'] + b['Interest Expense']
  c = b.T
  newdf =c.reset_index()

  b_P = appendR_P.T
  b_P['Net Interest Income'] = b_P['Interest Income'] + b_P['Interest Expense']
  c_P = b_P.T
  newdf_P =c_P.reset_index()

  #----------------------------------------------Underwriting/Takaful results-------------------------------------------------------------

  dic_undwr_tkfl1 = dic_undwr_tkfl.iloc[np.where(~dic_undwr_tkfl['GL_Code_'].isna())].fillna(0)
  #dic_undwr_tkfl1.GL_Code_ = dic_undwr_tkfl1.GL_Code_.astype(int)
  dic_undwr_tkfl1.GL_Code_ = dic_undwr_tkfl1.GL_Code_.astype(str)
  dic_undwr_tkfl1 = dic_undwr_tkfl1.drop_duplicates('GL_Code_', keep='first')

  UndwrTkfl = dic_undwr_tkfl1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(month)]],on=['GL_Code_'],how='left').fillna(0)
  UndwrTkfl['YTD '+str(year)+"-"+str(month)] = UndwrTkfl['YTD '+str(year)+"-"+str(month)]*-1
  UndwrTkfl1 = UndwrTkfl.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index() #,'Business_Unit'

  UndwrTkfl_P = dic_undwr_tkfl1.merge(Income_prev_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(int(month-1))]],on=['GL_Code_'],how='left').fillna(0)
  UndwrTkfl_P['YTD '+str(year)+"-"+str(int(month-1))] = UndwrTkfl_P['YTD '+str(year)+"-"+str(int(month-1))]*-1
  UndwrTkfl1_P = UndwrTkfl_P.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(int(month-1))]].sum().reset_index() #,'Business_Unit'

  #----------------------------------------------Income from Islamic Businesses-------------------------------------------------------------

  dic_inc_isl_biz1 = dic_inc_isl_biz.iloc[np.where(~dic_inc_isl_biz['GL_Code_'].isna())].fillna(0)
  dic_inc_isl_biz1 = dic_inc_isl_biz1.iloc[np.where(~dic_inc_isl_biz1.GL_Description_2.isin(['Forex loss/gain realised','Forex loss/gain unrealised']))]
  dic_inc_isl_biz1.GL_Code_ = dic_inc_isl_biz1.GL_Code_.astype(int)
  dic_inc_isl_biz1.GL_Code_ = dic_inc_isl_biz1.GL_Code_.astype(str)
  #dic_inc_isl_biz1 = dic_inc_isl_biz1.drop_duplicates('GL_Code_', keep='first')

  IncIslBiz = dic_inc_isl_biz1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(month)]],on=['GL_Code_'],how='left').fillna(0)
  IncIslBiz['YTD '+str(year)+"-"+str(month)] = IncIslBiz['YTD '+str(year)+"-"+str(month)]*-1

  IncIslBiz_P = dic_inc_isl_biz1.merge(Income_prev_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(int(month-1))]],on=['GL_Code_'],how='left').fillna(0)
  IncIslBiz_P['YTD '+str(year)+"-"+str(int(month-1))] = IncIslBiz_P['YTD '+str(year)+"-"+str(int(month-1))]*-1

  #unwind
  IncIslBiz.loc[IncIslBiz.GL_Code_ == '5500306' , 'GL_Description_2'] = 'Other Income'
  IncIslBiz1 = IncIslBiz.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index() #,'Business_Unit

  #unwind_P
  IncIslBiz_P.loc[IncIslBiz_P.GL_Code_ == '5500306' , 'GL_Description_2'] = 'Other Income'
  IncIslBiz1_P = IncIslBiz_P.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(int(month-1))]].sum().reset_index() #,'Business_Unit

  #----------------------------------------------Other Income-------------------------------------------------------------

  dic_oth_inc1 = dic_oth_inc.iloc[np.where(~dic_oth_inc['GL_Code_'].isna())].fillna(0)
  dic_oth_inc1.GL_Code_ = dic_oth_inc1.GL_Code_.astype(int)
  dic_oth_inc1.GL_Code_ = dic_oth_inc1.GL_Code_.astype(str)
  #dic_inc_isl_biz1 = dic_inc_isl_biz1.drop_duplicates('GL_Code_', keep='first')

  OthInc = dic_oth_inc1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(month)]],on=['GL_Code_'],how='left').fillna(0)
  OthInc['YTD '+str(year)+"-"+str(month)] = OthInc['YTD '+str(year)+"-"+str(month)]*-1
  OthInc1 = OthInc.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index() #,'Business_Unit

  OthInc_P = dic_oth_inc1.merge(Income_prev_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(int(month-1))]],on=['GL_Code_'],how='left').fillna(0)
  OthInc_P['YTD '+str(year)+"-"+str(int(month-1))] = OthInc_P['YTD '+str(year)+"-"+str(int(month-1))]*-1
  OthInc1_P = OthInc_P.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(int(month-1))]].sum().reset_index() #,'Business_Unit


  appendnew = pd.concat([newdf, UndwrTkfl1, IncIslBiz1, OthInc1] )
  appendnew.set_index('Class', inplace=True)
  la = appendnew.T
  la['Net Income'] = la['Net Interest Income'] + la['Underwriting/Takaful results'] + la['Income from Islamic business'] + la['Other income']
  la1 = la.T
  newdf1 =la1.reset_index()

  appendnew_P = pd.concat([newdf_P, UndwrTkfl1_P, IncIslBiz1_P, OthInc1_P] )
  appendnew_P.set_index('Class', inplace=True)
  la_P = appendnew_P.T
  la_P['Net Income'] = la_P['Net Interest Income'] + la_P['Underwriting/Takaful results'] + la_P['Income from Islamic business'] + la_P['Other income']
  la1_P = la_P.T
  newdf1_P = la1_P.reset_index()

  #----------------------------------------------Overhead expenses-------------------------------------------------------------

  dic_ovh_exp1 = dic_ovh_exp.iloc[np.where(~dic_ovh_exp['GL_Code_'].isna())].fillna(0)
  dic_ovh_exp1.GL_Code_ = dic_ovh_exp1.GL_Code_.astype(int)
  dic_ovh_exp1.GL_Code_ = dic_ovh_exp1.GL_Code_.astype(str)
  dic_ovh_exp1 = dic_ovh_exp1.drop_duplicates('GL_Code_', keep='last')

  OvhExp = dic_ovh_exp1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(month)]],on=['GL_Code_'],how='left').fillna(0)
  OvhExp['YTD '+str(year)+"-"+str(month)] = OvhExp['YTD '+str(year)+"-"+str(month)]*-1
  OvhExp1 = OvhExp.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index() #,'Business_Unit

  OvhExp_P = dic_ovh_exp1.merge(Income_prev_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(int(month-1))]],on=['GL_Code_'],how='left').fillna(0)
  OvhExp_P['YTD '+str(year)+"-"+str(int(month-1))] = OvhExp_P['YTD '+str(year)+"-"+str(int(month-1))]*-1
  OvhExp1_P = OvhExp_P.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(int(month-1))]].sum().reset_index() #,'Business_Unit

  appendnew1 = pd.concat([newdf1, OvhExp1] )
  appendnew1.set_index('Class', inplace=True)
  laa = appendnew1.T
  laa['Operating profit/loss'] = laa['Net Income'] + laa['Overhead expenses']
  laa1 = laa.T
  newdf2 =laa1.reset_index()

  appendnew1_P = pd.concat([newdf1_P, OvhExp1_P] )
  appendnew1_P.set_index('Class', inplace=True)
  laa_P = appendnew1_P.T
  laa_P['Operating profit/loss'] = laa_P['Net Income'] + laa_P['Overhead expenses']
  laa1_P = laa_P.T
  newdf2_P = laa1_P.reset_index()

  #----------------------------------------------Allowances for losses on loans & financing -------------------------------------------------------------

  dic_allw_laf1 = dic_allw_laf.iloc[np.where(~dic_allw_laf['GL_Code_'].isna())].fillna(0)
  dic_allw_laf1.GL_Code_ = dic_allw_laf1.GL_Code_.astype(int)
  dic_allw_laf1.GL_Code_ = dic_allw_laf1.GL_Code_.astype(str)
  #dic_inc_isl_biz1 = dic_inc_isl_biz1.drop_duplicates('GL_Code_', keep='first')

  AllwLaf = dic_allw_laf1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(month)]],on=['GL_Code_'],how='left').fillna(0)
  AllwLaf['YTD '+str(year)+"-"+str(month)] = AllwLaf['YTD '+str(year)+"-"+str(month)]*-1
  AllwLaf1 = AllwLaf.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index() #,'Business_Unit

  AllwLaf_P = dic_allw_laf1.merge(Income_prev_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(int(month-1))]],on=['GL_Code_'],how='left').fillna(0)
  AllwLaf_P['YTD '+str(year)+"-"+str(int(month-1))] = AllwLaf_P['YTD '+str(year)+"-"+str(int(month-1))]*-1
  AllwLaf1_P = AllwLaf_P.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(int(month-1))]].sum().reset_index() #,'Business_Unit

  #----------------------------------------------Allowance for diminution in value of investment in subsidiaries  -------------------------------------------------------------

  dic_allw_dim1 = dic_allw_dim.iloc[np.where(~dic_allw_dim['GL_Code_'].isna())].fillna(0)
  dic_allw_dim1.GL_Code_ = dic_allw_dim1.GL_Code_.astype(int)
  dic_allw_dim1.GL_Code_ = dic_allw_dim1.GL_Code_.astype(str)
  #dic_inc_isl_biz1 = dic_inc_isl_biz1.drop_duplicates('GL_Code_', keep='first')

  AllwDim = dic_allw_dim1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(month)]],on=['GL_Code_'],how='left').fillna(0)
  AllwDim['YTD '+str(year)+"-"+str(month)] = AllwDim['YTD '+str(year)+"-"+str(month)]*-1
  AllwDim1 = AllwDim.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index() #,'Business_Unit

  AllwDim_P = dic_allw_dim1.merge(Income_prev_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(int(month-1))]],on=['GL_Code_'],how='left').fillna(0)
  AllwDim_P['YTD '+str(year)+"-"+str(int(month-1))] = AllwDim_P['YTD '+str(year)+"-"+str(int(month-1))]*-1
  AllwDim1_P = AllwDim_P.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(int(month-1))]].sum().reset_index() #,'Business_Unit

  #----------------------------------------------Allowance for commitments and contingencies  -------------------------------------------------------------

  dic_allw_cnc1 = dic_allw_cnc.iloc[np.where(~dic_allw_cnc['GL_Code_'].isna())].fillna(0)
  dic_allw_cnc1.GL_Code_ = dic_allw_cnc1.GL_Code_.astype(int)
  dic_allw_cnc1.GL_Code_ = dic_allw_cnc1.GL_Code_.astype(str)
  #dic_inc_isl_biz1 = dic_inc_isl_biz1.drop_duplicates('GL_Code_', keep='first')

  AllwCnC = dic_allw_cnc1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(month)]],on=['GL_Code_'],how='left').fillna(0)
  AllwCnC['YTD '+str(year)+"-"+str(month)] = AllwCnC['YTD '+str(year)+"-"+str(month)]*-1
  AllwCnC1 = AllwCnC.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index() #,'Business_Unit

  AllwCnC_P = dic_allw_cnc1.merge(Income_prev_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(int(month-1))]],on=['GL_Code_'],how='left').fillna(0)
  AllwCnC_P['YTD '+str(year)+"-"+str(int(month-1))] = AllwCnC_P['YTD '+str(year)+"-"+str(int(month-1))]*-1
  AllwCnC1_P = AllwCnC_P.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(int(month-1))]].sum().reset_index() #,'Business_Unit

  #----------------------------------------------Allowance on investment securities  -------------------------------------------------------------

  dic_allw_invsec1 = dic_allw_invsec.iloc[np.where(~dic_allw_invsec['GL_Code_'].isna())].fillna(0)
  dic_allw_invsec1.GL_Code_ = dic_allw_invsec1.GL_Code_.astype(int)
  dic_allw_invsec1.GL_Code_ = dic_allw_invsec1.GL_Code_.astype(str)
  #dic_inc_isl_biz1 = dic_inc_isl_biz1.drop_duplicates('GL_Code_', keep='first')

  AllwInvSec = dic_allw_invsec1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(month)]],on=['GL_Code_'],how='left').fillna(0)
  AllwInvSec['YTD '+str(year)+"-"+str(month)] = AllwInvSec['YTD '+str(year)+"-"+str(month)]*-1
  AllwInvSec1 = AllwInvSec.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index() #,'Business_Unit

  AllwInvSec_P = dic_allw_invsec1.merge(Income_prev_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(int(month-1))]],on=['GL_Code_'],how='left').fillna(0)
  AllwInvSec_P['YTD '+str(year)+"-"+str(int(month-1))] = AllwInvSec_P['YTD '+str(year)+"-"+str(int(month-1))]*-1
  AllwInvSec1_P = AllwInvSec_P.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(int(month-1))]].sum().reset_index() #,'Business_Unit

  #---------------------------------------------General allowance -Sundry debtors-------------------------------------------------------------

  dic_allw_sundry1 = dic_allw_sundry.iloc[np.where(~dic_allw_sundry['GL_Code_'].isna())].fillna(0)
  dic_allw_sundry1.GL_Code_ = dic_allw_sundry1.GL_Code_.astype(int)
  dic_allw_sundry1.GL_Code_ = dic_allw_sundry1.GL_Code_.astype(str)
  #dic_inc_isl_biz1 = dic_inc_isl_biz1.drop_duplicates('GL_Code_', keep='first')

  AllwInvSun = dic_allw_sundry1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(month)]],on=['GL_Code_'],how='left').fillna(0)
  AllwInvSun['YTD '+str(year)+"-"+str(month)] = AllwInvSun['YTD '+str(year)+"-"+str(month)]*-1
  AllwInvSun1 = AllwInvSun.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index() #,'Business_Unit

  AllwInvSun_P = dic_allw_sundry1.merge(Income_prev_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(int(month-1))]],on=['GL_Code_'],how='left').fillna(0)
  AllwInvSun_P['YTD '+str(year)+"-"+str(int(month-1))] = AllwInvSun_P['YTD '+str(year)+"-"+str(int(month-1))]*-1
  AllwInvSun1_P = AllwInvSun_P.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(int(month-1))]].sum().reset_index() #,'Business_Unit


  appendnew2 = pd.concat([newdf2, AllwLaf1, AllwDim1, AllwCnC1, AllwInvSec1, AllwInvSun1] )
  appendnew2.set_index('Class', inplace=True)
  laaa = appendnew2.T
  laaa['Profit/Loss before taxation'] = laaa['Operating profit/loss'] + laaa['Allowances for losses on loans & financing']+ laaa['Allowance for diminution in value of investment in subsidiaries ']+ laaa['Allowance for commitments and contingencies']+ laaa['Allowance on investment securities']+ laaa['General allowance -Sundry debtors']
  laaa1 = laaa.T
  newdf3 =laaa1.reset_index()

  appendnew2_P = pd.concat([newdf2_P, AllwLaf1_P, AllwDim1_P, AllwCnC1_P, AllwInvSec1_P, AllwInvSun1_P] )
  appendnew2_P.set_index('Class', inplace=True)
  laaa_P = appendnew2_P.T
  laaa_P['Profit/Loss before taxation'] = laaa_P['Operating profit/loss'] + laaa_P['Allowances for losses on loans & financing']+ laaa_P['Allowance for diminution in value of investment in subsidiaries ']+ laaa_P['Allowance for commitments and contingencies']+ laaa_P['Allowance on investment securities']+ laaa_P['General allowance -Sundry debtors']
  laaa1_P = laaa_P.T
  newdf3_P = laaa1_P.reset_index()

  #---------------------------------------------Less: Surplus attributable from Takaful Participants-------------------------------------------------------------

  dic_sur_tkfl1 = dic_sur_tkfl.iloc[np.where(~dic_sur_tkfl['GL_Code_'].isna())].fillna(0)
  #dic_sur_tkfl1.GL_Code_ = dic_sur_tkfl1.GL_Code_.astype(int)
  dic_sur_tkfl1.GL_Code_ = dic_sur_tkfl1.GL_Code_.astype(str)
  #dic_inc_isl_biz1 = dic_inc_isl_biz1.drop_duplicates('GL_Code_', keep='first')

  SurTfkl = dic_sur_tkfl1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(month)]],on=['GL_Code_'],how='left').fillna(0)
  #SurTfkl['YTD '+str(year)+"-"+str(month)] = SurTfkl['YTD '+str(year)+"-"+str(month)]*-1
  SurTfkl1 = SurTfkl.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index() #,'Business_Unit

  SurTfkl_P = dic_sur_tkfl1.merge(Income_prev_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(int(month-1))]],on=['GL_Code_'],how='left').fillna(0)
  #SurTfkl['YTD '+str(year)+"-"+str(month)] = SurTfkl['YTD '+str(year)+"-"+str(month)]*-1
  SurTfkl1_P = SurTfkl_P.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(int(month-1))]].sum().reset_index() #,'Business_Unit

  #---------------------------------------------Taxation-------------------------------------------------------------

  tax1 = tax.iloc[np.where(~tax['GL_Code_'].isna())].fillna(0)
  tax1.GL_Code_ = tax1.GL_Code_.astype(int)
  tax1.GL_Code_ = tax1.GL_Code_.astype(str)
  #dic_inc_isl_biz1 = dic_inc_isl_biz1.drop_duplicates('GL_Code_', keep='first')

  TAXX = tax1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(month)]],on=['GL_Code_'],how='left').fillna(0)
  TAXX['YTD '+str(year)+"-"+str(month)] = TAXX['YTD '+str(year)+"-"+str(month)]*-1

  TAXX_P = tax1.merge(Income_prev_raw1[['Item','GL_Code_','YTD '+str(year)+"-"+str(int(month-1))]],on=['GL_Code_'],how='left').fillna(0)
  TAXX_P['YTD '+str(year)+"-"+str(int(month-1))] = TAXX_P['YTD '+str(year)+"-"+str(int(month-1))]*-1

  #dividen expense
  TAXX = TAXX.iloc[np.where(TAXX.GL_Code_!="530001")]
  TAXX1 = TAXX.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index() #,'Business_Unit
  
  #dividen expense_P
  TAXX_P = TAXX_P.iloc[np.where(TAXX_P.GL_Code_!="530001")]
  TAXX1_P = TAXX_P.fillna(0).groupby(['Class'])[['YTD '+str(year)+"-"+str(int(month-1))]].sum().reset_index() #,'Business_Unit


  appendnew3 = pd.concat([newdf3, SurTfkl1, TAXX1] )
  appendnew3.set_index('Class', inplace=True)

  appendnew3_P = pd.concat([newdf3_P, SurTfkl1_P, TAXX1_P] )
  appendnew3_P.set_index('Class', inplace=True)


  laaaa = appendnew3.T
  laaaa['Net Profit/Loss fo the year'] = laaaa['Profit/Loss before taxation'] + laaaa['Less: Surplus attributable from Takaful Participants']+\
  laaaa['Taxation']+ laaaa['Zakat']
  laaaa1 = laaaa.T
  newdf4 =laaaa1.reset_index()
  newdf4.rename(columns={'Class':'Income Statement'}, inplace=True)

  laaaa_P = appendnew3_P.T
  laaaa_P['Net Profit/Loss fo the year'] = laaaa_P['Profit/Loss before taxation'] + laaaa_P['Less: Surplus attributable from Takaful Participants']+\
  laaaa_P['Taxation']+ laaaa_P['Zakat']
  laaaa1_P = laaaa_P.T
  newdf4_P =laaaa1_P.reset_index()
  newdf4_P.rename(columns={'Class':'Income Statement'}, inplace=True)


  newdf_comb = newdf4.merge(newdf4_P, on="Income Statement", how='left')
  newdf_comb["FTM "+str(year)+"-"+str(month)] = newdf_comb['YTD '+str(year)+"-"+str(month)] - newdf_comb['YTD '+str(year)+"-"+str(int(month-1))]

  st.write("Income Statement - Overall: ")
  st.write(newdf_comb)
  #st.write(newdf4)
  #st.write(newdf4_P)


  #  st.write(Income_curr_raw['Item'].value_counts())

  st.download_button("Download CSV",
                   newdf_comb.to_csv(index=False),
                   file_name='Income Statement - Overall '+str(year)+"-"+str(month)+'.csv',
                   mime='text/csv')
  
  #---------------------------------------------Details/PowerBI-------------------------------------------------------------

  OpRev1_BI = OpRev.rename(columns={'Business_Unit':'GL_Description_2'})[['GL_Description','GL_Code_','GL_Category','GL_Description_2','Class','Item','YTD '+str(year)+"-"+str(month),'Business_Category']]
  IntInc['Business_Category'] = 'NA'
  IntExp['Business_Category'] = 'NA'
  UndwrTkfl['Business_Category'] = 'NA'
  IncIslBiz['Business_Category'] = 'NA'
  IncIslBiz.loc[IncIslBiz.GL_Description_2.isin(['Banking','Other Income','Financing cost','Wakalah fee']),"Business_Category"] = 'Islamic'
  OthInc['Business_Category'] = 'NA'
  #.drop('GL_Category',axis=1)
  OvhExpBI = OvhExp.rename(columns={'Class_2':'Business_Category'})[['GL_Description',
  'GL_Code_','GL_Category','GL_Description_2','Class','Item','YTD '+str(year)+"-"+str(month),'Business_Category']]
  #OvhExp1 = OvhExp.drop('GL_Category',axis=1).rename(columns={'Class_2':'GL_Description_2','GL_Description_2':'GL_Category'})[['GL_Description','GL_Code_','GL_Category','GL_Description_2','Class','Item','YTD '+str(Income_curr[21:]),'Business_Category']]
  AllwLaf['Business_Category'] = 'NA'
  AllwDim['Business_Category'] = 'NA'
  AllwCnC['Business_Category'] = 'NA'
  AllwInvSec['Business_Category'] = 'NA'
  AllwInvSun['Business_Category'] = 'NA'
  SurTfkl['Business_Category'] = 'NA'
  TAXX['Business_Category'] = 'NA'
  PnL_BI = pd.concat([OpRev1_BI,IntInc,IntExp,UndwrTkfl,IncIslBiz,OthInc,OvhExpBI,AllwLaf,AllwDim,AllwCnC,AllwInvSec,AllwInvSun,SurTfkl,TAXX])
  PnL_BI.loc[(PnL_BI.Item.isin(['EXIB','EXTF']))|(PnL_BI.Business_Category.isin(['Islamic'])),'Type of Financing'] = "Islamic"
  PnL_BI.loc[(PnL_BI.GL_Code_.isin(['5520003'])),'Type of Financing'] = "Islamic" 
  PnL_BI.loc[(PnL_BI.Item.isin(['EXIM'])),'Type of Financing'] = "Conventional"
  PnL_BI.loc[(PnL_BI.GL_Code_.isin(['5520001'])),'Type of Financing'] = "Conventional"

  OpRev1_BI_P = OpRev_P.rename(columns={'Business_Unit':'GL_Description_2'})[['GL_Description','GL_Code_','GL_Category','GL_Description_2','Class','Item','YTD '+str(year)+"-"+str(int(month-1)),'Business_Category']]
  IntInc_P['Business_Category'] = 'NA'
  IntExp_P['Business_Category'] = 'NA'
  UndwrTkfl_P['Business_Category'] = 'NA'
  IncIslBiz_P['Business_Category'] = 'NA'
  IncIslBiz_P.loc[IncIslBiz_P.GL_Description_2.isin(['Banking','Other Income','Financing cost','Wakalah fee']),"Business_Category"] = 'Islamic'
  OthInc_P['Business_Category'] = 'NA'
  #.drop('GL_Category',axis=1)
  OvhExpBI_P = OvhExp_P.rename(columns={'Class_2':'Business_Category'})[['GL_Description',
  'GL_Code_','GL_Category','GL_Description_2','Class','Item','YTD '+str(year)+"-"+str(int(month-1)),'Business_Category']]
  #OvhExp1 = OvhExp.drop('GL_Category',axis=1).rename(columns={'Class_2':'GL_Description_2','GL_Description_2':'GL_Category'})[['GL_Description','GL_Code_','GL_Category','GL_Description_2','Class','Item','YTD '+str(Income_curr[21:]),'Business_Category']]
  AllwLaf_P['Business_Category'] = 'NA'
  AllwDim_P['Business_Category'] = 'NA'
  AllwCnC_P['Business_Category'] = 'NA'
  AllwInvSec_P['Business_Category'] = 'NA'
  AllwInvSun_P['Business_Category'] = 'NA'
  SurTfkl_P['Business_Category'] = 'NA'
  TAXX_P['Business_Category'] = 'NA'
  PnL_BI_P = pd.concat([OpRev1_BI_P,IntInc_P,IntExp_P,UndwrTkfl_P,IncIslBiz_P,OthInc_P,OvhExpBI_P,AllwLaf_P,AllwDim_P,AllwCnC_P,AllwInvSec_P,AllwInvSun_P,SurTfkl_P,TAXX_P])
  PnL_BI_P.loc[(PnL_BI_P.Item.isin(['EXIB','EXTF']))|(PnL_BI_P.Business_Category.isin(['Islamic'])),'Type of Financing'] = "Islamic"
  PnL_BI_P.loc[(PnL_BI_P.GL_Code_.isin(['5520003'])),'Type of Financing'] = "Islamic" 
  PnL_BI_P.loc[(PnL_BI_P.Item.isin(['EXIM'])),'Type of Financing'] = "Conventional"
  PnL_BI_P.loc[(PnL_BI_P.GL_Code_.isin(['5520001'])),'Type of Financing'] = "Conventional"
  
  #---------------------------------------------Conventional-------------------------------------------------------------

  IS_Conventional = PnL_BI.fillna(0).iloc[np.where(PnL_BI['Type of Financing']=="Conventional")].groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index()#.sort_values(by='YTD '+str(year)+"-"+str(month),ascending=False)
  IS_Conventional.set_index('Class', inplace=True)
  IS_Conventional_T = IS_Conventional.T
  IS_Conventional_T['Net Interest Income'] = IS_Conventional_T['Interest Income']+\
                                         IS_Conventional_T['Interest Expense']
  IS_Conventional_T['Net Income'] = IS_Conventional_T['Net Interest Income']+\
                                         IS_Conventional_T['Underwriting/Takaful results']+\
                                         IS_Conventional_T['Other income']
  IS_Conventional_T['Operating profit/loss'] = IS_Conventional_T['Net Income']+\
                                         IS_Conventional_T['Overhead expenses']
  IS_Conventional_T['Profit/Loss before taxation'] = IS_Conventional_T['Operating profit/loss']+\
                                         IS_Conventional_T['Allowances for losses on loans & financing']+\
                                         IS_Conventional_T['Allowance on investment securities']+\
                                         IS_Conventional_T['General allowance -Sundry debtors']+\
                                         IS_Conventional_T['Allowance for commitments and contingencies']+\
                                         IS_Conventional_T['Allowance for diminution in value of investment in subsidiaries ']
  IS_Conventional_T['Net Profit/Loss fo the year'] = IS_Conventional_T['Interest Income']+\
                                         IS_Conventional_T['Interest Expense']+\
                                         IS_Conventional_T['Underwriting/Takaful results']+\
                                         IS_Conventional_T['Other income']+\
                                         IS_Conventional_T['Overhead expenses']+\
                                         IS_Conventional_T['Allowances for losses on loans & financing']+\
                                         IS_Conventional_T['Allowance on investment securities']+\
                                         IS_Conventional_T['General allowance -Sundry debtors']+\
                                         IS_Conventional_T['Allowance for commitments and contingencies']+\
                                         IS_Conventional_T['Allowance for diminution in value of investment in subsidiaries ']+\
                                         IS_Conventional_T['Taxation']#+IS_Conventional_T['Zakat']
  IS_Conventional_T = IS_Conventional_T[['Operating Revenue',
                                         'Interest Income',
                                         'Interest Expense',
                                         'Net Interest Income',
                                         'Underwriting/Takaful results',
                                         #'Income from Islamic business',
                                         'Other income',
                                         'Net Income',
                                         'Overhead expenses',
                                         'Operating profit/loss',
                                         'Allowances for losses on loans & financing',
                                         'Allowance for diminution in value of investment in subsidiaries ',
                                         'General allowance -Sundry debtors',
                                         'Allowance for commitments and contingencies',
                                         'Allowance on investment securities',
                                         'Profit/Loss before taxation',
                                         #'Less: Surplus attributable from Takaful Participants',
                                         'Taxation', #'Zakat'
                                         'Net Profit/Loss fo the year']]
  IS_Conventional_TT = IS_Conventional_T.T
  IS_Conventional_TT = IS_Conventional_TT.reset_index()
  IS_Conventional_TT.rename(columns={'Class':'Income Statement'}, inplace=True)
  #sum(IS_Conventional['YTD '+str(year)+"-"+str(month)]) - sum(IS_Conventional.iloc[np.where(IS_Conventional['Class']=="Operating Revenue")]['YTD '+str(year)+"-"+str(month)])
  
  IS_Conventional_P = PnL_BI_P.fillna(0).iloc[np.where(PnL_BI_P['Type of Financing']=="Conventional")].groupby(['Class'])[['YTD '+str(year)+"-"+str(int(month-1))]].sum().reset_index()#.sort_values(by='YTD '+str(year)+"-"+str(month),ascending=False)
  IS_Conventional_P.set_index('Class', inplace=True)
  IS_Conventional_T_P = IS_Conventional_P.T
  IS_Conventional_T_P['Net Interest Income'] = IS_Conventional_T_P['Interest Income']+\
                                         IS_Conventional_T_P['Interest Expense']
  IS_Conventional_T_P['Net Income'] = IS_Conventional_T_P['Net Interest Income']+\
                                         IS_Conventional_T_P['Underwriting/Takaful results']+\
                                         IS_Conventional_T_P['Other income']
  IS_Conventional_T_P['Operating profit/loss'] = IS_Conventional_T_P['Net Income']+\
                                         IS_Conventional_T_P['Overhead expenses']
  IS_Conventional_T_P['Profit/Loss before taxation'] = IS_Conventional_T_P['Operating profit/loss']+\
                                         IS_Conventional_T_P['Allowances for losses on loans & financing']+\
                                         IS_Conventional_T_P['Allowance on investment securities']+\
                                         IS_Conventional_T_P['General allowance -Sundry debtors']+\
                                         IS_Conventional_T_P['Allowance for commitments and contingencies']+\
                                         IS_Conventional_T_P['Allowance for diminution in value of investment in subsidiaries ']
  IS_Conventional_T_P['Net Profit/Loss fo the year'] = IS_Conventional_T_P['Interest Income']+\
                                         IS_Conventional_T_P['Interest Expense']+\
                                         IS_Conventional_T_P['Underwriting/Takaful results']+\
                                         IS_Conventional_T_P['Other income']+\
                                         IS_Conventional_T_P['Overhead expenses']+\
                                         IS_Conventional_T_P['Allowances for losses on loans & financing']+\
                                         IS_Conventional_T_P['Allowance on investment securities']+\
                                         IS_Conventional_T_P['General allowance -Sundry debtors']+\
                                         IS_Conventional_T_P['Allowance for commitments and contingencies']+\
                                         IS_Conventional_T_P['Allowance for diminution in value of investment in subsidiaries ']+\
                                         IS_Conventional_T_P['Taxation']#+IS_Conventional_T['Zakat']
  IS_Conventional_T_P = IS_Conventional_T_P[['Operating Revenue',
                                         'Interest Income',
                                         'Interest Expense',
                                         'Net Interest Income',
                                         'Underwriting/Takaful results',
                                         #'Income from Islamic business',
                                         'Other income',
                                         'Net Income',
                                         'Overhead expenses',
                                         'Operating profit/loss',
                                         'Allowances for losses on loans & financing',
                                         'Allowance for diminution in value of investment in subsidiaries ',
                                         'General allowance -Sundry debtors',
                                         'Allowance for commitments and contingencies',
                                         'Allowance on investment securities',
                                         'Profit/Loss before taxation',
                                         #'Less: Surplus attributable from Takaful Participants',
                                         'Taxation', #'Zakat'
                                         'Net Profit/Loss fo the year']]
  IS_Conventional_TT_P = IS_Conventional_T_P.T
  IS_Conventional_TT_P = IS_Conventional_TT_P.reset_index()
  IS_Conventional_TT_P.rename(columns={'Class':'Income Statement'}, inplace=True)

  IS_Conventional_TT_comb = IS_Conventional_TT.merge(IS_Conventional_TT_P, on="Income Statement", how='left')
  IS_Conventional_TT_comb["FTM "+str(year)+"-"+str(month)] = IS_Conventional_TT_comb['YTD '+str(year)+"-"+str(month)] - IS_Conventional_TT_comb['YTD '+str(year)+"-"+str(int(month-1))]


  st.write("Income Statement - Conventional: ")
  st.write(IS_Conventional_TT_comb)

  st.download_button("Download CSV",
                   IS_Conventional_TT_comb.to_csv(index=False),
                   file_name='Income Statement - Conventional '+str(year)+"-"+str(month)+'.csv',
                   mime='text/csv')
  
  #---------------------------------------------Islamic-------------------------------------------------------------

  IS_Islamic = PnL_BI.fillna(0).iloc[np.where((PnL_BI['Type of Financing']=="Islamic")|(PnL_BI.Item.isin(['EXIB'])))].groupby(['Class'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index()#.sort_values(by='YTD '+str(year)+"-"+str(month),ascending=False)
  #st.dataframe(IS_Islamic)
  IS_Islamic.set_index('Class', inplace=True)
  IS_Islamic_T = IS_Islamic.T
  IS_Islamic_T['Net Income'] = IS_Islamic_T['Income from Islamic business']+\
                                         IS_Islamic_T['Other income']
  IS_Islamic_T['Operating profit/loss'] = IS_Islamic_T['Net Income']+\
                                         IS_Islamic_T['Overhead expenses']
  IS_Islamic_T['Profit/Loss before taxation'] = IS_Islamic_T['Operating profit/loss']+\
                                         IS_Islamic_T['Allowances for losses on loans & financing']+\
                                         IS_Islamic_T['Allowance for commitments and contingencies'] #+\
                                         #IS_Islamic_T['Allowance on investment securities']
  #IS_Islamic_T['Zakat'] = 0
  IS_Islamic_T['Net Profit/Loss fo the year'] = IS_Islamic_T['Profit/Loss before taxation']#+\
                                         #IS_Islamic_T['Zakat']
  IS_Islamic_T = IS_Islamic_T[['Operating Revenue',
                                         #'Interest Income',
                                         #'Interest Expense',
                                         #'Net Interest Income',
                                         #'Underwriting/Takaful results',
                                         'Income from Islamic business',
                                         'Other income',
                                         'Net Income',
                                         'Overhead expenses',
                                         'Operating profit/loss',
                                         'Allowances for losses on loans & financing',
                                         #'Allowance for diminution in value of investment in subsidiaries ',
                                         #'General allowance -Sundry debtors',
                                         'Allowance for commitments and contingencies',
                                         #'Allowance on investment securities',
                                         'Profit/Loss before taxation',
                                         #'Less: Surplus attributable from Takaful Participants',
                                         #'Taxation',
                                         'Zakat',
                                         'Net Profit/Loss fo the year']]
  IS_Islamic_TT = IS_Islamic_T.T
  IS_Islamic_TT = IS_Islamic_TT.reset_index()
  IS_Islamic_TT.rename(columns={'Class':'Income Statement'}, inplace=True)
  #sum(IS_Conventional['YTD '+str(year)+"-"+str(month)]) - sum(IS_Conventional.iloc[np.where(IS_Conventional['Class']=="Operating Revenue")]['YTD '+str(year)+"-"+str(month)])

  IS_Islamic_P = PnL_BI_P.fillna(0).iloc[np.where((PnL_BI_P['Type of Financing']=="Islamic")|(PnL_BI_P.Item.isin(['EXIB'])))].groupby(['Class'])[['YTD '+str(year)+"-"+str((int(month-1)))]].sum().reset_index()#.sort_values(by='YTD '+str(year)+"-"+str(month),ascending=False)
  #st.dataframe(IS_Islamic)
  IS_Islamic_P.set_index('Class', inplace=True)
  IS_Islamic_T_P = IS_Islamic_P.T
  IS_Islamic_T_P['Net Income'] = IS_Islamic_T_P['Income from Islamic business']+\
                                         IS_Islamic_T_P['Other income']
  IS_Islamic_T_P['Operating profit/loss'] = IS_Islamic_T_P['Net Income']+\
                                         IS_Islamic_T_P['Overhead expenses']
  IS_Islamic_T_P['Profit/Loss before taxation'] = IS_Islamic_T_P['Operating profit/loss']+\
                                         IS_Islamic_T_P['Allowances for losses on loans & financing']+\
                                         IS_Islamic_T_P['Allowance for commitments and contingencies'] #+\
                                         #IS_Islamic_T['Allowance on investment securities']
  #IS_Islamic_T['Zakat'] = 0
  IS_Islamic_T_P['Net Profit/Loss fo the year'] = IS_Islamic_T_P['Profit/Loss before taxation']#+\
                                         #IS_Islamic_T['Zakat']
  IS_Islamic_T_P = IS_Islamic_T_P[['Operating Revenue',
                                         #'Interest Income',
                                         #'Interest Expense',
                                         #'Net Interest Income',
                                         #'Underwriting/Takaful results',
                                         'Income from Islamic business',
                                         'Other income',
                                         'Net Income',
                                         'Overhead expenses',
                                         'Operating profit/loss',
                                         'Allowances for losses on loans & financing',
                                         #'Allowance for diminution in value of investment in subsidiaries ',
                                         #'General allowance -Sundry debtors',
                                         'Allowance for commitments and contingencies',
                                         #'Allowance on investment securities',
                                         'Profit/Loss before taxation',
                                         #'Less: Surplus attributable from Takaful Participants',
                                         #'Taxation',
                                         'Zakat',
                                         'Net Profit/Loss fo the year']]
  IS_Islamic_TT_P = IS_Islamic_T_P.T
  IS_Islamic_TT_P = IS_Islamic_TT_P.reset_index()
  IS_Islamic_TT_P.rename(columns={'Class':'Income Statement'}, inplace=True)

  IS_Islamic_TT_comb = IS_Islamic_TT.merge(IS_Islamic_TT_P, on="Income Statement", how='left')
  IS_Islamic_TT_comb["FTM "+str(year)+"-"+str(month)] = IS_Islamic_TT_comb['YTD '+str(year)+"-"+str(month)] - IS_Islamic_TT_comb['YTD '+str(year)+"-"+str(int(month-1))]

  st.write("Income Statement - Islamic: ")
  st.write(IS_Islamic_TT_comb)

  st.download_button("Download CSV",
                   IS_Islamic_TT_comb.to_csv(index=False),
                   file_name='Income Statement - Islamic '+str(year)+"-"+str(month)+'.csv',
                   mime='text/csv')

  #---------------------------------------------Takaful-------------------------------------------------------------

  IS_Takaful = PnL_BI.fillna(0).iloc[np.where((PnL_BI.Item.isin(['EXTF'])))].groupby(['GL_Description_2'])[['YTD '+str(year)+"-"+str(month)]].sum().reset_index()#.sort_values(by='YTD '+str(year)+"-"+str(month),ascending=False)
  IS_Takaful.set_index('GL_Description_2', inplace=True)
  IS_Takaful_T = IS_Takaful.T
  #st.dataframe(IS_Takaful)
  #st.write(sum(IS_Takaful['YTD '+str(year)+"-"+str(month)]))
  IS_Takaful_T['Gross premium contribution'] = -1*IS_Takaful_T['Gross premium contribution']
  IS_Takaful_T['Wakalah fee'] = -1*IS_Takaful_T['Wakalah fee']
  IS_Takaful_T['Reinsurance outward'] = -1*IS_Takaful_T['Reinsurance outward']
  IS_Takaful_T['Income from recoveries'] = -1*IS_Takaful_T['Income from recoveries']
  IS_Takaful_T['Movement in premium contribution liability'] = -1*IS_Takaful_T['Movement in premium contribution liability']
  IS_Takaful_T['Movement in claim liability'] = -1*IS_Takaful_T['Movement in claim liability']
  IS_Takaful_T['Takaful fees'] = -1*IS_Takaful_T['Takaful fees']
  IS_Takaful_T['Allowance for doubtful debts'] = -1*IS_Takaful_T['Allowance for doubtful debts']
  IS_Takaful_T['Administrative expenses'] = -1*IS_Takaful_T['Administrative expenses']
  IS_Takaful_T['Income from takaful activities']=IS_Takaful_T['Gross premium contribution']+\
                                                 IS_Takaful_T['Wakalah fee']+\
                                                 IS_Takaful_T['Reinsurance outward']+\
                                                 IS_Takaful_T['Income from recoveries']+\
                                                 IS_Takaful_T['Movement in premium contribution liability']+\
                                                 IS_Takaful_T['Movement in claim liability']+\
                                                 IS_Takaful_T['Takaful fees']+\
                                                 IS_Takaful_T['Allowance for doubtful debts']
  IS_Takaful_T['Takaful fund results']= IS_Takaful_T['Income from takaful activities']+IS_Takaful_T['Administrative expenses']
  IS_Takaful_T = IS_Takaful_T[['Insurance/Takaful',
                               'Gross premium contribution',
                               'Wakalah fee',
                               'Reinsurance outward',
                               'Income from recoveries',
                               'Movement in premium contribution liability',
                               'Movement in claim liability',
                               'Takaful fees',
                               'Allowance for doubtful debts',
                               'Income from takaful activities',
                               'Administrative expenses',
                               'Takaful fund results']]
  IS_Takaful_T.rename(columns={'Insurance/Takaful':'Operating Revenue',
                               'Administrative expenses':'Bank charges'}, inplace=True)
  IS_Takaful_TT = IS_Takaful_T.T
  IS_Takaful_TT = IS_Takaful_TT.reset_index()
  IS_Takaful_TT.rename(columns={'GL_Description_2':'Income Statement'}, inplace=True)


  IS_Takaful_P = PnL_BI_P.fillna(0).iloc[np.where((PnL_BI_P.Item.isin(['EXTF'])))].groupby(['GL_Description_2'])[['YTD '+str(year)+"-"+str(int(month-1))]].sum().reset_index()#.sort_values(by='YTD '+str(year)+"-"+str(month),ascending=False)
  IS_Takaful_P.set_index('GL_Description_2', inplace=True)
  IS_Takaful_T_P = IS_Takaful_P.T
  #st.dataframe(IS_Takaful)
  #st.write(sum(IS_Takaful['YTD '+str(year)+"-"+str(month)]))
  IS_Takaful_T_P['Gross premium contribution'] = -1*IS_Takaful_T_P['Gross premium contribution']
  IS_Takaful_T_P['Wakalah fee'] = -1*IS_Takaful_T_P['Wakalah fee']
  IS_Takaful_T_P['Reinsurance outward'] = -1*IS_Takaful_T_P['Reinsurance outward']
  IS_Takaful_T_P['Income from recoveries'] = -1*IS_Takaful_T_P['Income from recoveries']
  IS_Takaful_T_P['Movement in premium contribution liability'] = -1*IS_Takaful_T_P['Movement in premium contribution liability']
  IS_Takaful_T_P['Movement in claim liability'] = -1*IS_Takaful_T_P['Movement in claim liability']
  IS_Takaful_T_P['Takaful fees'] = -1*IS_Takaful_T_P['Takaful fees']
  IS_Takaful_T_P['Allowance for doubtful debts'] = -1*IS_Takaful_T_P['Allowance for doubtful debts']
  IS_Takaful_T_P['Administrative expenses'] = -1*IS_Takaful_T_P['Administrative expenses']
  IS_Takaful_T_P['Income from takaful activities']=IS_Takaful_T_P['Gross premium contribution']+\
                                                 IS_Takaful_T_P['Wakalah fee']+\
                                                 IS_Takaful_T_P['Reinsurance outward']+\
                                                 IS_Takaful_T_P['Income from recoveries']+\
                                                 IS_Takaful_T_P['Movement in premium contribution liability']+\
                                                 IS_Takaful_T_P['Movement in claim liability']+\
                                                 IS_Takaful_T_P['Takaful fees']+\
                                                 IS_Takaful_T_P['Allowance for doubtful debts']
  IS_Takaful_T_P['Takaful fund results']= IS_Takaful_T_P['Income from takaful activities']+IS_Takaful_T_P['Administrative expenses']
  IS_Takaful_T_P = IS_Takaful_T_P[['Insurance/Takaful',
                               'Gross premium contribution',
                               'Wakalah fee',
                               'Reinsurance outward',
                               'Income from recoveries',
                               'Movement in premium contribution liability',
                               'Movement in claim liability',
                               'Takaful fees',
                               'Allowance for doubtful debts',
                               'Income from takaful activities',
                               'Administrative expenses',
                               'Takaful fund results']]
  IS_Takaful_T_P.rename(columns={'Insurance/Takaful':'Operating Revenue',
                               'Administrative expenses':'Bank charges'}, inplace=True)
  IS_Takaful_TT_P = IS_Takaful_T_P.T
  IS_Takaful_TT_P = IS_Takaful_TT_P.reset_index()
  IS_Takaful_TT_P.rename(columns={'GL_Description_2':'Income Statement'}, inplace=True)

  IS_Takaful_TT_comb = IS_Takaful_TT.merge(IS_Takaful_TT_P, on="Income Statement", how='left')
  IS_Takaful_TT_comb["FTM "+str(year)+"-"+str(month)] = IS_Takaful_TT_comb['YTD '+str(year)+"-"+str(month)] - IS_Takaful_TT_comb['YTD '+str(year)+"-"+str(int(month-1))]

  st.write("Income Statement - Takaful: ")
  st.write(IS_Takaful_TT_comb)

  st.download_button("Download CSV",
                   IS_Takaful_TT_comb.to_csv(index=False),
                   file_name='Income Statement - Takaful '+str(year)+"-"+str(month)+'.csv',
                   mime='text/csv')

  #---------------------------------------------Details-------------------------------------------------------------


  PnL_BI_comb = PnL_BI.merge(PnL_BI_P[['GL_Code_','YTD '+str(year)+"-"+str(int(month-1))]], on="GL_Code_", how='left')
  PnL_BI_comb["FTM "+str(year)+"-"+str(month)] = PnL_BI_comb['YTD '+str(year)+"-"+str(month)] - PnL_BI_comb['YTD '+str(year)+"-"+str(int(month-1))]


  st.write("Income Statement - Details: ")
  #st.write(newdf4)
  #st.write(PnL_BI_comb)

  query = st.text_input("Filter dataframe in lowercase")

  #fill in the blank

  if query:
    mask = PnL_BI_comb.applymap(lambda x: query in str(x).lower()).any(axis=1)
    PnL_BI_comb = PnL_BI_comb[mask]

  #gender_filter = st.multiselect('Nature of Business in Operating Cost', options=PnL_BI_comb.iloc[np.where(PnL_BI_comb.Class=="Operating Revenue")]['GL_Description_2'].unique(), default=PnL_BI_comb.iloc[np.where(PnL_BI_comb.Class=="Operating Revenue")]['GL_Description_2'].unique())

  data_bar = IS_Takaful_TT_comb.set_index("Income Statement")
  st.bar_chart(data_bar[["YTD "+str(year)+"-"+str(month),'YTD '+str(year)+"-"+str(int(month-1))]],
                x_label="Class",
                y_label="RM",
                color=["#8E1600","#00239c"],
                horizontal=True,
                stack=False,
                width=1000,height=500,)
  
  st.data_editor(
    PnL_BI_comb,
    hide_index=True, 
    column_order=PnL_BI_comb#("Customer Name","Status","Amount Approved / Facility Limit (MYR)")
  ) 


  st.download_button("Download CSV",
                   PnL_BI_comb.to_csv(index=False),
                   file_name='Income Statement - Details '+str(year)+"-"+str(month)+'.csv',
                   mime='text/csv')
  
  #column_name = st.selectbox('Select a column to visualize:', IS_Takaful_TT_comb.columns)
  #x = IS_Takaful_TT_comb[column_name]


  
  #fig = px.bar(IS_Takaful_TT_comb, x="Income Statement", y="FTM "+str(year)+"-"+str(month))
  #fig.update_layout(bargap=0.0075,
  #title="bike by month",
  #width=1000,
  #height=500,
  #xaxis_title="month",
  #yaxis_title="bike",
  #template="simple_white")
  #hoverlabel=dict(bgcolor="white",font_size12,font_family="Arial")

  #fig.update_traces(marker_color="#AAAAAA") #hex code for silver
  #fig.show()





