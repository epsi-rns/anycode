# coding: utf-8
from __future__ import unicode_literals
from datetime import datetime

from com.sun.star.awt.FontWeight import BOLD
from com.sun.star.table.CellHoriJustify import CENTER

def test():
    desktop = XSCRIPTCONTEXT.getDesktop()
    model = desktop.loadComponentFromURL(
      "private:factory/scalc", "_blank", 0, ())
    numberfmt = model.NumberFormats
    locale    = model.CharLocale

    sheet = model.Sheets[0]

    column = sheet.getColumns().getByName('B')
    column.CharHeight   = 10
    column.CharFontName = "Arial"
    column.Width        = 5000

    # serial format example
    cell = sheet["B2"]
    cell.CellBackColor = 0x64B5F6
    cell.CharWeight    = BOLD
    cell.HoriJustify   = CENTER # or just 2
    
    cell.Value    = 81443518011000.0
    serial_format = '00\.000\.000\.0-000\.000'
    
    nfs = numberfmt.queryKey(serial_format, locale, True)
    if nfs == -1:
      nfs = numberfmt.addNew(serial_format, locale)
    cell.NumberFormat = nfs

    # date format example
    cell = sheet["B3"]
    cell.CellBackColor = 0xBBDEFB
    cell.HoriJustify   = CENTER # or just 2

    # Offset of the date value for the date of 1900-01-00
    offset = 693594

    date_string = '05/07/2022'
    date_value = datetime.strptime(date_string, "%d/%m/%Y")
    cell.Value = date_value.toordinal()-offset
    
    # nFormat = numberfmt.getStandardFormat( 2, locale ) 
    # cell.NumberFormat = nFormat

    date_format = 'DD-MMM-YY;@'

    nfd = numberfmt.queryKey(date_format, locale, True)
    if nfd == -1:
      nfd = numberfmt.addNew(date_format, locale)
    cell.NumberFormat = nfd


