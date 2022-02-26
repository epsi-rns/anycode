import matplotlib.pyplot as plt
import numpy as np

# variable initialization

from MyColors import material
from MyPopulation import breeds, stages, transpose

[puppy, junior, adult, mature] = transpose
width = 0.35

# plot horizontal bar chart

axes = plt.subplot()
y_pos = np.arange(len(breeds))

axes.barh(y_pos, puppy, width,
  color=material['blue500'],   label='Puppy')

axes.barh(y_pos, junior, width,
  color=material['cyan500'],   label='Junior',
  left = puppy)

axes.barh(y_pos, adult, width,
  color=material['green500'],  label='Adult',
  left = puppy + junior)

axes.barh(y_pos, mature, width,
  color=material['teal500'], label='Mature',
  left = puppy + junior + adult)
  
# configure decoration property

axes.legend(
  loc="upper left",
  bbox_to_anchor=(1, 1, 0, 0))
axes.margins(x=0.1)

axes.set_yticks(y_pos, labels=breeds)
axes.invert_yaxis()
axes.set_xlabel('Population')
axes.set_title('Pet Stages')
axes.set_position([0.15, 0.1, 0.60, 0.8])
axes.set_xlim([-1, 25])

plt.show()
