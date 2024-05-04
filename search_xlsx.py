#Search in excel workbooks
import pandas as pd
import numpy as np

files = ['Users/SampleData2.xlsx']

for file in files:
    df = pd.read_excel(file)
    pencil = df['Rep'].where(df['Item'] == 'Pencil').dropna()
    print(file)
    print(pencil)
