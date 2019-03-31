from scripts.subprocess_wrapper import run_script, run_command

colors_templates = {
    ".ez_colors.template": "~/.ez_colors",
}

links = {
    "~/.bash_profile": ".bash_profile",
    "~/.bashrc": ".bashrc",
    "~/.config/mpv/mpv.conf": "mpv.conf",
    "~/.gdbinit": ".gdbinit",
    "~/.inputrc": ".inputrc",
    "~/.tmux.conf": ".tmux.conf",
    "~/.Xdefaults": ".Xdefaults",
    "~/.xprofile": ".xprofile",
    "~/.xbindkeysrc": ".xbindkeysrc",
    "/etc/X11/xorg.conf.d/00-custom-kdb.conf": "00-custom-kdb.conf",
}

note = '''
tmux
xsel
urxvt
redshift-gtk
python-xdg
xbindkeys
mpv
bash-completion
ibus: Ubuntu im-config, Untick Use system keyboard layout
tmux <prefix>-I'''


def setup():
    run_script("change-power-settings.sh")
    run_command("git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm")
    # Intel vtune
    run_command("echo kernel.yama.ptrace_scope=0 | sudo tee /etc/sysctl.d/10-ptrace.conf > /dev/null")
