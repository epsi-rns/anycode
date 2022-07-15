import re
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Color, PatternFill, Font, Border, Alignment
from openpyxl.utils.cell import get_column_letter
from datetime import datetime

def split_quotes(header):
  header = header.replace(",\n", ',""')
  header = header.replace("\n", '')

  keys = re.split(r',(?=")', header)
  keys = [key.replace('"', '') for key in keys]
  return keys

# Master Detail Faktur Exporter Class
class FakturMD2Sheet:
  def __init__(self, filename, sheet):
    self.sheet = sheet

    # prepare header
    self.init_header_keys()
    self.init_field_type()
    self.init_sheet_style()

    # parse lines
    with open(filename) as f:
      self.lines = f.readlines()
      f.close()

  def init_header_keys(self):
    header_fk  = \
      '"FK","Kode","Ganti","Faktur","Masa","Tahun","Tanggal",' + \
      '"NPWP","Nama","Alamat","DPP","PPn","PPnBM","Keterangan",' + \
      '"FG","UM DPP","UM PPn","UM PPnBM","Referensi"'

    header_fpr = \
      '"LT","Nama","Alamat","Perekam","Wilayah","Timestamp","Hash"'

    header_of  = \
      '"OF","Kode","Nama","Satuan","Jumlah","Total",' + \
      '"Diskon","DPP","PPn","Tarif","PPnBM"'

    self.keys_fk  = split_quotes(header_fk)
    self.keys_fpr = split_quotes(header_fpr)
    self.keys_of  = split_quotes(header_of)

    self.keys_fk2 = self.keys_fk.copy()
    self.keys_fk2.insert(self.keys_fk2.index('Faktur')+1, 'Lengkap')

  def init_field_type(self):
    self.keys_fk_int   = ["Masa", "Tahun", "Faktur", "NPWP"]
    self.keys_fk_money = ["DPP", "PPn", "PPnBM", \
                          "UM DPP", "UM PPn", "UM PPnBM"]
    self.keys_fk_date  = ["Tanggal"]

    self.keys_fpr_date = ["Timestamp"]

    self.keys_of_money = ["Satuan", "Total", "Diskon", "DPP", "PPn", "PPnBM"]
    self.keys_of_float = ["Jumlah", "Tarif"]

  def init_sheet_style(self):
    self.blueFill = PatternFill(
      start_color='ff4fc3f7',
      end_color='ff4fc3f7',
      fill_type='solid')

    self.headerFont = Font(name='Arial', sz='10', bold=True)
    self.normalFont = Font(name='Arial', sz='10')
    self.centerText = Alignment(horizontal='center')

  def set_column_width(self):
    # Column Width

    # 12.98 unit = 1
    wscd = self.sheet.column_dimensions
    wscd['A'].width =  4.0       # left empty ~0.31"
    wscd['B'].width =  4.0       # FK         ~0.31"
    wscd['C'].width =  5.2       # Kode       ~0.4_
    wscd['D'].width =  5.2       # Ganti      ~0.4_
    wscd['E'].width = 15.5       # Faktur     ~1.2

  def write_header(self, index, keys):
    for key in keys:
      letter  = get_column_letter(index)
      cell = self.sheet[letter + "2"]
  
      cell.value = key
      cell.fill  = self.blueFill
      cell.font  = self.headerFont
      cell.alignment = self.centerText

      index += 1

  def write_entry_fk(self, count, values):
    pairs = dict(zip(self.keys_fk, values))

    index = 2
    for key in self.keys_fk2: # with additional field (lengkap)
      letter = get_column_letter(index)
      cell = self.sheet[letter + str(count)]
      cell.font  = self.normalFont

      if key in self.keys_fk:
        value = pairs[key]

        if key in self.keys_fk_int:
          cell.value = int(value)
        elif key in self.keys_fk_money:
          cell.value = float(value)
        elif key in self.keys_fk_date:
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
      elif key in self.keys_fk_money:
        # beware of the comma or period, depend on locale
        cell.number_format = '" Rp"* #,##0.00 ;' + \
              '"-Rp"* #,##0.00 ;" Rp"* -# ;@ '

      if key=='Lengkap':
        faktur = "%013s" % pairs["Faktur"]
        faktur = faktur[:3] + '-' + faktur[3:5] + '.' + faktur[5:]
        cell.value = pairs["Kode"]+pairs["Ganti"]+"."+faktur

      index += 1

  def write_entry_fpr(self, count, values):
    pairs = dict(zip(self.keys_fpr, values))
    if "Hash" in pairs: pairs.pop("Hash") # Remove Hash

    index = 23
    for key in pairs:
      letter = get_column_letter(index)
      cell = self.sheet[letter + str(count)]
      cell.font  = self.normalFont

      value = pairs[key]
      if key in self.keys_fpr_date:
        if len(value) > 8:
          cell.value = datetime.strptime(value[0:8], "%Y%m%d")
      else:
        cell.value = value

      if key=='Timestamp':
        cell.number_format = "DD-MMM-YY;@"

      index += 1

  def write_entry_of(self, count, values):
    pairs = dict(zip(self.keys_of, values))

    index = 30
    for key in pairs:
      letter  = get_column_letter(index)
      cell = self.sheet[letter + str(count)]
      cell.font = self.normalFont

      value = pairs[key]
      if key in self.keys_of_money:
        cell.value = float(value)
      elif key in self.keys_of_float:
        cell.value = float(value)
      else:
        cell.value = value

      if key in self.keys_of_money:
        # beware of the comma or period, depend on locale
        cell.number_format = '" Rp"* #,##0.00 ;' + \
            '"-Rp"* #,##0.00 ;" Rp"* -# ;@ '

      index += 1

  def run(self):
    # write headers
    self.write_header( 2, self.keys_fk2)

    keys_fpr_slim = self.keys_fpr.copy()
    keys_fpr_slim.remove("Hash")
    self.write_header(23, keys_fpr_slim)

    self.write_header(30, self.keys_of)
    
    self.set_column_width()
    self.write_entries()

    # write entries
    count = 2

    for line in self.lines:
      count += 1

      # ignore top headers
      if (count>5):
        values = split_quotes(line)

        if values[0]=="FK":
          self.write_entry_fk(count, values)

        if values[0]=="FAPR":
          self.write_entry_fpr(count, values)

        if values[0]=="OF":
          self.write_entry_of(count, values)

def main():
  filename = 'faktur-keluaran.csv'

  wb = Workbook()
  ws = wb.active

  md = FakturMD2Sheet(filename, ws)
  md.run()

  # Save the file
  wb.save("sample.xlsx")

main()
