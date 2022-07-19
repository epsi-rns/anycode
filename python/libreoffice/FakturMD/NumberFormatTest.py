# coding: utf-8
from __future__ import unicode_literals
from datetime import datetime

from com.sun.star.\
  awt.FontWeight import BOLD
from com.sun.star.\
  table.CellHoriJustify import CENTER

class NumberFormatTest:
  def __init__(self):
    desktop = XSCRIPTCONTEXT.getDesktop()
    model = desktop.loadComponentFromURL(
      "private:factory/scalc", "_blank", 0, ())
    self.numberfmt = model.NumberFormats
    self.locale    = model.CharLocale

    self.sheet = model.Sheets[0]

  # gather all example here
  def run(self):
    self.column_example()
    self.serial_example()
    self.date_value_example()
    # self.date_format_standard()
    self.date_format_custom()

  def get_number_format(self, format_string):
    nf = self.numberfmt.queryKey(  \
              format_string, self.locale, True)
    if nf == -1:
       nf = self.numberfmt.addNew( \
              format_string, self.locale)
    return nf

  def column_example(self):
    column = self.sheet. \
      getColumns().getByName('B')
    column.CharHeight   = 10
    column.CharFontName = "Arial"
    column.Width        = 5000

  def serial_example(self):
    # cell decoration
    cell = self.sheet["B2"]
    cell.CellBackColor = 0x64B5F6
    cell.CharWeight    = BOLD
    cell.HoriJustify   = CENTER # or just 2
    
    # handling value and format
    cell.Value    = 81443518011000.0
    serial_format = '00\.000\.000\.0-000\.000'
    cell.NumberFormat = self. \
      get_number_format(serial_format)

  def date_value_example(self):
    # cell decoration
    cell = self.sheet["B3"]
    cell.CellBackColor = 0xBBDEFB
    cell.HoriJustify   = CENTER # or just 2

    # Offset of the date value
    # for the date of 1900-01-00
    offset = 693594

    # handling date value
    date_string = '05/07/2022'
    date_value = datetime. \
      strptime(date_string, "%d/%m/%Y")
    cell.Value = date_value.toordinal() - offset

  def date_format_standard(self):
    cell = self.sheet["B3"]
    dateFormat = self.numberfmt. \
      getStandardFormat(2, self.locale)
    cell.NumberFormat = dateFormat

  def date_format_custom(self):
    cell = self.sheet["B3"]
    date_format = 'DD-MMM-YY;@'
    cell.NumberFormat = \
      self.get_number_format(date_format)

def test():
  sample = NumberFormatTest()
  sample.run()
