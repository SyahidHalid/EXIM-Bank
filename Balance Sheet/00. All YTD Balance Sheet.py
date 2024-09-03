import pandas as pd
import numpy as np

#warnings.filterwarnings('ignore')
pd.set_option("display.max_columns", None) 
pd.set_option("display.max_colwidth", 1000) #huruf dlm column
pd.set_option("display.max_rows", 100)
pd.set_option("display.precision", 2) #2 titik perpuluhan

EXIB_name = "EXIB_July2024"
 
EXIM_name = "EXIM_July2024"

EXTF_name = "EXTF_July2024"

date_file = 202407

Income_curr = "07. Income statement Jul 2024"

Invesment_Properties_Cost = -62999998
Invesment_Properties_Accumulated_Depreciation = 9570000+(55000*int(Income_curr[:2]))
#=(1650000+(55000*12)+(55000*12)+(55000*12)+(55000*12)+(55000*12)+(55000*12)+(55000*12)+(55000*12)+(55000*12)+(55000*12)+(55000*12)+(55000*12)+(55000*Number of Month))

Location = r"C:\Users\syahidhalid\Syahid_PC\Analytics - FAD\06. Management Account\\"+str(date_file)

EXIB = pd.read_excel(str(Location)+"\\Source\\"+str(EXIB_name)+".xlsx", sheet_name=EXIB_name, header=5)
EXIB.columns = EXIB.columns.str.replace("\n", "_").str.replace(" ", "_")

EXIM = pd.read_excel(str(Location)+"\\Source\\"+str(EXIM_name)+".xlsx", sheet_name=EXIM_name, header=5)
EXIM.columns = EXIM.columns.str.replace("\n", "_").str.replace(" ", "_")

EXTF = pd.read_excel(str(Location)+"\\Source\\"+str(EXTF_name)+".xlsx", sheet_name=EXTF_name, header=5)
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

Location_dic = r"C:\\Users\\syahidhalid\\Syahid_PC\\Analytics - FAD\\06. Management Account\\Working"
file_dic = "Balance Sheet - Dictionary"

dic_Cash = pd.read_excel(str(Location_dic)+"\\"+str(file_dic)+".xlsx", sheet_name='Cash Bank', header=0)
dic_Cash.columns = dic_Cash.columns.str.replace("\n", "_").str.replace(" ", "_")

dic_Depo = pd.read_excel(str(Location_dic)+"\\"+str(file_dic)+".xlsx", sheet_name='Deposit Placement', header=0)
dic_Depo.columns = dic_Depo.columns.str.replace("\n", "_").str.replace(" ", "_")

dic_InvSec = pd.read_excel(str(Location_dic)+"\\"+str(file_dic)+".xlsx", sheet_name='Investment Securities', header=0)
dic_InvSec.columns = dic_InvSec.columns.str.replace("\n", "_").str.replace(" ", "_")

dic_ECR = pd.read_excel(str(Location_dic)+"\\"+str(file_dic)+".xlsx", sheet_name='ECR', header=0)
dic_ECR.columns = dic_ECR.columns.str.replace("\n", "_").str.replace(" ", "_")

dic_LAF = pd.read_excel(str(Location_dic)+"\\"+str(file_dic)+".xlsx", sheet_name='LAF', header=0)
dic_LAF.columns = dic_LAF.columns.str.replace("\n", "_").str.replace(" ", "_")

dic_InsReceivables = pd.read_excel(str(Location_dic)+"\\"+str(file_dic)+".xlsx", sheet_name='Insurance receivables', header=0)
dic_InsReceivables.columns = dic_InsReceivables.columns.str.replace("\n", "_").str.replace(" ", "_")

dic_Deriv = pd.read_excel(str(Location_dic)+"\\"+str(file_dic)+".xlsx", sheet_name='Derivative Asset', header=0)
dic_Deriv.columns = dic_Deriv.columns.str.replace("\n", "_").str.replace(" ", "_")

dic_Other = pd.read_excel(str(Location_dic)+"\\"+str(file_dic)+".xlsx", sheet_name='Other Assets', header=0)
dic_Other.columns = dic_Other.columns.str.replace("\n", "_").str.replace(" ", "_")

dic_InvSub = pd.read_excel(str(Location_dic)+"\\"+str(file_dic)+".xlsx", sheet_name='Investment Subsidaries', header=0)
dic_InvSub.columns = dic_InvSub.columns.str.replace("\n", "_").str.replace(" ", "_")

