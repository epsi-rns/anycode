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

# Main: Program Entry Point
def main():
  file_source = "source.xlsx"
  file_target = "target.xlsx"

  wb = load_workbook(file_source)
  ws = wb["Example"]

  cr = CopyRange(ws,'B4:K13')
  cr.run(10)
  cr.run(20)

  ws.print_area = "A1:L34"

  # Save the file
  wb.save(file_target)

main()
