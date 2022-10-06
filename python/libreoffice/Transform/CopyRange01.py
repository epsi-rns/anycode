# coding: utf-8
from __future__ import unicode_literals

class CopyRange01:
  def __init__(self, name):
    # save initial parameter
    desktop    = XSCRIPTCONTEXT.getDesktop()
    model      = desktop.getCurrentComponent()
    sheets     = model.getSheets()
    self.sheet = sheets.getByName(name)

  def addressTest(self):
    c5 = self.sheet['C5']
    print("Cell C5: Type = %s, String = %s" \
        % (c5.Type.value, c5.String))

    cellRange = self.sheet.getCellRangeByName('B4:K12')
    rangeAddress = cellRange.RangeAddress
    print(rangeAddress.StartColumn)
    print(rangeAddress.StartRow)
    print(rangeAddress.EndColumn)
    print(rangeAddress.EndRow)

  def run(self):
    self.addressTest()

def main():
  sample = CopyRange01('Example-en')
  sample.run()

