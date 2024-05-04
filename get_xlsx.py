# Get values from different excel workbooks
import openpyxl

excel_files = ['Users/SampleData2.xlsx']

values = []

for file in excel_files:
    workbook = openpyxl.load_workbook(file)
    worksheet = workbook['SalesOrder']
    cell_value = worksheet['G11'].value
    values.append(cell_value)

    print(cell_value)
