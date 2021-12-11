# coding: utf-8
from __future__ import unicode_literals
import math

blueScale = {
  0: 0xE3F2FD, 1: 0xBBDEFB, 2: 0x90CAF9,
  3: 0x64B5F6, 4: 0x42A5F5, 5: 0x2196F3,
  6: 0x1E88E5, 7: 0x1976D2, 8: 0x1565C0,
  9: 0x0D47A1
}

limeScale = {
  0: 0xF9FBE7, 1: 0xF0F4C3, 2: 0xE6EE9C,
  3: 0xDCE775, 4: 0xD4E157, 5: 0xCDDC39,
  6: 0xC0CA33, 7: 0xAFB42B, 8: 0x9E9D24,
  9: 0x827717
}

greenScale = {
  0: 0xE8F5E9, 1: 0xC8E6C9, 2: 0xA5D6A7,
  3: 0x81C784, 4: 0x66BB6A, 5: 0x4CAF50,
  6: 0x43A047, 7: 0x388E3C, 8: 0x2E7D32,
  9: 0x1B5E20
}

def _color_me(sheet, row, name_pred, name_prob):
  column_pred = sheet["%s%d" % (name_pred, row)]
  column_prob = sheet["%s%d" % (name_prob, row)]
  column_both = sheet["%s%d:%s%d" \
    % (name_pred, row,name_prob, row)]

  pred = column_pred.String
  prob = column_prob.Value
  
  if not (type(prob) == int or type(prob) == float): return
  colScale = math.floor(prob*10)

  if pred=='Female': 
    colorPick = blueScale[colScale]
  elif pred=='Male':
    colorPick = limeScale[colScale]
  elif pred=='Junior':
    colorPick = greenScale[4]
  elif pred=='Juvenile':
    colorPick = greenScale[3]
  elif pred=='Puppy':
    colorPick = greenScale[2]
  else: return

  column_both.CellBackColor = colorPick

def color_all():
  document   = XSCRIPTCONTEXT.getDocument()
  sheet      = document.Sheets["Combined"]

  rows = range(1, 60)
  for row in rows:
    _color_me(sheet, row, 'B', 'C')
    _color_me(sheet, row, 'D', 'E')
    _color_me(sheet, row, 'F', 'G')

