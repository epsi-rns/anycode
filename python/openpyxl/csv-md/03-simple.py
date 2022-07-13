import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Color, PatternFill, Font, Border

wb = Workbook()
ws = wb.active

blueFill = PatternFill(
  start_color='ff4fc3f7',
  end_color='ff4fc3f7',
  fill_type='solid')

headerFont = Font(name='Arial', sz='10', bold=True)

# prepare header

header = '"FK","Kode","Ganti","Faktur","Masa","Tahun","Tanggal",' + \
         '"NPWP","Nama","Alamat","DPP,"PPn","PPnBM","Keterangan",' + \
         '"FG","UM DPP","UM PPn","UM PPnBM","Referensi"'

keys = header.split('",')
keys = [key.replace('"', '') for key in keys]

index = 2
for key in keys:
  letter  = openpyxl.utils.cell.get_column_letter(index)
  cell = ws[letter + "2"]
  
  cell.value = key
  cell.fill  = blueFill
  cell.font  = headerFont

  index += 1

# Save the file
wb.save("sample.xlsx")
