import openpyxl
from openpyxl import load_workbook

wb = load_workbook('recap.xlsx')
ws = wb["Combined"]

puppy    = 0
juvenile = 0
junior   = { '04': 0, '06': 0, '08': 0 }
female   = { '02': 0, '04': 0, '06': 0, '08':0 }
male     = { '02': 0, '04': 0, '06': 0, '08':0 }
total    = 0

# start: 3
# end:  43
rows = range(3, 43)
for row in rows:
  pred_col = ws['D'+str(row)]
  prob_col = ws['E'+str(row)]

  pred = pred_col.value
  prob = float(prob_col.value)

  if pred=='Female':
    if   (0.2 <= prob < 0.4): female['02'] += 1
    elif (0.4 <= prob < 0.6): female['04'] += 1
    elif (0.6 <= prob < 0.8): female['06'] += 1
    elif (0.8 <= prob <= 1):  female['08'] += 1
    else: raise Exception("Female not in range" + str(prob))
  elif pred=='Male':
    if   (0.2 <= prob < 0.4): male['02'] += 1
    elif (0.4 <= prob < 0.6): male['04'] += 1
    elif (0.6 <= prob < 0.8): male['06'] += 1
    elif (0.8 <= prob <= 1):  male['08'] += 1
    else: raise Exception("Male not in range" + str(prob))
  elif pred=='Junior':
    if   (0.4 <= prob < 0.6): junior['04'] += 1
    elif (0.6 <= prob < 0.8): junior['06'] += 1
    elif (0.8 <= prob <= 1) : junior['08'] += 1
    else: raise Exception("Junior not in range" + str(prob))
  elif pred=='Juvenile':
    juvenile += 1
  elif pred=='Puppy':
    puppy += 1

total = puppy + juvenile + sum(junior.values()) \
      + sum(female.values()) + sum(male.values())

print('Puppy          : %3d' % puppy)
print('Juvenile       : %3d' % juvenile)
print('Junior 0.4-0.6 : %3d' % junior['04'])
print('Junior 0.6-0.8 : %3d' % junior['06'])
print('Junior 0.8-1.0 : %3d' % junior['08'])
print('Female 0.2-0.4 : %3d' % female['02'])
print('Female 0.4-0.6 : %3d' % female['04'])
print('Female 0.6-0.8 : %3d' % female['06'])
print('Female 0.8-1.0 : %3d' % female['08'])
print('Male 0.2-0.4   : %3d' % male['02'])
print('Male 0.4-0.6   : %3d' % male['04'])
print('Male 0.6-0.8   : %3d' % male['06'])
print('Male 0.8-1.0   : %3d' % male['08'])
print('------------------------')
print('Total          : %3d' % total)
