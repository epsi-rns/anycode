import re
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Color, PatternFill, Font, Border, Alignment
from openpyxl.utils.cell import get_column_letter

def split_quotes(header):
  keys = re.split(r',(?=")', header)
  return [key.replace('"', '') for key in keys]

# Master Detail Faktur Exporter Class
class FakturMD2Sheet:
  def __init__(self, filename, sheet):
    self.sheet = sheet

    # prepare header
    self.init_header_keys()
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

    self.keys_fk  = split_quotes(header_fk)

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

  def write_header(self):
    index = 2
    for key in self.keys_fk:
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
    for key in pairs:
      letter  = get_column_letter(index)
      cell = self.sheet[letter + str(count)]
      cell.value = pairs[key]
      cell.font  = self.normalFont
      index += 1

  def write_entries(self):
    count = 2

    for line in self.lines:
      count += 1

      # ignore top headers
      if (count>5):
        values = split_quotes(line)

        if values[0]=="FK":
          print(f'line {count}:\n{line}') 
          self.write_entry_fk(count, values)

  def run(self):
    self.write_header()
    self.set_column_width()
    self.write_entries()

def main():
  filename = 'faktur-keluaran.csv'

  wb = Workbook()
  ws = wb.active

  md = FakturMD2Sheet(filename, ws)
  md.run()

  # Save the file
  wb.save("sample.xlsx")

main()
