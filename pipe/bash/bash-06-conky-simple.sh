#!/usr/bin/env bash

generated_output() {
    dirname=$(dirname $(readlink -f "$0"))
    path="$dirname/../assets"
    conky -c "$path/conky.lua"
}

# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----
# parameters

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
# parameters+=" -title-name dzentop"

# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----
# main

# remove all dzen2 instance
pkill dzen2

# execute dzen
generated_output | dzen2 $parameters &

# optional transparency
# sleep 1 && exec `(transset .8 -n dzentop >/dev/null 2>&1 &)` & 
