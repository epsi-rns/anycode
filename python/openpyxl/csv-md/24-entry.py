import re
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import (Color,
  PatternFill, Font, Border, Alignment)
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
    # save initial parameter
    self.filename = filename
    self.sheet = sheet

    # prepare header
    self.init_header_keys()
    self.init_field_metadata()
    self.init_sheet_style()

  def init_header_keys(self):
    header_fk  = \
      '"FK","Kode","Ganti","Faktur","Masa",' + \
      '"Tahun","Tanggal","NPWP","Nama","Alamat",' + \
      '"DPP","PPn","PPnBM","Keterangan","FG",' + \
      '"UM DPP","UM PPn","UM PPnBM","Referensi"'

    self.keys_fk   = split_quotes(header_fk)

  def init_field_metadata(self):
    self.fields_fk = {
      'FK'       : { 'col': 'B', 'width': 0.3 },
      'Kode'     : { 'col': 'C', 'width': 0.4 },
      'Ganti'    : { 'col': 'D', 'width': 0.4 },
      'Faktur'   : { 'col': 'E', 'width': 1.2, 'type': 'int' },
      'Lengkap'  : { 'col': 'F', 'width': 1.5 },
      'Masa'     : { 'col': 'G', 'width': 0.4, 'type': 'int', },
      'Tahun'    : { 'col': 'H', 'width': 0.5, 'type': 'int', },
      'Tanggal'  : { 'col': 'I', 'width': 0.8, 'type': 'date',
                     'format': 'DD-MMM-YY;@' },
      'NPWP'     : { 'col': 'J', 'width': 1.5, 'type': 'int' },
      'Nama'     : { 'col': 'K', 'width': 3.0 },
      'Alamat'   : { 'col': 'L', 'hidden': True },
      'DPP'      : { 'col': 'M', 'width': 1.4, 'type': 'money' },
      'PPn'      : { 'col': 'N', 'width': 1.4, 'type': 'money' },
      'PPnBM'    : { 'col': 'O', 'width': 0.8, 'type': 'money' },
      'Keterangan' : { 'col': 'P', 'width': 0.8 },
      'FG'       : { 'col': 'Q', 'width': 0.3 },
      'UM DPP'   : { 'col': 'R', 'width': 1.4, 'type': 'money' },
      'UM PPn'   : { 'col': 'S', 'width': 1.4, 'type': 'money' },
      'UM PPnBM' : { 'col': 'T', 'width': 0.8, 'type': 'money' },
      'Referensi': { 'col': 'U', 'width': 0.8 }
    }

  def init_sheet_style(self):
    self.blueFill = PatternFill(
      start_color='ff4fc3f7',
      end_color='ff4fc3f7',
      fill_type='solid')

    self.headerFont = Font(name='Arial', sz='10', bold=True)
    self.normalFont = Font(name='Arial', sz='10')
    self.centerText = Alignment(horizontal='center')

  def write_header(self, fields):
    for key in fields:
      metadata = fields[key]
      
      letter = metadata['col']
      cell = self.sheet[letter + "2"]

      cell.value = key
      cell.fill  = self.blueFill
      cell.font  = self.headerFont
      cell.alignment = self.centerText

      # take care of column width
      wscd = self.sheet.column_dimensions

      if 'width' in metadata.keys():
        wscd[letter].width = metadata['width']*12.98

      # take care of visibility
      if ('hidden' in metadata.keys()) \
      and (metadata['hidden']==True):
        wscd.hidden = True

  def write_entry(self, row, fields, keys, values):
    pairs = dict(zip(keys, values))

    for field_key in fields:
      metadata = fields[field_key]

      letter = metadata['col']
      cell = self.sheet[letter + str(row)]
      cell.font  = self.normalFont

      # display progress
      if (values[0]=='FK') and (field_key == 'Nama'):
        print(pairs['Nama'])

      # take care of value
      if field_key in keys:
        value = pairs[field_key]

        if 'type' in metadata.keys():
          match metadata['type']:
            case 'int'  : cell.value = int(value)
            case 'float': cell.value = float(value)
            case 'money': cell.value = float(value)
            case 'date' : cell.value = \
              datetime.strptime(value, "%d/%m/%Y")
        else: cell.value = value

  def run(self):
    # write headers
    self.write_header(self.fields_fk)

    # parse lines
    with open(self.filename) as f:
      lines = f.readlines()
      f.close()

    # write entries
    row = 2

    for line in lines:
      row += 1

      # ignore top headers
      if (row>5):
        values = split_quotes(line)

        if values[0]=="FK":
          self.write_entry(
            row, self.fields_fk, self.keys_fk, values)

def main():
  filename = 'faktur-keluaran.csv'

  wb = Workbook()
  ws = wb.active

  md = FakturMD2Sheet(filename, ws)
  md.run()

  # Save the file
  wb.save("sample.xlsx")

main()
