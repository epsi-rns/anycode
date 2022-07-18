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

    header_fapr = \
      '"LT","Nama","Alamat","Perekam",' +\
      '"Wilayah","Timestamp","Hash"'

    header_of  = \
      '"OF","Kode","Nama","Satuan","Jumlah",' +\
      '"Total","Diskon","DPP","PPN","Tarif","PPnBM"'

    self.keys_fk   = split_quotes(header_fk)
    self.keys_fapr = split_quotes(header_fapr)
    self.keys_of   = split_quotes(header_of)

  def init_field_metadata(self):
    self.fields_fk = {
      'FK'       : { 'col': 'B', 'width': 0.3 },
      'Kode'     : { 'col': 'C', 'width': 0.4,
                     'format': '00' },
      'Ganti'    : { 'col': 'D', 'width': 0.4 },
      'Faktur'   : { 'col': 'E', 'width': 1.2, 'type': 'int',
                     'format': '000-00\.00000000' },
      'Lengkap'  : { 'col': 'F', 'width': 1.5 },
      'Masa'     : { 'col': 'G', 'width': 0.4, 'type': 'int', },
      'Tahun'    : { 'col': 'H', 'width': 0.5, 'type': 'int', },
      'Tanggal'  : { 'col': 'I', 'width': 0.8, 'type': 'date',
                     'format': 'DD-MMM-YY;@' },
      'NPWP'     : { 'col': 'J', 'width': 1.5, 'type': 'int',
                     'format': '00\.000\.000\.0-000\.000' },
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

    self.fields_fapr = {
      'LT'       : { 'col': 'W',  'width': 0.4 },
      'Nama'     : { 'col': 'X',  'width': 2.0 },
      'Alamat'   : { 'col': 'Y',  'hidden': True },
      'Perekam'  : { 'col': 'Z',  'width': 1.0 },
      'Wilayah'  : { 'col': 'AA', 'width': 1.4 },
      'Timestamp': { 'col': 'AB', 'width': 0.8, 'type': 'date',
                       'format': 'DD-MMM-YY;@' }
    }

    self.fields_of = {
      'OF'     : { 'col': 'AD',  'width': 0.3 },
      'Kode'   : { 'col': 'AE',  'width': 0.4 },
      'Nama'   : { 'col': 'AF',  'width': 1.5 },
      'Satuan' : { 'col': 'AG',  'width': 1.4, 'type': 'money' },
      'Jumlah' : { 'col': 'AH',  'width': 0.6, 'type': 'float' },
      'Total'  : { 'col': 'AI',  'width': 1.4, 'type': 'money' },
      'Diskon' : { 'col': 'AJ',  'width': 0.8, 'type': 'money' },
      'DPP'    : { 'col': 'AK',  'width': 1.4, 'type': 'money' },
      'PPn'    : { 'col': 'AL',  'width': 1.4, 'type': 'money' },
      'Tarif'  : { 'col': 'AM',  'width': 0.8, 'type': 'float' },
      'PPnBM'  : { 'col': 'AN',  'width': 0.8, 'type': 'money' },
    }

  def init_sheet_style(self):
    self.blueFill = PatternFill(
      start_color='ff4fc3f7',
      end_color='ff4fc3f7',
      fill_type='solid')

    self.headerFont = Font(name='Arial', sz='10', bold=True)
    self.normalFont = Font(name='Arial', sz='10')
    self.centerText = Alignment(horizontal='center')

  def set_divider_width(self):
    # 12.98 unit = 1
    wscd = self.sheet.column_dimensions
    wscd['A'].width  =  4.0      # left empty ~0.31"
    wscd['V'].width  =  4.0      # empty      ~0.31"
    wscd['AC'].width =  4.0      # empty      ~0.31"

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
        wscd[letter].hidden = True

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
            case 'date' :
              if field_key=='Tanggal': cell.value = \
                  datetime.strptime(value, "%d/%m/%Y")
              if field_key=='Timestamp':
                if len(value) > 8: cell.value = \
                  datetime.strptime(value[0:8], "%Y%m%d")
        else: cell.value = value
      elif field_key=='Lengkap':
        faktur = "%013s" % pairs["Faktur"]
        faktur = faktur[:3] +'-'+ faktur[3:5] +'.'+ faktur[5:]
        cell.value = pairs["Kode"]+pairs["Ganti"]+"."+faktur

      # take care of format
      if 'format' in metadata.keys():
        cell.number_format = metadata['format']
      elif ('type' in metadata.keys()) \
      and (metadata['type']=='money'):
        # beware of the comma or period, depend on locale
        cell.number_format = '" Rp"* #,##0.00 ;' + \
            '"-Rp"* #,##0.00 ;" Rp"* -# ;@ '

  def run(self):
    # write headers
    self.write_header(self.fields_fk)
    self.write_header(self.fields_fapr)
    self.write_header(self.fields_of) 
    self.set_divider_width()

    # parse lines
    with open(self.filename) as f:
      lines = f.readlines()
      f.close()

    # write entries
    row = 5

    # ignore top headers
    for line in lines[3:]:
      row += 1

      values = split_quotes(line)

      match values[0]:
        case "FK"  : self.write_entry (
            row, self.fields_fk,   self.keys_fk,   values)
        case "FAPR": self.write_entry (
            row, self.fields_fapr, self.keys_fapr, values)
        case "OF"  : self.write_entry (
            row, self.fields_of,   self.keys_of,   values)

def main():
  filename = 'faktur-keluaran.csv'

  wb = Workbook()
  ws = wb.active

  md = FakturMD2Sheet(filename, ws)
  md.run()

  # Save the file
  wb.save("sample.xlsx")

main()
