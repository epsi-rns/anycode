# coding: utf-8
from __future__ import unicode_literals

class CopyRange03:
  def __init__(self, sName, tName):
    desktop     = XSCRIPTCONTEXT.getDesktop()
    model       = desktop.getCurrentComponent()
    self.sheets = model.Sheets

    # save initial parameter
    self.sName = sName
    self.tName = tName

  def copySheet(self):
    self.sheets.copyByName(
      self.sName, self.tName, len(self.sheets))

  def calculateOffset(self, rangeAddr, index):
    rStart  = rangeAddr.StartRow
    rEnd    = rangeAddr.EndRow

    rHeight = rEnd - rStart
    return (rHeight + 1) * (index - 1)

  def copyRange(self, strRange, index):
    sSheet = self.sSheet
    tSheet = self.tSheet

    sCellRange = sSheet.getCellRangeByName(strRange)
    sRangeAddr = sCellRange.RangeAddress
    srStart  = sRangeAddr.StartRow
    scStart  = sRangeAddr.StartColumn

    Offset = self.calculateOffset(sRangeAddr, index)
    tCell  = tSheet.getCellByPosition(\
      scStart, srStart + Offset)
    tCellAddr = tCell.CellAddress

    sSheet.copyRange(tCellAddr, sRangeAddr)

  def setRangeHeights(self, strRange, index):
    sCellRange = self.sSheet.getCellRangeByName(strRange)
    sRangeAddr = sCellRange.RangeAddress
    srStart  = sRangeAddr.StartRow
    srEnd    = sRangeAddr.EndRow

    sRows  = self.sSheet.getRows()
    tRows  = self.tSheet.getRows()

    Offset = self.calculateOffset(sRangeAddr, index)

    detailIndices = range(srStart, srEnd + 1) 
    for row in detailIndices:
      tRows.getByIndex(row + Offset).Height = \
        sRows.getByIndex(row).Height

  def setPrintArea(self, strRange):
    cellRange = self.tSheet.getCellRangeByName(strRange)
    rangeAddr = cellRange.RangeAddress
    self.tSheet.setPrintAreas([rangeAddr])

  def run(self, stringRange, index):
    self.sSheet = self.sheets.getByName(self.sName)
    self.tSheet = self.sheets.getByName(self.tName)

    self.copyRange(stringRange, index)
    self.setRangeHeights(stringRange, index)

class TransformRow03:
  def __init__(self, eName, sName, tName):
    # save initial parameter
    desktop     = XSCRIPTCONTEXT.getDesktop()
    model       = desktop.getCurrentComponent()
    self.sheets = model.Sheets

    self.eName = eName
    self.sName = sName
    self.tName = tName

  def getFieldsMapping(self):
    # declare all field coordinate
    return {
      'id'    : { 'source': 'B6', 'target': 'B5' },
      'name'  : { 'source': 'C6', 'target': 'C5' },
      'taxpayer_id'     : { 'source': 'D6', 'target': 'F5' },
      'tax_inv_id'      : { 'source': 'E6', 'target': 'I5' },
      'tax_inv_date'    : { 'source': 'F6', 'target': 'D6' },
      'month_period'    : { 'source': 'G6', 'target': 'G6' },
      'year'            : { 'source': 'H6', 'target': 'G7' },
      'tax_inv_status'  : { 'source': 'I6', 'target': 'I9' },
      'price'  : { 'source': 'J6', 'target': 'J6' },
      'vat'    : { 'source': 'K6', 'target': 'J7' },
      'vat_lux': { 'source': 'L6', 'target': 'J8' },
      'approval_status' : { 'source': 'M6', 'target': 'I10' },
      'approval_date'   : { 'source': 'N6', 'target': 'D7' },
      'description'     : { 'source': 'O6', 'target': 'I11' },
      'record_user'     : { 'source': 'P6', 'target': 'D9' },
      'record_date'     : { 'source': 'Q6', 'target': 'D8' },
      'update_user'     : { 'source': 'R6', 'target': 'D11' },
      'update_date'     : { 'source': 'S6', 'target': 'D10' },
    }

  def copySheet(self):
    sheets = self.sheets
    sheets.copyByName(
      self.eName, self.tName, len(sheets))

    self.eSheet = sheets.getByName(self.eName)
    self.sSheet = sheets.getByName(self.sName)
    self.tSheet = sheets.getByName(self.tName)

  def copyField(self, pair, rowHeight, index):
    addrSource = pair['source']
    addrTarget = pair['target']

    sCellBase = self.sSheet.getCellRangeByName(addrSource)
    tCellBase = self.tSheet.getCellRangeByName(addrTarget)
    scAddress = sCellBase.CellAddress
    tcAddress = tCellBase.CellAddress

    Offset = (rowHeight+1) * (index-1)

    sCell  = self.sSheet.getCellByPosition(\
      scAddress.Column, scAddress.Row + (index-1))
    tCell  = self.tSheet.getCellByPosition(\
      tcAddress.Column, tcAddress.Row + Offset)

    match sCell.Type.value:
      case "VALUE" : tCell.Value  = sCell.Value
      case "TEXT"  : tCell.String = sCell.String

  def calculateHeight(self, stringRange):
    eCellRange = self.eSheet.getCellRangeByName(stringRange)
    eRangeAddr = eCellRange.RangeAddress

    rStart  = eRangeAddr.StartRow
    rEnd    = eRangeAddr.EndRow

    return rEnd - rStart

  def run(self, stringRange, printArea, rowCount):
    self.copySheet()
    fields = self.getFieldsMapping()

    template = CopyRange03(self.eName, self.tName)
    rowHeight = self.calculateHeight(stringRange)

    masterIndices = range(1, rowCount + 1)
    for index in masterIndices:
      template.run(stringRange, index)
      for field, pair in fields.items():
        self.copyField(pair, rowHeight, index)

    template.setPrintArea(printArea)

def main():
  sample = TransformRow03(\
    'T-FPM', '2022-FPM', '22-M')
  sample.run('B4:K12', 'A1:L12', 1)
