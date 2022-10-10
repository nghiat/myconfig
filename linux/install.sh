#!/usr/bin/env bash
if [ -x "$(command -v apt)" ]; then
  sudo apt install xsel xbindkeys ibus-unikey rxvt-unicode
elif [ -x "$(command -v dnf)" ]; then
  sudo dnf install xsel xbindkeys ibus-unikey rxvt-unicode
elif [ -x "$(command -v pacman)" ]; then
  sudo pacman -S xsel xbindkeys ibus-unikey rxvt-unicode
else
  echo "xsel xbindkeys ibus-unikey rxvt-unicode"
fi
