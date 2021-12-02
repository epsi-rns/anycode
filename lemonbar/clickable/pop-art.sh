#! /bin/bash

# based on Addie script: 
# https://pastebin.com/a1z494zM

# global variable
art=''

function get_art() {
    local art_dirs art_dir arts

    local 	vlc_cache=~/.cache/vlc/art/artistalbum/
    local       album="$(mpc current --format %album%)"
    # local      file="$(mpc current --format %file%)"
    # local album_dir="${file%/*}"

    IFS=$'\n'
    art_dirs=($(find $vlc_cache -type d -name "$album" | sed 's/:.*//'))

    for art_dir in $art_dirs; do
        arts=($(find $art_dir -type f -name "art" | sed 's/:.*//')) 
        art=${arts[0]}
    done
    unset IFS

    # echo $art
    # example: this will show
    # /home/epsi/.cache/vlc/art/artistalbum/Avenged Sevenfold/Avenged Sevenfold/art
}

get_art
[[ -z "$art" ]] && exit 1

### --main--

cover_png=/tmp/cover.png
rm -f "$cover_png" 
convert "${art}" -resize 150 $cover_png

n30f -x 150 -y 150 $cover_png
