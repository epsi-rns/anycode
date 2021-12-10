# coding: utf-8
from __future__ import unicode_literals

def context_test():
  # set global variables for context
  global desktop
  global model
  global active_sheet

  # get the doc from the scripting context
  # which is made available to all scripts
  desktop = XSCRIPTCONTEXT.getDesktop()
  model = desktop.getCurrentComponent()

  # access the active sheet
  active_sheet = model.CurrentController.ActiveSheet

def query_sheet():
  all_sheets = model.Sheets
  print("Total of %d sheets" % len(all_sheets))
  sheetnames = [s.Name for s in all_sheets]
  print(sheetnames)

def rename_sheet_test():
  active_sheet.Name = "Blewah"

def copy_sheet_test():
  all_sheets = model.Sheets
  all_sheets.copyByName(
    "Blewah", "BlewahKopi", len(all_sheets))

def open_calc_test():
  desktop = XSCRIPTCONTEXT.getDesktop()
  model = desktop.loadComponentFromURL(
    "private:factory/scalc", "_blank", 0, ())

def copy_out_sheet_test():
  desktop = XSCRIPTCONTEXT.getDesktop()
  
  model_src = desktop.getCurrentComponent()  
  first_sheet = model_src.Sheets[0]

  model_dst = desktop.loadComponentFromURL(
    "private:factory/scalc", "_blank", 0, ())

  model_dst.Sheets.importSheet(
    model_src, first_sheet.Name, 0)

  print(model_src.getLocation())

  model_dst.storeToURL(
    "file:///home/epsi/Test.ods", ())

def copy_out_first_sheet_test():
  desktop = XSCRIPTCONTEXT.getDesktop()
  
  model_src   = desktop.getCurrentComponent()  
  first_sheet = model_src.Sheets[0]
  sheet_name  = first_sheet.Name

  model_dst   = desktop.loadComponentFromURL(
    "private:factory/scalc", "_blank", 0, ())

  model_dst.Sheets.importSheet(
    model_src, sheet_name, 0)

  base_url = "file:///home/epsi/monthly/"
  full_url = "%s%s.ods" % (base_url, sheet_name)
  print(full_url)

  model_dst.storeToURL(full_url, ())
  model_dst.close(True)

def open_ods_file():
  desktop  = XSCRIPTCONTEXT.getDesktop()
  file_url = "file:///home/epsi/monthly.ods"
  model = desktop.loadComponentFromURL(
    file_url, '_default', 0, ())

def query_files_test():
  import os
  from os import listdir
  from os.path import isfile, join
  import pprint

  path = '/home/epsi/monthly/'

  onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
  onlyods   = [f for f in onlyfiles if '.ods' in f]
  onlyods.sort()

  my_print  = pprint.PrettyPrinter(width=60, compact=True)
  my_print.pprint(onlyods)

# Main
context_test()
