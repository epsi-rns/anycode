#!/usr/bin/env bash

generated_output() {
    # endless loop
    while :; do 
      date +'%a %b %d %H:%M:%S'
      sleep 1
    done
}

cmdout="less" # or dzen2 # or lemonbar

generated_output | $cmdout
