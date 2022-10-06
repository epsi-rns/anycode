# coding: utf-8
from __future__ import unicode_literals

class CopyRange03:
  def __init__(self):
    # save initial parameter
    desktop     = XSCRIPTCONTEXT.getDesktop()
    model       = desktop.getCurrentComponent()
    self.sheets = model.Sheets

  def copySheet(self, sName, tName):
    sheets = self.sheets

    sheets.copyByName(
      sName, tName, len(sheets))
    self.sSheet = sheets.getByName(sName)
    self.tSheet = sheets.getByName(tName)

  def calculateOffset(self, rangeAddr, index):
    rStart  = rangeAddr.StartRow
    rEnd    = rangeAddr.EndRow

    rHeight = rEnd - rStart
    return (rHeight + 1) * (index-1)

  def copyRange(self, strRange, rowCount):
    sSheet = self.sSheet
    tSheet = self.tSheet

    sCellRange = sSheet.getCellRangeByName(strRange)
    sRangeAddr = sCellRange.RangeAddress
    srStart  = sRangeAddr.StartRow
    scStart  = sRangeAddr.StartColumn

    for index in range(1, rowCount + 1):
      Offset = self.calculateOffset(sRangeAddr, index)
      tCell  = tSheet.getCellByPosition(\
        scStart, srStart + Offset)
      tCellAddr = tCell.CellAddress

      sSheet.copyRange(tCellAddr, sRangeAddr)

  def setRangeHeights(self, strRange, rowCount):
    cellRange  = self.sSheet.getCellRangeByName(strRange)
    sRangeAddr = cellRange.RangeAddress
    srStart  = sRangeAddr.StartRow
    srEnd    = sRangeAddr.EndRow

    sRows  = self.sSheet.getRows()
    tRows  = self.tSheet.getRows()

    for index in range(1, rowCount + 1):
      Offset = self.calculateOffset(sRangeAddr, index)

      for row in range(srStart, srEnd + 1):
        tRows.getByIndex(row + Offset).Height = \
          sRows.getByIndex(row).Height

  def setPrintArea(self, strRange):
    cellRange = self.tSheet.getCellRangeByName(strRange)
    rangeAddr = cellRange.RangeAddress
    self.tSheet.setPrintAreas([rangeAddr])

  def run(self):
    self.copySheet('Example', 'Result')
    self.copyRange('B4:K13', 5)
    self.setRangeHeights('B4:K13', 5)
    self.setPrintArea('A1:L53')

def main():
  sample = CopyRange03()
  sample.run()
