from scripts.subprocess_wrapper import run_script, run_command

colors_templates = {
    ".Xdefaults.template": "~/.Xdefaults",
    ".Xresources.light.template": "~/.Xresources.light",
    ".Xresources.dark.template": "~/.Xresources.dark",
}

links = {
    "~/.bash_profile": ".bash_profile",
    "~/.bashrc": ".bashrc",
    "~/.config/mpv/mpv.conf": "mpv.conf",
    "~/.inputrc": ".inputrc",
    "~/.tmux.conf": ".tmux.conf",
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
