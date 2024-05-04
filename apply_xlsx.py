# Apply formulas to excel workbooks
import openpyxl

excel_files = ['Users/SampleData2.xlsx']

for file in excel_files:
    wb = openpyxl.load_workbook(file)
    worksheet = wb("SalesOrders")
    worksheet['G46'] = '=AVERAGE(G3:G45)'
    wb.save(file)
