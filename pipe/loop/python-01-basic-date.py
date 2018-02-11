#!/usr/bin/env python3

import datetime
from time import sleep

timeformat = '{0:%Y-%m-%d %H:%M:%S}'

while True:
    datestr = timeformat.format(datetime.datetime.now())
    print(datestr)
    sleep(1)

