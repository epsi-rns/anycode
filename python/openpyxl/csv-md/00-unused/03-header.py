import re
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Color, PatternFill, Font, Border, Alignment

wb = Workbook()
ws = wb.active

blueFill = PatternFill(
  start_color='ff4fc3f7',
  end_color='ff4fc3f7',
  fill_type='solid')

headerFont = Font(name='Arial', sz='10', bold=True)
centerText = Alignment(horizontal='center')

# Column Width

# 12.98 unit = 1
wscd = ws.column_dimensions
wscd['A'].width =  4.0       # left empty ~0.31"
wscd['B'].width =  4.0       # FK         ~0.31"
wscd['C'].width =  5.2       # Kode       ~0.4_
wscd['D'].width =  5.2       # Ganti      ~0.4_
wscd['E'].width = 15.5       # Faktur     ~1.2

# prepare header

header = '"FK","Kode","Ganti","Faktur","Masa","Tahun","Tanggal",' + \
         '"NPWP","Nama","Alamat","DPP,"PPn","PPnBM","Keterangan",' + \
         '"FG","UM DPP","UM PPn","UM PPnBM","Referensi"'

# keys = header.split('",')
keys = re.split(r',(?=")', header)
keys = [key.replace('"', '') for key in keys]

index = 2
for key in keys:
  letter  = openpyxl.utils.cell.get_column_letter(index)
  cell = ws[letter + "2"]
  
  cell.value = key
  cell.fill  = blueFill
  cell.font  = headerFont
  cell.alignment = centerText

  index += 1

# Save the file
wb.save("sample.xlsx")

