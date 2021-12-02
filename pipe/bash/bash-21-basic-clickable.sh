#!/usr/bin/env bash

# endless loop
while true; do 
    time=$(date +'%a %b %d %H:%M:%S')
    echo "%{A:cal}${time}%{A}"
    sleep 1
done