dic_InvShare = pd.read_excel(str(Location_dic)+"\\"+str(file_dic)+".xlsx", sheet_name='Investment in Share', header=0)
dic_InvShare.columns = dic_InvShare.columns.str.replace("\n", "_").str.replace(" ", "_")

dic_InvProp = pd.read_excel(str(Location_dic)+"\\"+str(file_dic)+".xlsx", sheet_name='Inv Properties', header=0)
dic_InvProp.columns = dic_InvProp.columns.str.replace("\n", "_").str.replace(" ", "_")

# Raw

Income_curr_raw1 = Income_curr_raw.iloc[np.where(~Income_curr_raw['GL_no.'].isna())]

Income_curr_raw1 = Income_curr_raw1[['Item','GL_no.','Unnamed:_7','Unnamed:_10']].\
    rename(columns={'GL_no.': 'GL_Code_',\
                    'Unnamed:_10':'YTD '+str(Income_curr[21:]),\
                    'Unnamed:_7':'GL_Category'}).fillna(0)

Income_curr_raw1.GL_Code_ = Income_curr_raw1.GL_Code_.astype(str)
Income_curr_raw1.GL_Category = Income_curr_raw1.GL_Category.astype(str)
Income_curr_raw1['YTD '+str(Income_curr[21:])] = Income_curr_raw1['YTD '+str(Income_curr[21:])].astype(float)

#---------------------------------------------Cash Bank------------------------------------------------------------

dic_op_rev1 = dic_Cash.iloc[np.where(~dic_Cash['GL_Code_'].isna())].fillna(0)

dic_op_rev1.GL_Code_ = dic_op_rev1.GL_Code_.astype(int)
dic_op_rev1.GL_Code_ = dic_op_rev1.GL_Code_.astype(str)

dic_op_rev1 = dic_op_rev1.drop_duplicates('GL_Code_', keep='first')

Cash = dic_op_rev1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(Income_curr[21:])]],on=['GL_Code_'],how='left',suffixes=("_Excel","_SAP")).fillna(0)

#OpRev['YTD '+str(Income_curr[21:])] = OpRev['YTD '+str(Income_curr[21:])]*-1

Cash1 = Cash.fillna(0).groupby(['Class'])[['YTD '+str(Income_curr[21:])]].sum().reset_index() #,'Business_Unit'

#print(sum(Cash1['YTD '+str(Income_curr[21:])]))

#-----------------------------------------Deposit Placement------------------------------------------------------------

dic_Depo1 = dic_Depo.iloc[np.where(~dic_Depo['GL_Code_'].isna())].fillna(0)

dic_Depo1.GL_Code_ = dic_Depo1.GL_Code_.astype(int)
dic_Depo1.GL_Code_ = dic_Depo1.GL_Code_.astype(str)

dic_Depo1 = dic_Depo1.drop_duplicates('GL_Code_', keep='first')

Depo = dic_Depo1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(Income_curr[21:])]],on=['GL_Code_'],how='left',suffixes=("_Excel","_SAP")).fillna(0)

#OpRev['YTD '+str(Income_curr[21:])] = OpRev['YTD '+str(Income_curr[21:])]*-1

Depo1 = Depo.fillna(0).groupby(['Class'])[['YTD '+str(Income_curr[21:])]].sum().reset_index() #,'Business_Unit'

#print(sum(Depo1['YTD '+str(Income_curr[21:])]))

#-----------------------------------------Invesment Security------------------------------------------------------------

dic_InvSec1 = dic_InvSec.iloc[np.where(~dic_InvSec['GL_Code_'].isna())].fillna(0)

dic_InvSec1.GL_Code_ = dic_InvSec1.GL_Code_.astype(int)
dic_InvSec1.GL_Code_ = dic_InvSec1.GL_Code_.astype(str)

dic_InvSec1 = dic_InvSec1.drop_duplicates('GL_Code_', keep='first')

InvSec = dic_InvSec1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(Income_curr[21:])]],on=['GL_Code_'],how='left',suffixes=("_Excel","_SAP")).fillna(0)

#OpRev['YTD '+str(Income_curr[21:])] = OpRev['YTD '+str(Income_curr[21:])]*-1

InvSec1 = InvSec.fillna(0).groupby(['Class'])[['YTD '+str(Income_curr[21:])]].sum().reset_index() #,'Business_Unit'

#print(sum(InvSec1['YTD '+str(Income_curr[21:])]))

#-----------------------------------------ECR------------------------------------------------------------

dic_ECR1 = dic_ECR.iloc[np.where(~dic_ECR['GL_Code_'].isna())].fillna(0)

