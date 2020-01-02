#!/bin/sh
# Nvidia
xrandr --auto
[ -f ~/.xprofile ] && . ~/.xprofile
exec i3
