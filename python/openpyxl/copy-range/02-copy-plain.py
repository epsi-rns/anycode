from copy import copy

import openpyxl
from openpyxl import load_workbook
from openpyxl.utils import rows_from_range
from openpyxl.utils.cell import coordinate_from_string
from openpyxl.worksheet.cell_range import CellRange

def copy_range(coord_copied, sheet, offset_down):
  # row height related
  wsrd = sheet.row_dimensions

  for row in rows_from_range(coord_copied):
    # value, style and number format
    for cell in row:
      coord  = coordinate_from_string(cell)
      offset = coord[0] + str(coord[1] + offset_down)

      source = sheet[cell]
      target = sheet[offset]

      target.value = source.value
      target.number_format = source.number_format
      if source.has_style:
         target._style = copy(source._style)

    # row height
    first  = row[0]
    coord  = coordinate_from_string(first)
    source = wsrd[coord[1]]
    target = wsrd[coord[1] + offset_down]
    target.height = source.height

  # merged range
  range_copied = CellRange(coord_copied)
  for merged_cell in sheet.merged_cells:
    coord_source = merged_cell.coord
    if coord_source in range_copied:
       cell_range = CellRange(coord_source)
       cell_range.shift(row_shift = offset_down)
       coord_target = cell_range.coord
       sheet.merge_cells(coord_target)

# Main: Program Entry Point

wb = load_workbook("source-en.xlsx")
ws = wb["Example"]

copy_range ('B4:K13', ws, 10)

# Save the file
wb.save("target-en.xlsx")




