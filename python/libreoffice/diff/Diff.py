# coding: utf-8
from __future__ import unicode_literals

class SheetDiff:
  def __init__(self, sheet_fst,
                     sheet_snd, cols, rows):
    document       = XSCRIPTCONTEXT.getDocument()
    self.sheet_fst = document.Sheets[sheet_fst]
    self.sheet_snd = document.Sheets[sheet_snd]
    self.rows      = rows
    self.columns   = cols
    self.color     = 0xCDDC39 # lime5

  def compare(self, cell_fst, cell_snd):
    if (cell_fst.String != cell_snd.String):
      print(f'{cell_snd.AbsoluteName:16} : '
            f'{cell_fst.String:8} -> '
            f'{cell_snd.String:8}')
      cell_snd.CellBackColor = self.color

  def diff(self):
    for col in self.columns:
      for row in self.rows:
        cell_fst = self.sheet_fst \
          .getCellByPosition(col, row)
        cell_snd = self.sheet_snd \
          .getCellByPosition(col, row)
        self.compare(cell_fst, cell_snd)

def main():
  r_columns = range(0, 8)
  r_rows    = range(0, 42)
  sample = SheetDiff(
             'First', 'Second',
             r_columns, r_rows)
  sample.diff()
