#!/usr/bin/env bash
if [ -x "$(command -v apt)" ]; then
  sudo apt install fzf ripgrep universal-ctags
elif [ -x "$(command -v dnf)" ]; then
  sudo dnf install fzf ripgrep ctags
elif [ -x "$(command -v pacman)" ]; then
  sudo pacman -S fzf ripgrep universal-ctags
else
  echo "fzf ripgrep universal-ctags"
fi
