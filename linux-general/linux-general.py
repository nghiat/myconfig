from scripts.subprocess_wrapper import run_script, run_command

colors_templates = {
    ".ez_colors.template": "~/.ez_colors",
}

links = {
    "~/.bash_profile": ".bash_profile",
    "~/.bashrc": ".bashrc",
    "~/.config/mpv/mpv.conf": "mpv.conf",
    "~/.config/pulse/default.pa": "default.pa",
    "~/.gdbinit": ".gdbinit",
    "~/.inputrc": ".inputrc",
    "~/.tmux.conf": ".tmux.conf",
    "~/.Xdefaults": ".Xdefaults",
    "~/.xprofile": ".xprofile",
    "~/.xbindkeysrc": ".xbindkeysrc",
}

note = '''
tmux
xsel
urxvt
redshift
python-xdg
xbindkeys
mpv
bash-completion
ibus: Ubuntu im-config, Untick Use system keyboard layout
tmux <prefix>-I
dropbox
pulseaudio
pulseaudio-alsa
google-chrome
systemd-timesyncd
noto-fonts
noto-fonts-cjk
gem install tmuxinator'''


def setup():
    run_script("change-power-settings.sh")
    run_command("git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm")
    # Intel vtune
    run_command("echo kernel.yama.ptrace_scope=0 | sudo tee /etc/sysctl.d/10-ptrace.conf > /dev/null")
    run_command("cp ~/myconfig/linux-general/.tmux_local.conf ~")
