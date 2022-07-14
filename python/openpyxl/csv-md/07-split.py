import re
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Color, PatternFill, Font, Border, Alignment
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

header_fpr = \
    '"LT","Nama","Alamat","Perekam","Wilayah","Timestamp","Hash"'

header_of  = \
    '"OF","Kode","Nama","Satuan","Jumlah","Total",' + \
    '"Diskon","DPP","PPn","Tarif","PPnBM"'

# keys_fk  = header_fk.split('",')
keys_fk = re.split(r',(?=")', header_fk)
keys_fk  = [key.replace('"', '') for key in keys_fk]

# keys_fpr  = header_fpr.split('",')
keys_fpr = re.split(r',(?=")', header_fpr)
keys_fpr = [key.replace('"', '') for key in keys_fpr]

# keys_of  = header_of.split('",')
keys_of  = re.split(r',(?=")', header_of)
keys_of  = [key.replace('"', '') for key in keys_of]

keys_fk2 = keys_fk.copy()
keys_fk2.insert(keys_fk2.index('Faktur')+1, 'Lengkap')

keys_fk_int   = ["Masa", "Tahun", "Faktur", "NPWP"]
keys_fk_money = ["DPP", "PPn", "PPnBM", "UM DPP", "UM PPn", "UM PPnBM"]
keys_fk_date  = ["Tanggal"]

keys_fpr_date = ["Timestamp"]

keys_of_money = ["Satuan", "Total", "Diskon", "DPP", "PPn", "PPnBM"]
keys_of_float = ["Jumlah", "Tarif"]

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
          # beware of the comma or period, depend on locale
          cell.number_format = '" Rp"* #,##0.00 ;' + \
              '"-Rp"* #,##0.00 ;" Rp"* -# ;@ '

        if key=='Lengkap':
          faktur = "%013s" % pairs["Faktur"]
          faktur = faktur[:3] + '-' + faktur[3:5] + '.' + faktur[5:]
          cell.value = pairs["Kode"]+pairs["Ganti"]+"."+faktur

        index += 1

    if values[0]=="FAPR":
      pairs = dict(zip(keys_fpr, values))
      if "Hash" in pairs: pairs.pop("Hash") # Remove Hash

      index = 23
      for key in pairs:
        letter  = openpyxl.utils.cell.get_column_letter(index)
        cell = ws[letter + str(count)]
        cell.font  = normalFont

        value = pairs[key]
        if key in keys_fpr_date:
          cell.value = datetime.strptime(value[0:8], "%Y%m%d")
        else:
          cell.value = value

        if key=='Timestamp':
          cell.number_format = "DD-MMM-YY;@"

        index += 1

    if values[0]=="OF":
      pairs = dict(zip(keys_of, values))

      index = 30
      for key in pairs:
        letter  = openpyxl.utils.cell.get_column_letter(index)
        cell = ws[letter + str(count)]
        cell.font  = normalFont

        value = pairs[key]
        if key in keys_of_money:
          cell.value = float(value)
        elif key in keys_of_float:
          cell.value = float(value)
        else:
          cell.value = value

        if key in keys_of_money:
          # beware of the comma or period, depend on locale
          cell.number_format = '" Rp"* #,##0.00 ;' + \
              '"-Rp"* #,##0.00 ;" Rp"* -# ;@ '

        index += 1

# Save the file
wb.save("sample.xlsx")