dic_ECR1.GL_Code_ = dic_ECR1.GL_Code_.astype(int)
dic_ECR1.GL_Code_ = dic_ECR1.GL_Code_.astype(str)

dic_ECR1 = dic_ECR1.drop_duplicates('GL_Code_', keep='first')

ECR = dic_ECR1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(Income_curr[21:])]],on=['GL_Code_'],how='left',suffixes=("_Excel","_SAP")).fillna(0)

#OpRev['YTD '+str(Income_curr[21:])] = OpRev['YTD '+str(Income_curr[21:])]*-1

ECR1 = ECR.fillna(0).groupby(['Class'])[['YTD '+str(Income_curr[21:])]].sum().reset_index() #,'Business_Unit'

#print(sum(ECR1['YTD '+str(Income_curr[21:])]))

#-----------------------------------------LAF------------------------------------------------------------

dic_LAF1 = dic_LAF.iloc[np.where(~dic_LAF['GL_Code_'].isna())].fillna(0)

dic_LAF1.GL_Code_ = dic_LAF1.GL_Code_.astype(int)
dic_LAF1.GL_Code_ = dic_LAF1.GL_Code_.astype(str)

dic_LAF1 = dic_LAF1.drop_duplicates('GL_Code_', keep='first')

LAF = dic_LAF1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(Income_curr[21:])]],on=['GL_Code_'],how='left',suffixes=("_Excel","_SAP")).fillna(0)

#OpRev['YTD '+str(Income_curr[21:])] = OpRev['YTD '+str(Income_curr[21:])]*-1

LAF1 = LAF.fillna(0).groupby(['Class'])[['YTD '+str(Income_curr[21:])]].sum().reset_index() #,'Business_Unit'

#print(sum(LAF1['YTD '+str(Income_curr[21:])]))

#-----------------------------------------Insurance receivables------------------------------------------------------------

dic_InsReceivables1 = dic_InsReceivables.iloc[np.where(~dic_InsReceivables['GL_Code_'].isna())].fillna(0)

dic_InsReceivables1.GL_Code_ = dic_InsReceivables1.GL_Code_.astype(int)
dic_InsReceivables1.GL_Code_ = dic_InsReceivables1.GL_Code_.astype(str)

dic_InsReceivables1 = dic_InsReceivables1.drop_duplicates('GL_Code_', keep='first')

InsRecei = dic_InsReceivables1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(Income_curr[21:])]],on=['GL_Code_'],how='left',suffixes=("_Excel","_SAP")).fillna(0)

#OpRev['YTD '+str(Income_curr[21:])] = OpRev['YTD '+str(Income_curr[21:])]*-1

InsRecei1 = InsRecei.fillna(0).groupby(['Class'])[['YTD '+str(Income_curr[21:])]].sum().reset_index() #,'Business_Unit'

#print(sum(InsRecei1['YTD '+str(Income_curr[21:])]))

#-----------------------------------------Derivative Asset------------------------------------------------------------

dic_Deriv1 = dic_Deriv.iloc[np.where(~dic_Deriv['GL_Code_'].isna())].fillna(0)

dic_Deriv1.GL_Code_ = dic_Deriv1.GL_Code_.astype(int)
dic_Deriv1.GL_Code_ = dic_Deriv1.GL_Code_.astype(str)

dic_Deriv1 = dic_Deriv1.drop_duplicates('GL_Code_', keep='first')

Deriv = dic_Deriv1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(Income_curr[21:])]],on=['GL_Code_'],how='left',suffixes=("_Excel","_SAP")).fillna(0)

#OpRev['YTD '+str(Income_curr[21:])] = OpRev['YTD '+str(Income_curr[21:])]*-1

Deriv1 = Deriv.fillna(0).groupby(['Class'])[['YTD '+str(Income_curr[21:])]].sum().reset_index() #,'Business_Unit'

#print(sum(Deriv1['YTD '+str(Income_curr[21:])]))

#-----------------------------------------Other Assets------------------------------------------------------------

dic_Other1 = dic_Other.iloc[np.where(~dic_Other['GL_Code_'].isna())].fillna(0)

dic_Other1.GL_Code_ = dic_Other1.GL_Code_.astype(int)
dic_Other1.GL_Code_ = dic_Other1.GL_Code_.astype(str)

dic_Other1 = dic_Other1.drop_duplicates('GL_Code_', keep='first')

Other = dic_Other1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(Income_curr[21:])]],on=['GL_Code_'],how='left',suffixes=("_Excel","_SAP")).fillna(0)

