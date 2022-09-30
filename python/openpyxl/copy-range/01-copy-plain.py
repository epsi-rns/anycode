import openpyxl
from openpyxl import load_workbook
from copy import copy

# Main: Program Entry Point
wb = load_workbook("source-en.xlsx")
ws = wb["Example"]

# Save the file
wb.save("target-en.xlsx")
