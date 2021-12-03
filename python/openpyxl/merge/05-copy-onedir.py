import os
from os import listdir
from os.path import isfile, join

import openpyxl
from openpyxl import load_workbook
from openpyxl import Workbook

wb_dest   = load_workbook('./empty.xlsx')
path = './10-15-b5/'

onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
onlyxlxs  = [f for f in onlyfiles if '.xlsx' in f]

for f in onlyxlxs:
  wb_source = load_workbook(join(path, f))
  noext = os.path.splitext(f)[0]

  # Rename first sheet
  sheet = wb_source.worksheets[0] 
  sheet.title = noext

  sheet._parent = wb_dest
  wb_dest._add_sheet(sheet)

# Save the file
wb_dest.save("sample.xlsx")

