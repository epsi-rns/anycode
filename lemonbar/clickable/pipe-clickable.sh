#!/usr/bin/env bash

generated_output() {
    # endless loop
    while :; do 
      time=$(date +'%a %b %d %H:%M:%S')
      echo "%{A:~/Documents/misc/pop-art.sh :}${time}%{A}"
      sleep 1
    done
}

cmdout="lemonbar -B #aaffffff -F #000000"

generated_output | $cmdout | sh
