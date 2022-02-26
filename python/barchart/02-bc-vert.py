import matplotlib.pyplot as plt
import numpy as np

# variable initialization

from MyColors import material
from MyPopulation import breeds, stages, transpose

puppy  = transpose[0]
width = 0.65

# plot vertical bar chart

axes = plt.subplot()

axes.bar(breeds, puppy, width,
  color=material['blue500'], label='Puppy')

# configure decoration property

axes.set_ylabel('Population')
axes.set_title('Puppies')
axes.set_position([0.1, 0.3, 0.85, 0.6])
axes.set_ylim([-1, 11])

plt.xticks(rotation='vertical')
plt.show()
