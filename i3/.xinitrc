#!/bin/sh
# Nvidia
xrandr --auto
[ -f ~/.xprofile ] && . ~/.xprofile
[ -f ~/gnome_keyring.sh ] && . ~/gnome_keyring.sh
exec i3
