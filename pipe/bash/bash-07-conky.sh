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
    dirname=$(dirname $(readlink -f "$0"))
    path="$dirname/../assets"
    conky -c "$path/conky.lua"
}

function run_dzen2() {
    get_dzen2_parameters    
    command_out="dzen2 $parameters"
    
    {
        generated_output 
    } | $command_out
}

function detach_dzen2() {    
    run_dzen2 &
}

function detach_transset() { 
    {
        sleep 1
    
        # you may use either xorg-transset or transset-df instead
        # https://github.com/wildefyr/transset-df    
        exec `(transset .8 -n dzentop >/dev/null)`
    } &
}

# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----
# main

# remove all dzen2 instance
pkill dzen2

# run process in the background
detach_dzen2

# optional transparency
# detach_transset
