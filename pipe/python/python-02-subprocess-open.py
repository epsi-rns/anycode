#!/usr/bin/env python3

# https://pymotw.com/2/subprocess/

import os
import subprocess

dirname = os.path.dirname(os.path.abspath(__file__))
path    = dirname + "/../assets"
cmdin   = 'conky -c ' + path + '/conky.lua'

cmdout  = 'less -K' # or 'dzen2'

pipein = subprocess.Popen(
        [cmdin], 
        stdout = subprocess.PIPE, 
        stderr = subprocess.STDOUT,
        shell  = True,
        universal_newlines = True
    )

pipeout = subprocess.Popen(
        [cmdout],
        stdin  = pipein.stdout,
        shell  = True,
        universal_newlines = True
    )

# http://kendriu.com/how-to-use-pipes-in-python-subprocesspopen-objects

pipein.stdout.close()
outputs, errors = pipeout.communicate()

# avoid zombie apocalypse
pipeout.wait()
