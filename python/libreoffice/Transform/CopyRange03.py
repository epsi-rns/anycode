# coding: utf-8
from __future__ import unicode_literals

class CopyRange03:
  def __init__(self, sName, tName):
    # save initial parameter
    desktop     = XSCRIPTCONTEXT.getDesktop()
    model       = desktop.getCurrentComponent()
    self.sheets = model.Sheets

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

def main():
  template = CopyRange03('Example-id', 'Result-id')
  template.copySheet()

  rowCount = 5
  masterIndices = range(1, rowCount + 1)
  for index in masterIndices:
    template.run('B4:K13', index)

  template.setPrintArea('A1:L53')
