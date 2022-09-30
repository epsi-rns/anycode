import openpyxl
from openpyxl import load_workbook
from openpyxl.utils import rows_from_range
from openpyxl.utils.cell import coordinate_from_string

# Copy Range Class Class
class CopyRange:
  def __init__(self, sheet, coord_copied):
    # save initial parameter
    self.sheet = sheet
    self.coord_copied = coord_copied

  # value, style and number format
  def copy_cells(self, offset_down):
    from copy import copy

    for row in rows_from_range(self.coord_copied):
      for cell in row:
        coord  = coordinate_from_string(cell)
        offset = coord[0] + str(coord[1] + offset_down)

        source = self.sheet[cell]
        target = self.sheet[offset]

        target.value = source.value
        target.number_format = source.number_format
        if source.has_style:
           target._style = copy(source._style)

# Main: Program Entry Point
def main():
  file_source = "source-en.xlsx"
  file_target = "target-en.xlsx"

  wb = load_workbook(file_source)
  ws = wb["Example"]

  cr = CopyRange(ws,'B4:K13')
  cr.copy_cells(10)

  # Save the file
  wb.save(file_target)

main()
