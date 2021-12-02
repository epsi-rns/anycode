#!/usr/bin/env python3

import time

timeformat = '%Y-%m-%d %H:%M:%S'

while True:
    timestr = time.strftime(timeformat)
    print(timestr)
    time.sleep(1)

