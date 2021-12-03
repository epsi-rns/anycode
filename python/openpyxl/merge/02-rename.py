import openpyxl
from openpyxl import load_workbook

wb = load_workbook('./monthly/01-BS.xlsx')

# Rename first sheet
sheet = wb.worksheets[0] 
sheet.title = '01 - Balance Sheet'

# Save the file
wb.save("sample.xlsx")
