#!/usr/bin/env bash
if [ -x "$(command -v apt)" ]; then
  sudo apt install tmux
elif [ -x "$(command -v dnf)" ]; then
  sudo dnf install tmux
elif [ -x "$(command -v pacman)" ]; then
  sudo pacman -S tmux
else
  echo "tmux"
fi
