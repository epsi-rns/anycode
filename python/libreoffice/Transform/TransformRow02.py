# coding: utf-8
from __future__ import unicode_literals

class TransformRow02:
  def __init__(self, eName, sName, tName):
    # save initial parameter
    desktop     = XSCRIPTCONTEXT.getDesktop()
    model       = desktop.getCurrentComponent()
    self.sheets = model.Sheets

    self.eName = eName
    self.sName = sName
    self.tName = tName

  def get_fields_mapping(self):
    # declare all field coordinate
    return {
      'id'    : { 'source': 'A7', 'target': 'B5' },
      'name'  : { 'source': 'B7', 'target': 'C5' },
      'taxpayer_id'     : { 'source': 'C7', 'target': 'F5' },
      'tax_inv_id'      : { 'source': 'D7', 'target': 'I5' },
      'tax_inv_date'    : { 'source': 'E7', 'target': 'D6' },
      'month_period'    : { 'source': 'F7', 'target': 'G7' },
      'year'            : { 'source': 'G7', 'target': 'G8' },
      'tax_inv_status'  : { 'source': 'H7', 'target': 'I10' },
      'price'  : { 'source': 'I7', 'target': 'J7' },
      'vat'    : { 'source': 'J7', 'target': 'J8' },
      'vat_lux': { 'source': 'K7', 'target': 'J9' },
      'approval_status' : { 'source': 'L7', 'target': 'I11' },
      'approval_date'   : { 'source': 'M7', 'target': 'D7' },
      'description'     : { 'source': 'N7', 'target': 'I12' },
      'signatory_user'  : { 'source': 'O7', 'target': 'D8' },
      'reference'       : { 'source': 'P7', 'target': 'I6' },
      'record_user'     : { 'source': 'Q7', 'target': 'D10' },
      'record_date'     : { 'source': 'R7', 'target': 'D9' },
      'update_user'     : { 'source': 'S7', 'target': 'D12' },
      'update_date'     : { 'source': 'T7', 'target': 'D11' },
    }

  def copySheet(self):
    sheets = self.sheets
    sheets.copyByName(
      self.eName, self.tName, len(sheets))

    self.eSheet = sheets.getByName(self.eName)
    self.sSheet = sheets.getByName(self.sName)
    self.tSheet = sheets.getByName(self.tName)

  def copy_field(self, pair, rowHeight, index):
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

  def run(self, rowHeight, rowCount):
    self.copySheet()
    fields = self.get_fields_mapping()

    masterIndices = range(1, rowCount + 1)
    for index in masterIndices:
      for field, pair in fields.items():
        self.copy_field(pair, rowHeight, index)

def main():
  sample = TransformRow02('Empty-en', 'Source-en', 'Target-en')
  sample.run(9, 3)
