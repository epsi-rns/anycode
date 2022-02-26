import matplotlib.pyplot as plt
import numpy as np

# variable initialization

from MyColors import material
from MyPopulation import breeds, stages, transpose

[puppy, junior, adult, mature] = transpose
width = 0.35

# plot vertical bar chart

axes = plt.subplot()

axes.bar(breeds, puppy,  width,
  color=material['blue500'],   label='Puppy')

axes.bar(breeds, junior, width,
  color=material['cyan500'],   label='Junior',
  bottom = puppy)

axes.bar(breeds, adult, width,
  color=material['green500'],  label='Adult',
  bottom = puppy + junior)

axes.bar(breeds, mature, width,
  color=material['teal500'], label='Mature',
  bottom = puppy + junior + adult)

# configure decoration property

axes.legend(
  loc="upper left",
  bbox_to_anchor=(1, 1, 0, 0))
axes.margins(x=0.1)

axes.set_ylabel('Population')
axes.set_title('Pet Stages')
axes.set_position([0.1, 0.3, 0.65, 0.6])
axes.set_ylim([-1, 25])

plt.xticks(rotation='vertical')
plt.show()
