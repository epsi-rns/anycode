#!/usr/bin/env bash

function get_dzen2_parameters() { 
    xpos=0
    ypos=0
    width=640
    height=24

    fgcolor="#000000"
    bgcolor="#ffffff"
    font="-*-fixed-medium-*-*-*-12-*-*-*-*-*-*-*"

    parameters="  -x $xpos -y $ypos -w $width -h $height" 
    parameters+=" -fn $font"
    parameters+=" -ta c -bg $bgcolor -fg $fgcolor"
#   parameters+=" -title-name dzentop"
}

function generated_output() {
    # endless loop
    while :; do 
      date +'%a %b %d %H:%M:%S'
      sleep 1
    done
}

function run_dzen2() {
    get_dzen2_parameters    
    command_out="dzen2 $parameters"
    
    {
        generated_output 
    } | $command_out
}

function detach_dzen2() {
	# not exactly a fork
    run_dzen2 &
}

# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----
# main

# remove all dzen2 instance
pkill dzen2

# run process in the background
detach_dzen2
