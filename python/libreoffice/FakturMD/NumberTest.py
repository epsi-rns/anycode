# coding: utf-8
from __future__ import unicode_literals

from com.sun.star.awt.FontWeight import BOLD
from com.sun.star.table.CellHoriJustify import CENTER

def test():
    desktop = XSCRIPTCONTEXT.getDesktop()
    model = desktop.loadComponentFromURL(
      "private:factory/scalc", "_blank", 0, ())
    numbers = model.NumberFormats
    locale  = model.CharLocale

    sheet = model.Sheets[0]

    column = sheet.getColumns().getByName('B')
    column.CharHeight   = 10
    column.CharFontName = "Arial"
    column.Width        = 5000

    cell = sheet["B2"]
    cell.CellBackColor = 0xBBDEFB
    cell.CharWeight    = BOLD
    cell.HoriJustify   = CENTER # or just 2
    
    cell.Value         = 81443518011000.0
    serial_format = '00\.000\.000\.0-000\.000'
    
    nf = numbers.queryKey(serial_format, locale, True)
    if nf == -1:
      nf = numbers.addNew(serial_format, locale)
    cell.NumberFormat = nf
