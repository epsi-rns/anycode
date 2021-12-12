import openpyxl
import math
from openpyxl import Workbook
from openpyxl import load_workbook

wb = load_workbook('recap.xlsx')
ws = wb["Combined"]

# start: 3
# end:  43
rows = range(3, 43)

def pivot_me(rows, name_pred_source, name_prob_source,
             worksheet, name_key_dest, name_val_dest):

  # declare all local variables
  puppy      = 0
  juvenile   = 0
  junior     = { 40: 0, 60: 0, 80:0 }
  female     = { 40: 0, 60: 0, 80:0 }
  male       = { 0:0, 20: 0, 40: 0, 60: 0, 80:0 }
  total      = 0
  str_ranges = {  0: '0.0-0.2', 20: '0.2-0.4' , 40: '0.4-0.6',
                 60: '0.6-0.8', 80: '0.8-1.0' }

  for row in rows:
    pred_col = ws[name_pred_source + str(row)]
    prob_col = ws[name_prob_source + str(row)]

    pred = pred_col.value

    if prob_col.value == None: continue
    else:
      prob = float(prob_col.value)
      probint   = int(prob*100)
      probfloor = probint - (probint % 20)

    if pred=='Female': 
      if   (0.2 <= prob <= 1): female[probfloor] += 1
      else: raise Exception("Female not in range" + str(prob))
    elif pred=='Male':
      if   (0 <= prob <= 1): male[probfloor] += 1
      else: raise Exception("Male not in range" + str(prob))
    elif pred=='Junior':
      if   (0.4 <= prob <= 1): junior[probfloor] += 1
      else: raise Exception("Junior not in range" + str(prob))
    elif pred=='Juvenile':
      juvenile += 1
    elif pred=='Puppy':
      puppy += 1

  total = puppy + juvenile + sum(junior.values()) \
        + sum(female.values()) + sum(male.values())

  row_p = name_key_dest # row name: probability
  row_c = name_val_dest # row name: count value
  worksheet[row_p + '2']  = 'Prob'
  worksheet[row_c + '2']  = 'Count'

  worksheet[row_p + '3']  = '1.0'
  worksheet[row_c + '3']  = puppy

  if juvenile > 0:
    worksheet[row_p + '6']  = 'Juvenile'
    worksheet[row_c + '6']  = juvenile

  if sum(junior.values()) > 0:
    for key in [40, 60, 80]:
      col = str(4+int(key/20)-2)
      worksheet[row_p + col]  = str_ranges[key]
      worksheet[row_c + col]  = junior[key]

  for key in [40, 60, 80]:
    col = str(7+int(key/20)-2)
    worksheet[row_p + col]  = str_ranges[key]
    worksheet[row_c + col]  = female[key]

  for key in [0, 20, 40, 60, 80]:
    if male[key]:
      col = str(10+int(key/20))
      worksheet[row_p + col]  = str_ranges[key]
      worksheet[row_c + col]  = male[key]

  worksheet[row_c + '15']  = total

# ----

new_wb = Workbook()

# grab the active worksheet
new_ws = new_wb.active

row_name = 'B'
new_ws[row_name + '3']  = 'Puppy'
new_ws[row_name + '4']  = 'Junior'
new_ws[row_name + '7']  = 'Female'
new_ws[row_name + '10'] = 'Male'
new_ws[row_name + '15'] = 'Total Result'

print('First Pool')
pivot_me(rows, 'B', 'C', new_ws, 'C', 'D')

print('Second Pool')
pivot_me(rows, 'D', 'E', new_ws, 'E', 'F')

print('Third Pool')
pivot_me(rows, 'F', 'G', new_ws, 'G', 'H')


# Save the file
new_wb.save("sample.xlsx")
