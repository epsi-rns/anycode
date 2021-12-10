import openpyxl
import math
from mycolors import blueScaleFill, limeScaleFill, greenScaleFill
from openpyxl import load_workbook

# https://material.io/design/color/the-color-system.html#tools-for-picking-colors

wb = load_workbook('combined.xlsx')
ws = wb["Combined"]

def color_me(row, name_pred, name_prob):
  column_pred = ws[name_pred+str(row)]
  column_prob = ws[name_prob+str(row)]

  pred = column_pred.value
  prob = column_prob.value
  
  if not (type(prob) == int or type(prob) == float): return
  colScale = math.floor(prob*10)

  if pred=='Female': 
    column_pred.fill = blueScaleFill[colScale]
    column_prob.fill = blueScaleFill[colScale]
  elif pred=='Male':
    column_pred.fill = limeScaleFill[colScale]
    column_prob.fill = limeScaleFill[colScale]
  elif pred=='Junior':
    column_pred.fill = greenScaleFill[4]
    column_prob.fill = greenScaleFill[4]
  elif pred=='Juvenile':
    column_pred.fill = greenScaleFill[3]
    column_prob.fill = greenScaleFill[3]
  elif pred=='Puppy':
    column_pred.fill = greenScaleFill[2]
    column_prob.fill = greenScaleFill[2]

rows = range(1, 650)
for row in rows:
  color_me(row, 'B', 'C')
  color_me(row, 'D', 'E')
  color_me(row, 'F', 'G')

# Save the file
wb.save("sample.xlsx")
