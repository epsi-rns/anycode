import numpy as np

population = {
  "Labradors"   : [ 10,  0,  0,  0],
  "Bulldogs"    : [ 10,  0,  0,  0],
  "Shepherd"    : [  4, 14,  0,  0],
  "Retrievers"  : [  2, 10,  3,  1],
  "Poodles"     : [  4,  8, 12,  0],
  "Beagles"     : [  0,  0, 10,  0],
  "Rottweilers" : [  0,  0, 10,  0],
  "Pointers"    : [  1,  0,  9,  0],
  "Dachshunds"  : [  0,  0,  9,  0],
  "Terriers"    : [  3,  0,  7,  0],
  "Boxers"      : [  0,  2,  4, 10],
  "Huskies"     : [  0,  0,  1,  0],
  "Spaniels"    : [  2,  1,  0,  0],
  "Doberman"    : [  9,  0,  0,  0],
}

breeds    = list(population.keys())
stages    = list(population.values())
transpose = np.array(stages).T
