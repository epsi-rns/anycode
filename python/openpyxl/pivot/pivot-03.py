import openpyxl
from openpyxl import load_workbook

wb = load_workbook('recap.xlsx')
ws = wb["Combined"]

def pivot_me(rows, name_pred, name_prob):

  # declare all local variables
  puppy       = 0
  juvenile    = 0
  junior      = { 40: 0, 60: 0, 80:0 }
  female      = { 20: 0, 40: 0, 60: 0, 80:0 }
  male        = { 20: 0, 40: 0, 60: 0, 80:0 }
  total       = 0
  str_ranges  = { 20: '0.2-0.4', 40: '0.4-0.6',
                  60: '0.6-0.8', 80: '0.8-1.0' }

  for row in rows:
    pred_col = ws[name_pred + str(row)]
    prob_col = ws[name_prob + str(row)]

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
      if   (0.2 <= prob <= 1): male[probfloor] += 1
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

  print('Puppy            : %3d' % puppy)
  print('Juvenile         : %3d' % juvenile)
  for key in [40, 60, 80]:
    print('Junior %s   : %3d' % (str_ranges[key], junior[key]))
  for key in [20, 40, 60, 80]:
    print('Negative %s : %3d' % (str_ranges[key], female[key]))
  for key in [20, 40, 60, 80]:
    print('Positive %s : %3d' % (str_ranges[key], male[key]))
  print('------------------------')
  print('Total            : %3d' % total)
  print()

# start: 3
# end:  43
rows = range(3, 43)

print('First Pool')
print('------------------------')
pivot_me(rows, 'B', 'C')

print('Second Pool')
print('------------------------')
pivot_me(rows, 'D', 'E')

print('Third Pool')
print('------------------------')
pivot_me(rows, 'F', 'G')
