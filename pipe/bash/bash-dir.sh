#!/usr/bin/env bash

echo $0
dirname "$0"

dirname=$(dirname $(readlink -f "$0"))
echo $dirname

path="$dirname/../assets"
echo $path

