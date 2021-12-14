# coding: utf-8
from __future__ import unicode_literals

class DogSample:
  def __init__(self):
    document = XSCRIPTCONTEXT.getDocument()
    self.sheet_src = document.Sheets["Combined"]
    
  def display(self):
    sheet = self.sheet_src

    name_pred = 'B'
    name_prob = 'C'
    rows = range(3, 8)
    for row in rows:
      column_pred = sheet["%s%d" % (name_pred, row)]
      column_prob = sheet["%s%d" % (name_prob, row)]

      pred = column_pred.String
      prob = column_prob.Value
  
      if not (type(prob) == int or type(prob) == float): continue

      print(f'Prediction  : {pred}')
      print(f'Probability : {prob:.2f}')


def main():
  sample = DogSample()
  sample.display()
