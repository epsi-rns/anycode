# coding: utf-8
from __future__ import unicode_literals

def split_sheets():
  base_url = "file:///home/epsi/monthly/"
  desktop = XSCRIPTCONTEXT.getDesktop()

  model_src   = desktop.getCurrentComponent()
  all_sheets = model_src.Sheets
  print("Total of %d sheets" % len(all_sheets))

  for sheet in all_sheets:
    sheet_name  = sheet.Name

    model_dst   = desktop.loadComponentFromURL(
      "private:factory/scalc", "_blank", 0, ())
    first_sheet_name = model_dst.Sheets[0].Name

    model_dst.Sheets.importSheet(
      model_src, sheet_name, 0)
    model_dst.Sheets.removeByName(
      first_sheet_name)

    full_url = "%s%s.ods" % (base_url, sheet_name)
    print(full_url)

    model_dst.storeToURL(full_url, ())
    model_dst.close(True)

def merge_sheets():
  import os
  from os import listdir
  from os.path import isfile, join
  import pprint

  desktop     = XSCRIPTCONTEXT.getDesktop()
  model_dst   = desktop.loadComponentFromURL(
      "private:factory/scalc", "_blank", 0, ())
  first_sheet = model_dst.Sheets[0]
  
  # write something, do not delete this line
  first_sheet.getCellRangeByName(
    "A1").String = "Hello World!"

  path = '/home/epsi/monthly/'

  onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
  onlyods   = [f for f in onlyfiles if '.ods' in f]
  onlyods.sort(reverse=True)

  my_print  = pprint.PrettyPrinter(width=60, compact=True)
  my_print.pprint(onlyods)

  for file_name in onlyods:
    sheet_name = os.path.splitext(file_name)[0]
    file_url = "file://" + path + file_name
    print(file_url)

    model_src = desktop.loadComponentFromURL(
      file_url, '_default', 0, ())
    model_dst.Sheets.importSheet(
      model_src, sheet_name, 0)
    model_src.close(True)

  model_dst.Sheets.removeByName(
    first_sheet.Name)
