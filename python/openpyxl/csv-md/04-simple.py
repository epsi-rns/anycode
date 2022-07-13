import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Color, PatternFill, Font, Border

filename = 'faktur-keluaran.csv'

# prepare worksheet

wb = Workbook()
ws = wb.active

blueFill = PatternFill(
  start_color='ff4fc3f7',
  end_color='ff4fc3f7',
  fill_type='solid')

headerFont = Font(name='Arial', sz='10', bold=True)
normalFont = Font(name='Arial', sz='10')

# prepare header

header = '"FK","Kode","Ganti","Faktur","Masa","Tahun","Tanggal",' + \
         '"NPWP","Nama","Alamat","DPP,"PPn","PPnBM","Keterangan",' + \
         '"FG","UM DPP","UM PPn","UM PPnBM","Referensi"'

keys = header.split('",')
keys = [key.replace('"', '') for key in keys]

index = 2
for key in keys:
  letter  = openpyxl.utils.cell.get_column_letter(index)
  cell    = ws[letter + "2"]
  
  cell.value = key
  cell.fill  = blueFill
  cell.font  = headerFont

  index += 1

# parse lines

with open(filename) as f:
  lines = f.readlines()
  f.close()

count = 2
for line in lines:
  count += 1

  if (count>3):
    values = line.split('",')
    values = [value.replace('"', '') for value in values]

    if values[0]=="FK":

      print(f'line {count}:\n{line}') 
      pairs = dict(zip(keys, values))

      index = 2
      for key in pairs:
        letter  = openpyxl.utils.cell.get_column_letter(index)
        cell = ws[letter + str(count)]
        cell.value = pairs[key]
        cell.font  = normalFont
        index += 1

# Save the file
wb.save("sample.xlsx")
