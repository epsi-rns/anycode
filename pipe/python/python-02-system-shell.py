#!/usr/bin/env python3

import os

dirname = os.path.dirname(os.path.abspath(__file__))
path    = dirname + "/../assets"
cmdin   = 'conky -c ' + path + '/conky.lua'

cmdout  = 'less' # or 'dzen2'

cmd     = cmdin + ' | ' + cmdout

os.system(cmd)
