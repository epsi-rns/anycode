#!/usr/bin/env bash

dirname=$(dirname $(readlink -f "$0"))
path="$dirname/../assets"

cmdin="conky -c $path/conky.lua"
cmdout="less" # or dzen2 # or lemonbar

# my first pipe
$cmdin | $cmdout
