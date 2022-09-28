import openpyxl
from openpyxl import load_workbook
from openpyxl.utils import rows_from_range
from openpyxl.utils.cell import coordinate_from_string
from openpyxl.worksheet.cell_range import CellRange

# Copy Range Class
class CopyRange:
  def __init__(self, sheet, coord_copied):
    # save initial parameter
    self.sheet = sheet
    self.coord_copied = coord_copied

  # value, style and number format
  def copy_cells(self):
    from copy import copy

    for row in rows_from_range(self.coord_copied):
      for cell in row:
        coord  = coordinate_from_string(cell)
        offset = coord[0] + str(coord[1] + self.offset_down)

        source = self.sheet[cell]
        target = self.sheet[offset]

        target.value = source.value
        target.number_format = source.number_format
        if source.has_style:
           target._style = copy(source._style)

  # row height related
  def set_row_height(self):
    wsrd = self.sheet.row_dimensions
    for row in rows_from_range(self.coord_copied):
      first  = row[0]
      coord  = coordinate_from_string(first)
      source = wsrd[coord[1]]
      target = wsrd[coord[1] + self.offset_down]
      target.height = source.height

  # merged range related
  def set_merged_range(self):
    range_copied = CellRange(self.coord_copied)
    for merged_cell in self.sheet.merged_cells:
      coord_source = merged_cell.coord
      if coord_source in range_copied:
         cell_range = CellRange(coord_source)
         cell_range.shift(row_shift = self.offset_down)
         coord_target = cell_range.coord
         self.sheet.merge_cells(coord_target)

  def run(self, offset_down):
    self.offset_down = offset_down
    self.copy_cells()
    self.set_row_height()
    self.set_merged_range()

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
      'nomor' : { 'source': 'A7', 'target': 'B5' },
      'nama'  : { 'source': 'B7', 'target': 'C5' },
      'npwp'  : { 'source': 'C7', 'target': 'F5' },
      'nomor_faktur'    : { 'source': 'D7', 'target': 'I5' },
      'tanggal_faktur'  : { 'source': 'E7', 'target': 'D6' },
      'masa'            : { 'source': 'F7', 'target': 'G7' },
      'tahun'           : { 'source': 'G7', 'target': 'G8' },
      'status_faktur'   : { 'source': 'H7', 'target': 'I10' },
      'dpp'    : { 'source': 'I7', 'target': 'J7' },
      'ppn'    : { 'source': 'J7', 'target': 'J8' },
      'ppnbm'  : { 'source': 'K7', 'target': 'J9' },
      'status_approval' : { 'source': 'L7', 'target': 'I11' },
      'tanggal_approval': { 'source': 'M7', 'target': 'D7' },
      'keterangan'      : { 'source': 'N7', 'target': 'I12' },
      'penandatangan'   : { 'source': 'O7', 'target': 'D8' },
      'referensi'       : { 'source': 'P7', 'target': 'G6' },
      'user_perekam'    : { 'source': 'Q7', 'target': 'D10' },
      'tanggal_rekam'   : { 'source': 'R7', 'target': 'D9' },
      'user_pengubah'   : { 'source': 'S7', 'target': 'D12' },
      'tanggal_ubah'    : { 'source': 'T7', 'target': 'D11' },
    }

  def run(self, start, end):
    fields = self.get_fields_mapping()

    job = range(start, end + 1)
    for index in job:
      form_offset = index*self.form_height

      cr = CopyRange(self.ws_target,'B4:K13')
      cr.run(form_offset)

      for field, pair in fields.items():
        addr_source = pair['source']
        addr_target = pair['target']

        coord  = coordinate_from_string(addr_source)
        addr_source = coord[0] + str(coord[1] + index-1)

        coord  = coordinate_from_string(addr_target)
        addr_target = coord[0] + str(coord[1] + form_offset)

        cell_source  = self.ws_source[addr_source]
        cell_target  = self.ws_target[addr_target]

        cell_target.value = cell_source.value

# Main: Program Entry Point
def main():
  file_source = "data.xlsx"
  file_target = "result.xlsx"

  wb = load_workbook(file_source)
  ws_template = wb["Empty"]
  ws_source   = wb["Source"]
  ws_target   = wb.copy_worksheet(ws_template)
  ws_target.title = "Target"
  wb.active = ws_target
  
  cr = TranslateRow(ws_source, ws_target)
  cr.run(1, 8)

  # Save the file
  wb.save(file_target)

main()
