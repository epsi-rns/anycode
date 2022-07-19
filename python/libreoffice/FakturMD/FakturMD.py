# coding: utf-8
from __future__ import unicode_literals

import re
from datetime import datetime
from com.sun.star.awt.FontWeight import BOLD
from com.sun.star.table.CellHoriJustify import CENTER

blueScale = {
  0: 0xE3F2FD, 1: 0xBBDEFB, 2: 0x90CAF9,
  3: 0x64B5F6, 4: 0x42A5F5, 5: 0x2196F3,
  6: 0x1E88E5, 7: 0x1976D2, 8: 0x1565C0,
  9: 0x0D47A1
}

class FakturSample:
  def __init__(self, filename):
    # save initial parameter
    self.filename = filename

    # prepare header
    self.init_header_keys()
    self.init_field_metadata()

  def new_sheet(self):
    # open new sheet
    desktop = XSCRIPTCONTEXT.getDesktop()
    model = desktop.loadComponentFromURL(
      "private:factory/scalc", "_blank", 0, ())

    self.sheet   = model.Sheets[0]
    self.numbers = model.NumberFormats
    self.locale  = model.CharLocale

    # post loading properties
    self.init_rupiah_format()

  # helper
  def split_quotes(self, header):
    header = header.replace(",\n", ',""')
    header = header.replace("\n", '')

    keys = re.split(r',(?=")', header)
    keys = [key.replace('"', '') for key in keys]
    return keys

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

    self.keys_fk   = self.split_quotes(header_fk)
    self.keys_fapr = self.split_quotes(header_fapr)
    self.keys_of   = self.split_quotes(header_of)

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
      'LT'       : { 'col': 'W',  'width': 0.5 },
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

  def write_header(self, fields):
    for key in fields:
      metadata = fields[key]
      letter = metadata['col']

      # take care cell
      cell = self.sheet["%s%d" % (letter, 2)]
      cell.String = key
      cell.CellBackColor = blueScale[3]
      cell.CharWeight    = BOLD
      cell.HoriJustify   = CENTER # or just 2

      # take care column
      column = self.sheet.getColumns().getByName(letter)
      column.CharHeight = 10
      column.CharFontName = "Arial"

      if 'width' in metadata.keys():
        column.Width = metadata['width'] * 2536

      # take care of visibility
      if ('hidden' in metadata.keys()) \
      and (metadata['hidden']==True):
        column.IsVisible = False

  def set_divider_width(self):
    # 2536 unit = 1"
    columns = self.sheet.getColumns()
    columns.getByName('A').Width  = 0.3 * 2536
    columns.getByName('V').Width  = 0.3 * 2536
    columns.getByName('AC').Width = 0.3 * 2536

  def get_number_format(self, format_string):
    nf = self.numbers.queryKey(  \
              format_string, self.locale, True)
    if nf == -1:
       nf = self.numbers.addNew( \
              format_string, self.locale)
    return nf

  def init_rupiah_format(self):
    # beware of the comma or period, depend on locale
    rupiah_string = \
      '" Rp"* #.##0,00 ;' + \
      '"-Rp"* #.##0,00 ;" Rp"* -# ;@ '

    self.rupiah_format = self. \
      get_number_format(rupiah_string)

  def write_entry(self, row, fields, keys, values):
    pairs = dict(zip(keys, values))

    for field_key in fields:
      metadata = fields[field_key]

      letter = metadata['col']
      cell = self.sheet["%s%d" % (letter, row)]

      # display progress
      if (values[0]=='FK') and (field_key == 'Nama'):
        print(pairs['Nama'])

      # take care of value
      if field_key in keys:
        value = pairs[field_key]

        # date special case
        if 'type' in metadata.keys() \
        and metadata['type'] == 'date':
          if field_key=='Tanggal': cell.String = \
            datetime.strptime(value, "%d/%m/%Y"). \
            strftime("%Y-%m-%d")
          elif field_key=='Timestamp':
            if len(value) > 8: cell.String = \
              datetime.strptime(value[0:8], "%Y%m%d"). \
              strftime("%Y-%m-%d")

        # money special case
        elif 'type' in metadata.keys() \
        and metadata['type'] == 'money':
          cell.Value = float(value)
          cell.NumberFormat = self.rupiah_format

        # take care of format
        elif 'format' in metadata.keys():
          cell.Value = float(value)
          cell.NumberFormat = self. \
            get_number_format(metadata['format'])

        # no date, no number format
        else:  cell.String = value

      elif field_key=='Lengkap':
        faktur = "%013s" % pairs["Faktur"]
        faktur = faktur[:3] +'-'+ faktur[3:5] +'.'+ faktur[5:]
        cell.String = pairs["Kode"]+pairs["Ganti"]+"."+faktur

  def run(self):
    # open blank sheet
    self.new_sheet()

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

      values = self.split_quotes(line)

      match values[0]:
        case "FK"  : self.write_entry (
            row, self.fields_fk,   self.keys_fk,   values)
        case "FAPR": self.write_entry (
            row, self.fields_fapr, self.keys_fapr, values)
        case "OF"  : self.write_entry (
            row, self.fields_of,   self.keys_of,   values)

def main():
  filename = '/home/epsi/Documents'+ \
             '/master-detail/faktur-keluaran.csv'

  sample = FakturSample(filename)
  sample.run()

