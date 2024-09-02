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

Location = r"C:\Users\syahidhalid\Syahid_PC\Analytics - FAD\06. Management Account\\"+str(date_file)

EXIB = pd.read_excel(str(Location)+"\\Source\\"+str(EXIB_name)+".xlsx", sheet_name=EXIB_name, header=5)
EXIB.columns = EXIB.columns.str.replace("\n", "_").str.replace(" ", "_")

EXIM = pd.read_excel(str(Location)+"\\Source\\"+str(EXIM_name)+".xlsx", sheet_name=EXIM_name, header=5)
EXIM.columns = EXIM.columns.str.replace("\n", "_").str.replace(" ", "_")

EXTF = pd.read_excel(str(Location)+"\\Source\\"+str(EXTF_name)+".xlsx", sheet_name=EXTF_name, header=5)
EXTF.columns = EXTF.columns.str.replace("\n", "_").str.replace(" ", "_")
