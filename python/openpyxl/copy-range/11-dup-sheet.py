import openpyxl
from openpyxl import load_workbook

# Main: Program Entry Point
wb = load_workbook("data.xlsx")
ws_template = wb["Empty"]
ws_source   = wb["Source"]
ws_target   = wb.copy_worksheet(ws_template)
ws_target.title = "Target"

# Save the file
wb.save("result.xlsx")
