#!/usr/bin/env python3

import os
import subprocess

dirname = os.path.dirname(os.path.abspath(__file__))
path    = dirname + "/../assets"
cmdin   = 'conky -c ' + path + '/conky.lua'

cmdout  = 'dzen2' # no less

cmd     = cmdin + ' | ' + cmdout

process = os.popen(cmd, 'r')