#OpRev['YTD '+str(Income_curr[21:])] = OpRev['YTD '+str(Income_curr[21:])]*-1

Other1 = Other.fillna(0).groupby(['Class'])[['YTD '+str(Income_curr[21:])]].sum().reset_index() #,'Business_Unit'

#print(sum(Other1['YTD '+str(Income_curr[21:])]))

#-----------------------------------------Investment Subsidaries------------------------------------------------------------

dic_InvSub1 = dic_InvSub.iloc[np.where(~dic_InvSub['GL_Code_'].isna())].fillna(0)

dic_InvSub1.GL_Code_ = dic_InvSub1.GL_Code_.astype(int)
dic_InvSub1.GL_Code_ = dic_InvSub1.GL_Code_.astype(str)

dic_InvSub1 = dic_InvSub1.drop_duplicates('GL_Code_', keep='first')

InvSub = dic_InvSub1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(Income_curr[21:])]],on=['GL_Code_'],how='left',suffixes=("_Excel","_SAP")).fillna(0)

#OpRev['YTD '+str(Income_curr[21:])] = OpRev['YTD '+str(Income_curr[21:])]*-1

InvSub1 = InvSub.fillna(0).groupby(['Class'])[['YTD '+str(Income_curr[21:])]].sum().reset_index() #,'Business_Unit'

#print(sum(InvSub1['YTD '+str(Income_curr[21:])]))


#-----------------------------------------Investment Share------------------------------------------------------------

dic_InvShare1 = dic_InvShare.iloc[np.where(~dic_InvShare['GL_Code_'].isna())].fillna(0)

dic_InvShare1.GL_Code_ = dic_InvShare1.GL_Code_.astype(int)
dic_InvShare1.GL_Code_ = dic_InvShare1.GL_Code_.astype(str)

dic_InvShare1 = dic_InvShare1.drop_duplicates('GL_Code_', keep='first')

InvShare = dic_InvShare1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(Income_curr[21:])]],on=['GL_Code_'],how='left',suffixes=("_Excel","_SAP")).fillna(0)

#OpRev['YTD '+str(Income_curr[21:])] = OpRev['YTD '+str(Income_curr[21:])]*-1

InvShare1 = InvShare.fillna(0).groupby(['Class'])[['YTD '+str(Income_curr[21:])]].sum().reset_index() #,'Business_Unit'

#print(sum(InvShare1['YTD '+str(Income_curr[21:])]))

#-----------------------------------------Investment Properties------------------------------------------------------------

dic_InvProp1 = dic_InvProp.iloc[np.where(~dic_InvProp['GL_Code_'].isna())].fillna(0)

dic_InvProp1.GL_Code_ = dic_InvProp1.GL_Code_.astype(int)
dic_InvProp1.GL_Code_ = dic_InvProp1.GL_Code_.astype(str)

dic_InvProp1 = dic_InvProp1.drop_duplicates('GL_Code_', keep='first')

InvProp = dic_InvProp1.merge(Income_curr_raw1[['Item','GL_Code_','YTD '+str(Income_curr[21:])]],on=['GL_Code_'],how='left',suffixes=("_Excel","_SAP")).fillna(0)

#OpRev['YTD '+str(Income_curr[21:])] = OpRev['YTD '+str(Income_curr[21:])]*-1

df_add_BS10_1 = pd.DataFrame([['Cost of Building',
                        '1',
                        'Cost',
                        'Reclassified into Property & Equipment',
                        'Investment properties',
                        'EXIM',
                        Invesment_Properties_Cost]], columns=['GL_Description','GL_Code_','GL_Category','GL_Description_2','Class','Item','YTD '+str(Income_curr[21:])])

df_add_BS10_2 = pd.DataFrame([['Accumulated depreciation of Building',
                        '2',
                        'Accumulated depreciation',
                        'Reclassified into Property & Equipment',
                        'Investment properties',
                        'EXIM',
                        Invesment_Properties_Accumulated_Depreciation]], columns=['GL_Description','GL_Code_','GL_Category','GL_Description_2','Class','Item','YTD '+str(Income_curr[21:])])

InvProp = pd.concat([InvProp, df_add_BS10_1, df_add_BS10_2])

InvProp1 = InvProp.fillna(0).groupby(['Class'])[['YTD '+str(Income_curr[21:])]].sum().reset_index() #,'Business_Unit'

#print(sum(InvProp1['YTD '+str(Income_curr[21:])]))

#-----------------------------------------Intangable Asset------------------------------------------------------------


#print(sum(InvShare1['YTD '+str(Income_curr[21:])]))

