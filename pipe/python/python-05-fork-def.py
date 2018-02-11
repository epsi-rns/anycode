#!/usr/bin/env python3

# https://gist.github.com/waylan/2353749

import datetime
import time
import subprocess
import os
import signal

def get_dzen2_parameters():
    xpos    = '0'
    ypos    = '0'
    width   = '640'
    height  = '24'
    fgcolor = '#000000'
    bgcolor = '#ffffff'
    font    = '-*-fixed-medium-*-*-*-12-*-*-*-*-*-*-*'

    parameters  = '  -x '+xpos+' -y '+ypos+' -w '+width+' -h '+ height
    parameters += " -fn '"+font+"'"
    parameters += " -ta c -bg '"+bgcolor+"' -fg '"+fgcolor+"'"
#   parameters += ' -title-name dzentop'

    return parameters;

def generated_output(process):
    timeformat = '{0:%Y-%m-%d %H:%M:%S}'

    while True:
        datestr = timeformat.format(datetime.datetime.now())
    
        process.stdin.write(datestr + '\n')
        process.stdin.flush()
    
        time.sleep(1)

def run_dzen2():
    cmdout  = 'dzen2 '+get_dzen2_parameters()

    pipeout = subprocess.Popen(
            [cmdout], 
            stdin  = subprocess.PIPE,
            shell  = True,
            universal_newlines=True
        )

    generated_output(pipeout)

    pipeout.stdin.close()
    
    # avoid zombie apocalypse
    pipeout.wait()

def detach_dzen2():
    pid = os.fork()
    
    if pid == 0:
        try:
            run_dzen2()
        finally:
            os.kill(pid, signal.SIGTERM)

# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----
# main

# remove all dzen2 instance
os.system('pkill dzen2')

detach_dzen2()
