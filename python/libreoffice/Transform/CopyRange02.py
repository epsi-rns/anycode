# coding: utf-8
from __future__ import unicode_literals

class CopyRange02:
  def __init__(self, name):
    # save initial parameter
    desktop    = XSCRIPTCONTEXT.getDesktop()
    model      = desktop.getCurrentComponent()
    sheets     = model.getSheets()
    self.sheet = sheets.getByName(name)

  def copyRange(self, stringRange, stringAddress):
    sourceCellRange = self.sheet.getCellRangeByName(stringRange)
    sourceRangeAddress = sourceCellRange.RangeAddress

    targetCell = self.sheet.getCellRangeByName(stringAddress)
    targetCellAddress = targetCell.CellAddress

    self.sheet.copyRange(targetCellAddress, sourceRangeAddress)

  def setPrintArea(self, stringRange):
    cellRange = self.sheet.getCellRangeByName(stringRange)
    rangeAddress = cellRange.RangeAddress
    self.sheet.setPrintAreas([rangeAddress])

  def setRangeHeights(self, stringRange, stringAddress):
    cellRange = self.sheet.getCellRangeByName(stringRange)
    sourceRangeAddress = cellRange.RangeAddress
    sourceStart  = sourceRangeAddress.StartRow
    sourceEnd    = sourceRangeAddress.EndRow

    targetCell   = self.sheet.getCellRangeByName(stringAddress)
    targetStart  = targetCell.CellAddress.Row
    Offset = targetStart - sourceStart

    rows = self.sheet.getRows()
    for sourceRow in range(sourceStart, sourceEnd + 1):
      rows.getByIndex(sourceRow + Offset).Height = \
        rows.getByIndex(sourceRow).Height

  def run(self):
    self.copyRange('B4:K13', 'B14')
    self.setPrintArea('A1:L23')
    self.setRangeHeights('B4:K13', 'B14')

def main():
  sample = CopyRange02('Example')
  sample.run()
