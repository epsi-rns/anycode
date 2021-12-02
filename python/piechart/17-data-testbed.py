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
  autopct = lambda percent: wedge_text(percent, total))

axes.legend(
  wedges, legends,
  title="Date/Location",
  loc="center left",
  bbox_to_anchor=(-0.6, 0.5, 0, 0))

axes.set_position([0.4, 0, 0.6, 1])

plt.show()
