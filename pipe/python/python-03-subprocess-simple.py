#!/usr/bin/env python3

# https://gist.github.com/waylan/2353749

import datetime
import time
import subprocess

timeformat = '{0:%Y-%m-%d %H:%M:%S}'

cmdout  = 'less -K' # or 'dzen2' # or lemonbar

process = subprocess.Popen(
        [cmdout], 
        stdin  = subprocess.PIPE,
        shell  = True,
        universal_newlines=True
    )

while True:
    datestr = timeformat.format(datetime.datetime.now())
    
    process.stdin.write(datestr + '\n')
    process.stdin.flush()
    
    time.sleep(1)

process.stdin.close()
process.wait()
