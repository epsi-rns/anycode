import os
from os import listdir
from os.path import isfile, join
import pprint

path = './monthly/'

onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
onlyxlxs  = [f for f in onlyfiles if '.xlsx' in f]
onlyxlxs.sort()

my_print  = pprint.PrettyPrinter(width=60, compact=True)
my_print.pprint(onlyxlxs)

