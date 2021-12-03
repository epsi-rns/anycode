import openpyxl
from openpyxl import load_workbook

wb = load_workbook('./monthly/01-BS.xlsx')

for sheet in wb.worksheets:
    print(sheet.title)
