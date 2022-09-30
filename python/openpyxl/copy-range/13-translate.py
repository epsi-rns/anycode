import openpyxl
from openpyxl import load_workbook
from openpyxl.utils.cell import coordinate_from_string

# Translate Row Class
class TranslateRow:
  def __init__(self, ws_source, ws_target):
    # save initial parameter
    self.ws_source = ws_source
    self.ws_target = ws_target
    self.form_height = 10  

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

  def run(self, start, end):
    fields = self.get_fields_mapping()

    job = range(start, end + 1)
    for index in job:
      for field, pair in fields.items():
        addr_source = pair['source']
        addr_target = pair['target']

        coord  = coordinate_from_string(addr_source)
        addr_source = coord[0] + str(coord[1] + index-1)

        coord  = coordinate_from_string(addr_target)
        addr_target = coord[0] + str(coord[1] + (index-1)*self.form_height)

        cell_source  = self.ws_source[addr_source]
        cell_target  = self.ws_target[addr_target]

        cell_target.value = cell_source.value

        if field in ['nama', 'name']:
           print(cell_source.value)

# Main: Program Entry Point
def main():
  file_source = "data.xlsx"
  file_target = "result.xlsx"

  wb = load_workbook(file_source)
  ws_template = wb["Empty"]
  ws_source   = wb["Source-en"]   # example "06-Jun"
  ws_target   = wb.copy_worksheet(ws_template)
  ws_target.title = "Target"      # example "06-Form-Jun"
  wb.active = ws_target
  
  cr = TranslateRow(ws_source, ws_target)
  cr.run(1, 3)

  # Save the file
  wb.save(file_target)

main()
