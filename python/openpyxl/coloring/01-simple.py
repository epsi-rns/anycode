import openpyxl
from openpyxl import load_workbook
from openpyxl.styles import Color, PatternFill, Font, Border

wb = load_workbook('combined.xlsx')
ws = wb["Combined"]

b3 = ws['B3']
c3 = ws['C3']

print(b3.value)
print(c3.value)

redFill = PatternFill(
  start_color='FFFF0000',
  end_color='FFFF0000',
  fill_type='solid')

ws['c3'].fill = redFill

# Save the file
wb.save("sample.xlsx")



