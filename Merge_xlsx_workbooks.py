#Merge excel workbooks
import pandas as pd

excel_files = ['Users/SampleData2.xlsx']

merge = pd.DataFrame()

for file in excel_files:
    df = pd.read_excel(file, skiprows = 1)
    merge = merge.append(df, ignore_index = True)

merge.to_excel('Merged_files.xlsx')
