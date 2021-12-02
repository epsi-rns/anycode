import numpy as np
import matplotlib.pyplot as plt

# data structure
trainees  = [50, 31, 28, 50, 10, 46, 38, 47]
total     = sum(trainees)
locations = [
  'Bandung', 'Banjar', 'Bekasi', 'Bogor', 
  'Cimahi',  'Cirebon', 'Depok', 'Sukabumi']
colors = {
  '#F44336', '#E91E63', '#9C27B0', '#3F51B5',
  '#2196F3', '#00BCD4', '#009688', '#4CAF50',
  '#CDDC39', '#FF9800' }
explode = [0.1, 0.1, 0.1, 0.1,
           0.2, 0.1, 0.1, 0.1]

# additional function
def wedge_text(percent, total):
    absolute = int(round(total*percent/100))
    if percent > 10:
      return "{:.1f}%\n({:d})".format(percent, absolute)
    else:
      return ""

# plot pie chart
axes = plt.subplot()

wedges, texts, autotexts = axes.pie(
  trainees,
  labels  = locations,
  colors  = colors,
  explode = explode,
  autopct = lambda percent: wedge_text(percent, total))

plt.show()
