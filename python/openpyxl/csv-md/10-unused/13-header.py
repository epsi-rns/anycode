import re
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Color, PatternFill, Font, Border, Alignment

def split_quotes(header):
  keys = re.split(r',(?=")', header)
  return [key.replace('"', '') for key in keys]

# Master Detail Faktur Exporter Class
class FakturMD2Sheet:
  def __init__(self, sheet):
    self.sheet = sheet

    # prepare header
    self.init_header_keys()
    self.init_sheet_style()

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
      letter  = openpyxl.utils.cell.get_column_letter(index)
      cell = self.sheet[letter + "2"]
  
      cell.value = key
      cell.fill  = self.blueFill
      cell.font  = self.headerFont
      cell.alignment = self.centerText

      index += 1

  def run(self):
    self.write_header()
    self.set_column_width()

def main():
  wb = Workbook()
  ws = wb.active

  md = FakturMD2Sheet(ws)
  md.run()

  # Save the file
  wb.save("sample.xlsx")

main()
