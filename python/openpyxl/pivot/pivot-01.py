import openpyxl
from openpyxl import load_workbook

wb = load_workbook('recap.xlsx')
ws = wb["Combined"]

puppy      = 0
juvenile   = 0
junior_04  = 0
junior_06  = 0
junior_08  = 0
female_02  = 0
female_04  = 0
female_06  = 0
female_08  = 0
male_02    = 0
male_04    = 0
male_06    = 0
male_08    = 0
total      = 0

# start: 3
# end:  43
rows = range(3, 43)
for row in rows:
  pred_col = ws['B'+str(row)]
  prob_col = ws['C'+str(row)]

  pred = pred_col.value
  prob = float(prob_col.value)

  if pred=='Female':
    if (0.2 <= prob < 0.4):
      female_02 += 1
    elif (0.4 <= prob < 0.6):
      female_04 += 1
    elif (0.6 <= prob < 0.8):
      female_06 += 1
    elif (0.8 <= prob <= 1):
      female_08 += 1
    else:
      raise Exception("Female not in range" + str(prob))
  elif pred=='Male':
    if (0.2 <= prob < 0.4):
      male_02 += 1
    elif (0.4 <= prob < 0.6):
      male_04 += 1
    elif (0.6 <= prob < 0.8):
      male_06 += 1
    elif (0.8 <= prob <= 1):
      male_08 += 1
    else:
      raise Exception("Male not in range" + str(prob))
  elif pred=='Junior':
    if (0.4 <= prob < 0.6):
      junior_04 += 1
    elif (0.6 <= prob < 0.8):
      junior_06 += 1
    elif (0.8 <= prob <= 1):
      junior_08 += 1
    else:
      raise Exception("Junior not in range" + str(prob))
  elif pred=='Juvenile':
    juvenile += 1
  elif pred=='Puppy':
    puppy += 1

total = puppy + juvenile \
      + junior_04 + junior_06 + junior_08 \
      + female_02  + female_04  + female_06 + female_08 \
      + male_02  + male_04  + male_06 + male_08

print('Puppy          : %3d' % puppy)
print('Juvenile       : %3d' % juvenile)
print('Junior 0.4-0.6 : %3d' % junior_04)
print('Junior 0.6-0.8 : %3d' % junior_06)
print('Junior 0.8-1.0 : %3d' % junior_08)
print('Female 0.2-0.4 : %3d' % female_02)
print('Female 0.4-0.6 : %3d' % female_04)
print('Female 0.6-0.8 : %3d' % female_06)
print('Female 0.8-1.0 : %3d' % female_08)
print('Male 0.2-0.4   : %3d' % male_02)
print('Male 0.4-0.6   : %3d' % male_04)
print('Male 0.6-0.8   : %3d' % male_06)
print('Male 0.8-1.0   : %3d' % male_08)
print('------------------------')
print('Total          : %3d' % total)
