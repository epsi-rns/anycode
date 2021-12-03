import os
from os import listdir
from os.path import isfile, join

import openpyxl
from openpyxl import load_workbook
from openpyxl import Workbook

wb_dest   = load_workbook('./empty.xlsx')

def merge_all(path):
  onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
  onlyxlxs  = [f for f in onlyfiles if '.xlsx' in f]

  for f in onlyxlxs:
    wb_source = load_workbook(join(path, f))
    noext = os.path.splitext(f)[0]

    # Process first sheet
    sheet = wb_source.worksheets[0] 
    sheet.title = noext
    sheet._parent = wb_dest
    wb_dest._add_sheet(sheet)

merge_all('./10-15-b5/')
merge_all('./10-15-b6/')
merge_all('./10-15-b72/')

# Save the file
wb_dest.save("sample.xlsx")
