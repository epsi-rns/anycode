# coding: utf-8
from __future__ import unicode_literals

class DogSample:
  str_ranges  = {  0: '0.0-0.2',
                  20: '0.2-0.4', 40: '0.4-0.6',
                  60: '0.6-0.8', 80: '0.8-1.0' }

  def __init__(self, sheet_name, rows):
    document   = XSCRIPTCONTEXT.getDocument()
    sheet_src  = document.Sheets[sheet_name]

    self.sheet_src = sheet_src
    self.rows      = rows

  def reset(self):
    self.sample = {
      'puppy'    : 0,
      'juvenile' : 0,
      'junior'   : { 40: 0, 60: 0, 80: 0 },
      'female'   : { 40: 0, 60: 0, 80: 0 },
      'male'     : { 0:  0, 20: 0, 40: 0, 60: 0, 80:0 }
    }

  def get_total(self):
    return self.sample['puppy'] \
         + self.sample['juvenile'] \
         + sum(self.sample['junior'].values()) \
         + sum(self.sample['female'].values()) \
         + sum(self.sample['male'].values())

  def display_to_console(self):
    # shorter form of sample variable
    s = self.sample
    sr = self.str_ranges

    print(self.title)
    print('------------------------')
    print('Puppy            : %3d' % s['puppy'])
    print('Juvenile         : %3d' % s['juvenile'])
    for key in [40, 60, 80]:
      print('Junior %s   : %3d' % (sr[key], s['junior'][key]))
    for key in [40, 60, 80]:
      print('Female   %s : %3d' % (sr[key], s['female'][key]))
    for key in [0, 20, 40, 60, 80]:
      print('Male     %s : %3d' % (sr[key], s['male'][key]))
    print('------------------------')
    print('Total            : %3d' % self.get_total())
    print()

  def update(self, pred, prob):
    # s is just a shorter form of sample variable
    s = self.sample

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

    self.sample = s

  def walk_each_row(self):
    for row in self.rows:
      column_pred = self.sheet_src[self.name_pred + str(row)]
      column_prob = self.sheet_src[self.name_prob + str(row)]

      pred = column_pred.String

      if column_prob.Value == None: continue
      else:
        prob = float(column_prob.Value)
        self.update(pred, prob)

  def prepare_sheet(self):
    document   = XSCRIPTCONTEXT.getDocument()
    sheets_dst = document.Sheets
    if not sheets_dst.hasByName('Pivot'):
      sheets_dst.insertNewByName('Pivot', 1)
    self.sheet_dst = sheets_dst['Pivot']

    desktop    = XSCRIPTCONTEXT.getDesktop()
    model      = desktop.getCurrentComponent()
    controller = model.getCurrentController()
    controller.setActiveSheet(self.sheet_dst)

    self.sheet_dst["B7"].String = 'Puppy'
    self.sheet_dst["B8"].String = 'Junior'
    self.sheet_dst["B11"].String = 'Female'
    self.sheet_dst["B14"].String = 'Male'
    self.sheet_dst["B19"].String = 'Total Result'

  def write_to_sheet(self):
    # shorter form of property
    s  = self.sample
    sr = self.str_ranges

    row_p = self.name_key_dest # row name: probability
    row_c = self.name_val_dest # row name: count value
    self.sheet_dst[row_p + '6'].String = 'Prob'
    self.sheet_dst[row_c + '6'].String = 'Count'

    self.sheet_dst[row_p + '7'].String = '1.0'
    self.sheet_dst[row_c + '7'].Value  = s['puppy']

    if s['juvenile'] > 0:
      self.sheet_dst[row_p + '10'].String = 'Juvenile'
      self.sheet_dst[row_c + '10'].Value  = s['juvenile']

    if sum(s['junior'].values()) > 0:
      for key in [40, 60, 80]:
        col = str(8+int(key/20)-2)
        self.sheet_dst[row_p + col].String = sr[key]
        self.sheet_dst[row_c + col].Value  = s['junior'][key]

    for key in [40, 60, 80]:
      if s['female'][key]:
        col = str(11+int(key/20)-2)
        self.sheet_dst[row_p + col].String = sr[key]
        self.sheet_dst[row_c + col].Value  = s['female'][key]

    for key in [0, 20, 40, 60, 80]:
      if s['male'][key]:
        col = str(14+int(key/20))
        self.sheet_dst[row_p + col].String = sr[key]
        self.sheet_dst[row_c + col].Value  = s['male'][key]

    self.sheet_dst[row_c + '19'].Value = self.get_total()

  def pivot(
    self, title,
    name_pred, name_prob,
    name_key_dest, name_val_dest
  ):
    self.title     = title
    self.name_pred = name_pred
    self.name_prob = name_prob
    self.name_key_dest = name_key_dest
    self.name_val_dest = name_val_dest

    self.reset()
    self.walk_each_row()
    self.display_to_console()
    self.write_to_sheet()

def main():
  r_start =  3
  r_stop  = 43
  rows = range(r_start, r_stop)

  sample = DogSample("Combined", rows)
  sample.prepare_sheet()
  sample.pivot('First Pool',  'B', 'C', 'C', 'D')
  sample.pivot('Second Pool', 'D', 'E', 'E', 'F')
  sample.pivot('Third Pool',  'F', 'G', 'G', 'H')
