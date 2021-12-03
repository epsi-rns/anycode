import openpyxl
from openpyxl import load_workbook

wb = load_workbook('./10-15-b5/b5-136.xlsx')

for sheet in wb.worksheets:
    print(sheet.title)
