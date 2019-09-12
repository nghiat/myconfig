from scripts.subprocess_wrapper import run_script, run_command

colors_templates = {
    ".ez_colors.template": "~/.ez_colors",
}

links = {
    "~/.bash_profile": ".bash_profile",
    "~/.config/mpv/mpv.conf": "mpv.conf",
    "~/.config/pulse/default.pa": "default.pa",
    "~/.Xdefaults": ".Xdefaults",
    "~/.xprofile": ".xprofile",
    "~/.xbindkeysrc": ".xbindkeysrc",
}

note = '''
xsel
urxvt
redshift
python-xdg
xbindkeys
mpv
bash-completion
ibus: Ubuntu im-config, Untick Use system keyboard layout
dropbox
pulseaudio
pulseaudio-alsa
google-chrome
systemd-timesyncd
noto-fonts
noto-fonts-cjk'''


def setup():
    run_script("change-power-settings.sh")
    # Intel vtune
    run_command("echo kernel.yama.ptrace_scope=0 | sudo tee /etc/sysctl.d/10-ptrace.conf > /dev/null")
