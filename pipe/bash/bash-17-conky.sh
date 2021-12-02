#!/usr/bin/env bash

function get_lemon_parameters() { 
    # geometry: -g widthxheight+x+y
    xpos=0
    ypos=0
    width=640
    height=24
    
    geom_res="${width}x${height}+${xpos}+${ypos}"    

    # color, with transparency
    fgcolor="#000000"
    bgcolor="#aaffffff"

    # XFT: require lemonbar_xft_git 
    local font="monospace-9"

    # finally
    parameters="  -g $geom_res -u 2"
    parameters+=" -B $bgcolor -F $fgcolor" 
    parameters+=" -f $font" 
}

function generated_output() {
    dirname=$(dirname $(readlink -f "$0"))
    path="$dirname/../assets"
    conky -c "$path/conky.lua"
}

function run_lemon() {
    get_lemon_parameters    
    command_out="lemonbar $parameters"
    
    {
        generated_output 
    } | $command_out
}

function detach_lemon() {    
    run_lemon &
}

# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----
# main

# remove all lemon instance
pkill lemonbar

# run process in the background
detach_lemon
