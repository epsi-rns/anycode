import os
import openpyxl
from openpyxl import load_workbook

loadname = 'monthly.xlsx'
noext = os.path.splitext(loadname)[0]

try: 
  os.mkdir(noext)
except OSError as error:
  print(error)

wb_loop = load_workbook(loadname)
savename = ""

for index_loop, sheet_loop in enumerate(
  wb_loop.worksheets, start=1):

  if index_loop == 2:
    print("Keep %2d: %s" % (index_loop, sheet_loop.title))
    savename = "%s.xlsx" % sheet_loop.title
  else:
    wb_loop.remove(sheet_loop)

# Save the file
if savename:
  wb_loop.save("./%s/%s" % (noext, savename))
  print("%s saved" % savename)
else:
  print("No sheet saved")
