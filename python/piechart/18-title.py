import numpy as np
import matplotlib.pyplot as plt

from colors import *
from trainees import *
from helper import wedge_text

# plot pie chart
axes = plt.subplot()

wedges, texts, autotexts = axes.pie(
  trainees,
  labels  = None,
  colors  = colors,
  explode = explode,
  startangle=30,
  pctdistance=0.75,
  textprops=dict(color="#212121"),
  autopct = lambda percent: wedge_text(percent, total))

axes.legend(
  wedges, legends,
  title="Date/Location",
  loc="center left",
  bbox_to_anchor=(-0.6, 0.5, 0, 0))

axes.set_position([0.4, 0.1, 0.6, 0.9])

plt.suptitle("Participants in West Java Region",
  horizontalalignment='center',
  weight="bold",
  fontsize=12)
plt.title(   "Respondent = %d Trainees" % total,
  horizontalalignment='center',
  fontsize=9, y=-0.1)

plt.show()
