#!/usr/bin/env python3

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
    outputs, errors = pipeout.communicate()
    
    # avoid zombie apocalypse
    pipeout.wait()

def detach_dzen2():
    pid = os.fork()
    
    if pid == 0:
        try:
            run_dzen2()
            os._exit(1)
        finally:
            os.kill(pid, signal.SIGTERM)

def detach_transset():
    pid = os.fork()
    
    if pid == 0:
        try:
            time.sleep(1)
            os.system('transset .8 -n dzentop >/dev/null')
            os._exit(1)
        finally:
            os.kill(pid, signal.SIGTERM)

# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----
# main

# remove all dzen2 instance
os.system('pkill dzen2')

# run process in the background
detach_dzen2()

# optional transparency
# detach_transset()
