import openpyxl
import math
from openpyxl import load_workbook
from mycolors import blueScaleFill, limeScaleFill, greenScaleFill

wb = load_workbook('combined.xlsx')
ws = wb["Combined"]

b3 = ws['B3']
c3 = ws['C3']

print(b3.value)
print(c3.value)

pred = b3.value
prob = c3.value
colScale = math.floor(prob*10)

if pred=='Female': 
  ws['B3'].fill = blueScaleFill[colScale]
  ws['C3'].fill = blueScaleFill[colScale]
elif pred=='Male':
  ws['B3'].fill = limeScaleFill[colScale]
  ws['C3'].fill = limeScaleFill[colScale]
elif pred=='Junior':
  ws['B3'].fill = greenScaleFill[400]
  ws['C3'].fill = greenScaleFill[400]
elif pred=='Juvenile':
  ws['B3'].fill = greenScaleFill[300]
  ws['C3'].fill = greenScaleFill[300]
elif pred=='Puppy':
  ws['B3'].fill = greenScaleFill[200]
  ws['C3'].fill = greenScaleFill[200]

# Save the file
wb.save("sample.xlsx")



