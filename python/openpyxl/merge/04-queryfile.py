import os
from os import listdir
from os.path import isfile, join

path = './10-15-b5/'

onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
onlyxlxs  = [f for f in onlyfiles if '.xlsx' in f]

for f in onlyxlxs:
  noext = os.path.splitext(f)[0]
  print(noext)

