import openpyxl
from openpyxl import load_workbook
from openpyxl import Workbook

wb_dest   = load_workbook('./empty.xlsx')
wb_source = load_workbook('./monthly/01-BS.xlsx')

# Rename first sheet
sheet = wb_source.worksheets[0] 
sheet.title = '01-BS'

sheet._parent = wb_dest
wb_dest._add_sheet(sheet)

# Save the file
wb_dest.save("sample.xlsx")
