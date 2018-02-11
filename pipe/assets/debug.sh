#!/usr/bin/env bash

generated_output() {
	dirname=$(dirname $(readlink -f "$0"))
    conky -c ${dirname}/conky-dzen2-debug.lua
}

# ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----
# execute

clear
generated_output


