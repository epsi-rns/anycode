import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Color, PatternFill, Font, Border
from datetime import datetime

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

header_fk  = \
    '"FK","Kode","Ganti","Faktur","Masa","Tahun","Tanggal",' + \
    '"NPWP","Nama","Alamat","DPP","PPn","PPnBM","Keterangan",' + \
    '"FG","UM DPP","UM PPn","UM PPnBM","Referensi"'

keys_fk  = header_fk.split('",')
keys_fk  = [key.replace('"', '') for key in keys_fk]

keys_fk2 = keys_fk.copy()
keys_fk2.insert(keys_fk2.index('Faktur')+1, 'Lengkap')

keys_fk_int   = ["Masa", "Tahun", "Faktur", "NPWP"]
keys_fk_money = ["DPP", "PPn", "PPnBM", "UM DPP", "UM PPn", "UM PPnBM"]
keys_fk_date  = ["Tanggal"]

# Print Header: Faktur Keluaran

index = 2
for key in keys_fk2:
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

  if (count>5):
    values = line.split('",')
    values = [value.replace('"', '') for value in values]

    if values[0]=="FK":
      pairs = dict(zip(keys_fk, values))

      index = 2
      for key in keys_fk2: # with additional field (lengkap)
        letter = openpyxl.utils.cell.get_column_letter(index)
        cell = ws[letter + str(count)]
        cell.font  = normalFont

        if key in keys_fk:
          value = pairs[key]

          if key in keys_fk_int:
            cell.value = int(value)
          elif key in keys_fk_money:
            cell.value = float(value)
          elif key in keys_fk_date:
            cell.value = datetime.strptime(value, "%d/%m/%Y")
          else:
            cell.value = value

        if key=='Kode':
          cell.number_format = "00"
        elif key=='NPWP':
          cell.number_format = "00\.000\.000\.0-000\.000"
        elif key=='Faktur':
          cell.number_format = "000-00\.00000000"
        elif key=='Tanggal':
          cell.number_format = "DD-MMM-YY;@"
        elif key in keys_fk_money:
          cell.number_format = '" Rp"* #.##0,00 ;"-Rp"* #.##0,00 ;" Rp"* -# ;@ '

        if key=='Lengkap':
          faktur = "%013s" % pairs["Faktur"]
          faktur = faktur[:3] + '-' + faktur[3:5] + '.' + faktur[5:]
          cell.value = pairs["Kode"]+pairs["Ganti"]+"."+faktur

        index += 1

# Save the file
wb.save("sample.xlsx")
