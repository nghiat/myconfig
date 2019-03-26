export PATH="/bin:/usr/bin:$PATH";
export EDITOR="vim"
export PS1="\[\e[1m\]\u:\w$ \[\e[0m\]"
# Avoid duplicates
export HISTCONTROL=ignoredups:erasedups
export HISTSIZE=100000
export HISTFILESIZE=100000
export PROMPT_COMMAND="history -a; history -c; history -r;"

# If not running interactively, do not do anything
[[ $- != *i* ]] && return

# Autocorrect typos when using cd
shopt -s cdspell;
# Append history
shopt -s histappend
# Check the window size after each command and, if neccessary,
# update the value of LINES and COLUMNS
shopt -s checkwinsize
# Disable Ctrl-S
stty -ixon

force_color_prompt=yes
# This has to be sourced before running tmux
source ~/.ez_colors
if [ -f ~/.ez_local ]; then
  source ~/.ez_local
fi

[[ -z "$TMUX" && -x "$(command -v tmux)" ]] && exec tmux
