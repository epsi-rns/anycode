#!/usr/bin/env python3

import datetime
import time
import subprocess
import os
import signal

def get_lemon_parameters():
    # geometry: -g widthxheight+x+y
    xpos     = '0'
    ypos     = '0'
    width    = '640'
    height   = '24'

    geom_res = width + 'x' + height + '+' + xpos + '+' + ypos

    # color, with transparency
    fgcolor  = "'#000000'"
    bgcolor  = "'#aaffffff'"

    # XFT: require lemonbar_xft_git 
    font     = "monospace-9"

    # finally
    parameters  = ' -g ' + geom_res + ' -u 2 ' \
                + ' -B ' + bgcolor  + ' -F ' + fgcolor \
                + ' -f ' + font

    return parameters

def generated_output(pipeout):
    dirname = os.path.dirname(os.path.abspath(__file__))
    path    = dirname + "/../assets"
    cmdin   = 'conky -c ' + path + '/conky.lua'

    pipein = subprocess.Popen(
            [cmdin], 
            stdout = pipeout.stdin,
            stderr = subprocess.STDOUT,
            shell  = True,
            universal_newlines = True
        )

def run_lemon():
    cmdout  = 'lemonbar '+get_lemon_parameters()

    pipeout = subprocess.Popen(
            [cmdout], 
            stdin  = subprocess.PIPE,
            shell  = True,
            universal_newlines=True
        )

    generated_output(pipeout)

    pipeout.stdin.close()
    outputs, errors = pipeout.communicate()
    
    # avoid zombie apocalypse
    pipeout.wait()

def detach_lemon():
    pid = os.fork()
    
    if pid == 0:
        try:
            run_lemon()
            os._exit(1)
        finally:
            import signal
            os.kill(pid, signal.SIGTERM)

# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----
# main

# remove all lemon instance
os.system('pkill lemonbar')

# run process in the background
detach_lemon()
