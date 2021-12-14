import openpyxl
from openpyxl import load_workbook

wb = load_workbook('recap.xlsx')
ws = wb["Combined"]

def get_sample_init():
  # declare all local variables
  return {
    'puppy'    : 0,
    'juvenile' : 0,
    'junior'   : { 40: 0, 60: 0, 80:0 },
    'female'   : { 20: 0, 40: 0, 60: 0, 80:0 },
    'male'     : { 20: 0, 40: 0, 60: 0, 80:0 }
  }

def display_sample(s):
  str_ranges  = { 20: '0.2-0.4', 40: '0.4-0.6',
                  60: '0.6-0.8', 80: '0.8-1.0' }

  total = s['puppy'] + s['juvenile'] + sum(s['junior'].values()) \
        + sum(s['female'].values()) + sum(s['male'].values())

  print('Puppy            : %3d' % s['puppy'])
  print('Juvenile         : %3d' % s['juvenile'])
  for key in [40, 60, 80]:
    print('Junior %s   : %3d' % (str_ranges[key], s['junior'][key]))
  for key in [20, 40, 60, 80]:
    print('Female   %s : %3d' % (str_ranges[key], s['female'][key]))
  for key in [20, 40, 60, 80]:
    print('Male     %s : %3d' % (str_ranges[key], s['male'][key]))
  print('------------------------')
  print('Total            : %3d' % total)
  print()

def update_sample_count(pred, prob, s):
  probint   = int(prob*100)
  probfloor = probint - (probint % 20)

  if pred=='Female': 
    if   (0.2 <= prob <= 1): s['female'][probfloor] += 1
    else: raise Exception("Female not in range" + str(prob))
  elif pred=='Male':
    if   (0.2 <= prob <= 1): s['male'][probfloor] += 1
    else: raise Exception("Male not in range" + str(prob))
  elif pred=='Junior':
    if   (0.4 <= prob <= 1): s['junior'][probfloor] += 1
    else: raise Exception("Junior not in range" + str(prob))
  elif pred=='Juvenile':
    s['juvenile'] += 1
  elif pred=='Puppy':
    s['puppy'] += 1

  return s

def get_sample_count(rows, name_pred, name_prob, s):
  for row in rows:
    pred_col = ws[name_pred + str(row)]
    prob_col = ws[name_prob + str(row)]

    pred = pred_col.value

    if prob_col.value == None: continue
    else:
      prob = float(prob_col.value)
      s = update_sample_count(pred, prob, s)

  return s

def pivot_me(rows, name_pred, name_prob):
  s = get_sample_init()
  s = get_sample_count(rows, name_pred, name_prob, s)
  display_sample(s)

def main():
  r_start =  3
  r_stop  = 43
  rows = range(r_start, r_stop)

  print('First Pool')
  print('------------------------')
  pivot_me(rows, 'B', 'C')

  print('Second Pool')
  print('------------------------')
  pivot_me(rows, 'D', 'E')

  print('Third Pool')
  print('------------------------')
  pivot_me(rows, 'F', 'G')

main()
