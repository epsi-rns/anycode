import openpyxl
from openpyxl import load_workbook

wb = load_workbook('monthly.xlsx')

total = len(wb.worksheets)
print("Total %d sheet(s)." % total)

for index, sheet in enumerate(wb.worksheets, start=1):
  print("%2d: %s" % (index, sheet.title))
