import openpyxl
from openpyxl import load_workbook
from openpyxl.styles import PatternFill
from openpyxl.utils import get_column_letter

class SheetDiff:
  def __init__(self, book_fst, sheet_fst,
                     book_snd, sheet_snd,
                     book_target, cols, rows):

    wb_fst      = load_workbook(book_fst)
    self.ws_fst = wb_fst[sheet_fst]
    self.wb_snd = load_workbook(book_snd)
    self.ws_snd = self.wb_snd[sheet_snd]

    self.target = book_target
    self.rows   = rows
    self.cols   = cols

    color_lime5   = 'FFCDDC39'
    self.fill     = PatternFill(
      start_color   = color_lime5,
      end_color     = color_lime5,
      fill_type     = 'solid')

  def diff(self):
    for col in self.cols:
      for row in self.rows:
        cursor = get_column_letter(col) + str(row)

        value_fst = self.ws_fst[cursor].value
        value_snd = self.ws_snd[cursor].value

        if (value_fst != value_snd):
          print(f'{cursor:6} : {value_fst} -> {value_snd}')
          self.ws_snd[cursor].fill = self.fill

    # Save the file
    self.wb_snd.save(self.target)

def main():
  cols = range(1, 8)
  rows = range(3, 43)
  sample = SheetDiff(
             'first.xlsx',  'Combined',
             'second.xlsx', 'Combined',
             'diff.xlsx', cols, rows)
  sample.diff()

main()
