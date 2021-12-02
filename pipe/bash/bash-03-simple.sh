#!/usr/bin/env bash

# endless loop
while :; do 
  date +'%a %b %d %H:%M:%S'
  sleep 1
done | dzen2 -ta l
