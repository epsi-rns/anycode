# coding: utf-8
from __future__ import unicode_literals
import math

blueScale = {
  0: 0xE3F2FD, 1: 0xBBDEFB, 2: 0x90CAF9,
  3: 0x64B5F6, 4: 0x42A5F5, 5: 0x2196F3,
  6: 0x1E88E5, 7: 0x1976D2, 8: 0x1565C0,
  9: 0x0D47A1
}

limeScale = {
  0: 0xF9FBE7, 1: 0xF0F4C3, 2: 0xE6EE9C,
  3: 0xDCE775, 4: 0xD4E157, 5: 0xCDDC39,
  6: 0xC0CA33, 7: 0xAFB42B, 8: 0x9E9D24,
  9: 0x827717
}

greenScale = {
  0: 0xE8F5E9, 1: 0xC8E6C9, 2: 0xA5D6A7,
  3: 0x81C784, 4: 0x66BB6A, 5: 0x4CAF50,
  6: 0x43A047, 7: 0x388E3C, 8: 0x2E7D32,
  9: 0x1B5E20
}


def p00_get_cell_type_test():
  # https://tutolibro.tech/2020/06/26
  # /libreoffice-calc-python-programming-part-6-type-of-a-cell-content/

  # get the doc from the scripting context 
  desktop      = XSCRIPTCONTEXT.getDesktop()
  model        = desktop.getCurrentComponent()
  active_sheet = model.CurrentController.ActiveSheet

  # get the range of addresses from selection
  oSelection   = model.getCurrentSelection()
  oArea        = oSelection.getRangeAddress()
  
  # get the first cell
  firstRow     = oArea.StartRow
  firstCol     = oArea.StartColumn
  selectedCell = active_sheet. \
    getCellByPosition(firstCol,firstRow) 
  cellType     = selectedCell.Type.value
  cellValue    = selectedCell.Value

  # display in next cell
  print("Cell (%d,%d) Type: %s" \
    % (firstCol, firstRow, cellType))
  active_sheet.getCellByPosition(
    firstCol+1, firstRow
  ).String = "Cell Type:" + cellType

  # display in next of next cell
  print("Cell (%d,%d) Type: %s" \
    % (firstCol, firstRow, cellValue))
  active_sheet.getCellByPosition(
    firstCol+2, firstRow
  ).String = "Cell Value:" + str(cellValue)

def p01_activate_sheet_test():
  # https://wiki.openoffice.org/wiki/Documentation
  # /BASIC_Guide/Cells_and_Ranges

  desktop    = XSCRIPTCONTEXT.getDesktop()
  model      = desktop.getCurrentComponent()
  sheets     = model.getSheets()
  sheet      = sheets.getByName("Combined")
  controller = model.getCurrentController()
  controller.setActiveSheet(sheet)

def p02_show_value_test():
  # get the document from the scripting context 
  document   = XSCRIPTCONTEXT.getDocument()
  sheet      = document.Sheets["Combined"]
  XSCRIPTCONTEXT  \
    .getDesktop() \
    .getCurrentComponent()  \
    .getCurrentController() \
    .setActiveSheet(sheet)

  b3 = sheet['B3']
  print("Cell B3: Type = %s, String = %s" \
    % (b3.Type.value, b3.String))

  c3 = sheet['C3']
  print("Cell C3: Type = %s, Value = %.2f" \
    % (c3.Type.value, c3.Valu ))


def p03_simple_color_test():
  # get the document from the scripting context 
  document   = XSCRIPTCONTEXT.getDocument()
  sheet      = document.Sheets["Combined"]

  b3c3 = sheet.getCellRangeByName('B3:C3') 

  bgcolor = b3c3.CellBackColor
  print(bgcolor)
  b3c3.CellBackColor = 0xFF0000

def p04_conditional_color_test():
  # get the document from the scripting context 
  document   = XSCRIPTCONTEXT.getDocument()
  sheet      = document.Sheets["Combined"]

  b3c3 = sheet.getCellRangeByName('B3:C3') 
  b3   = sheet['B3']
  c3   = sheet['C3']

  pred = b3.String
  prob = c3.Value
  colScale = math.floor(prob*10)
  print(colScale)

  if pred=='Female': 
    b3c3.CellBackColor = blueScale[colScale]
  elif pred=='Male':
    b3c3.CellBackColor = limeScale[colScale]
  elif pred=='Junior':
    b3c3.CellBackColor = greenScale[4]
  elif pred=='Juvenile':
    b3c3.CellBackColor = greenScale[3]
  elif pred=='Puppy':
    b3c3.CellBackColor = greenScale[2]

