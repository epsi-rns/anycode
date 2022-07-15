import re
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

header_fk  = \
    '"FK","Kode","Ganti","Faktur","Masa","Tahun","Tanggal",' + \
    '"NPWP","Nama","Alamat","DPP","PPn","PPnBM","Keterangan",' + \
    '"FG","UM DPP","UM PPn","UM PPnBM","Referensi"'

header_fpr = \
    '"LT","Nama","Alamat","Perekam","Wilayah","Timestamp","Hash"'

header_of  = \
    '"OF","Kode","Nama","Satuan","Jumlah","Total",' + \
    '"Diskon","DPP","PPN","Tarif","PPnBM"'

# keys_fk  = header_fk.split('",')
keys_fk  = re.split(r',(?=")', header_fk)
keys_fk  = [key.replace('"', '') for key in keys_fk]

# keys_fpr  = header_fpr.split('",')
keys_fpr = re.split(r',(?=")', header_fpr)
keys_fpr = [key.replace('"', '') for key in keys_fpr]

# keys_of  = header_of.split('",')
keys_of  = re.split(r',(?=")', header_of)
keys_of  = [key.replace('"', '') for key in keys_of]

keys_fk2 = keys_fk.copy()
keys_fk2.insert(keys_fk2.index('Faktur')+1, 'Lengkap')

# Print Header: Faktur Keluaran

index = 2
for key in keys_fk2:
  letter  = openpyxl.utils.cell.get_column_letter(index)
  cell    = ws[letter + "2"]
  
  cell.value = key
  cell.fill  = blueFill
  cell.font  = headerFont

  index += 1

# Print Header: Faktur Perekam

index = 23
key_fpr_slim = keys_fpr.remove("Hash")
for key in keys_fpr:
  letter  = openpyxl.utils.cell.get_column_letter(index)
  cell    = ws[letter + "2"]
  
  cell.value = key
  cell.fill  = blueFill
  cell.font  = headerFont

  index += 1

# Print Header: Items

index = 30
for key in keys_of:
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
    # values = line.split('",')
    values = re.split(r',(?=")', line)
    values = [value.replace('"', '') for value in values]

    if values[0]=="FK":
      pairs = dict(zip(keys_fk, values))

      index = 2
      for key in keys_fk2: # with additional field (lengkap)
        letter = openpyxl.utils.cell.get_column_letter(index)
        cell = ws[letter + str(count)]
        if key in keys_fk:
          cell.value = pairs[key]
        cell.font  = normalFont
        index += 1

    if values[0]=="FAPR":
      pairs = dict(zip(keys_fpr, values))
      if "Hash" in pairs: pairs.pop("Hash") # Remove Hash

      index = 23
      for key in pairs:
        letter  = openpyxl.utils.cell.get_column_letter(index)
        cell = ws[letter + str(count)]
        cell.value = pairs[key]
        cell.font  = normalFont
        index += 1

    if values[0]=="OF":
      pairs = dict(zip(keys_of, values))

      index = 30
      for key in pairs:
        letter  = openpyxl.utils.cell.get_column_letter(index)
        cell = ws[letter + str(count)]
        cell.value = pairs[key]
        cell.font  = normalFont
        index += 1

# Save the file
wb.save("sample.xlsx")
