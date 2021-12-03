import openpyxl
from openpyxl import load_workbook
from openpyxl import Workbook

wb_dest   = load_workbook('./empty.xlsx')
wb_source = load_workbook('./10-15-b5/b5-136.xlsx')

# Rename first sheet
sheet = wb_source.worksheets[0] 
sheet.title = 'b5-136'

sheet._parent = wb_dest
wb_dest._add_sheet(sheet)

# Save the file
wb_dest.save("sample.xlsx")
