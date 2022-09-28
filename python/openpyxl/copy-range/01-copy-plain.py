import openpyxl
from openpyxl import load_workbook
from copy import copy

# Main: Program Entry Point
wb = load_workbook("source.xlsx")
ws = wb["Example"]

# Save the file
wb.save("target.xlsx")
