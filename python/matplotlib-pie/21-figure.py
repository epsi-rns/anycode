import numpy as np
import matplotlib.pyplot as plt

from colors import *
from trainees import *
from helper import wedge_text

# plot pie chart
fig, axes = plt.subplots(figsize=(8, 5))

wedges, texts, autotexts = axes.pie(
  trainees,
  labels  = None,
  colors  = colors,
  explode = explode,
  startangle=30,
  pctdistance=0.5,
  textprops=dict(color="#212121"),
  autopct = lambda percent: wedge_text(percent, total))

axes.legend(
  wedges, legends,
  title="Location",
  loc="center left",
  bbox_to_anchor=(-0.6, 0.5, 0, 0))

axes.set_position([0.4, 0.1, 0.6, 0.8])

plt.suptitle("Participants in West Java Region",
  horizontalalignment='center',
  weight="bold",
  fontsize=12)
plt.title(   "Respondent = %d Trainees" % total,
  horizontalalignment='center',
  fontsize=9, y=-0.1)

#draw circle
centre_circle = plt.Circle((0,0),0.80,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.show()
