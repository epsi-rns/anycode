#!/usr/bin/env python3

# https://gist.github.com/waylan/2353749

import datetime
import time
import subprocess
import errno

timeformat = '{0:%Y-%m-%d %H:%M:%S}'

cmdout  = 'less' # or 'dzen2'

process = subprocess.Popen(
        [cmdout], 
        stdin  = subprocess.PIPE,
        shell  = True,
        universal_newlines=True
    )

try:
    while True:
        datestr = timeformat.format(datetime.datetime.now())
    
        try:
            process.stdin.write(datestr + '\n')
            process.stdin.flush()
        except IOError as e:
            if e.errno == errno.EPIPE or e.errno == errno.EINVAL:
                # Stop loop on "Invalid pipe" or "Invalid argument".
                # No sense in continuing with broken pipe.
                break
            else:
                # Raise any other error.
                raise
    
        time.sleep(1)

except KeyboardInterrupt:
    print("Press `q` to exit.")
    process.wait()


process.stdin.close()
process.wait()
