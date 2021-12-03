import openpyxl
from openpyxl import load_workbook

wb = load_workbook('./10-15-b5/b5-136.xlsx')

# Rename first sheet
sheet = wb.worksheets[0] 
sheet.title = 'b5-136'

# Save the file
wb.save("sample.xlsx")



