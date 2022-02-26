import matplotlib.pyplot as plt
import numpy as np

# variable initialization

from MyColors import material
from MyPopulation import breeds, stages, transpose

puppy  = transpose[0]
width = 0.65

# plot horizontal bar chart

fig, axes = plt.subplots()
y_pos = np.arange(len(breeds))

axes.barh(y_pos, puppy, width,
  color=material['blue500'], label='Puppy')
  
# configure decoration property

axes.set_yticks(y_pos, labels=breeds)
axes.invert_yaxis()
axes.set_xlabel('Population')
axes.set_title('Puppies')
axes.set_position([0.15, 0.1, 0.80, 0.8])
axes.set_xlim([-1, 11])

plt.show()
