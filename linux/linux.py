from scripts.subprocess_wrapper import run_script, run_command

colors_templates = {
    ".ez_colors.template": "~/.ez_colors",
}

links = {
    "~/.config/mpv/mpv.conf": "mpv.conf",
    "~/.config/pulse/default.pa": "default.pa",
    "~/.Xdefaults": ".Xdefaults",
    "~/.xprofile": ".xprofile",
    "~/.xbindkeysrc": ".xbindkeysrc",
}
note = '''
hibernate:
- /etc/default/grub: GRUB_CMDLINE_LINUX_DEFAULT="resume=UUID={value in fstab}" -> grub-mkconfig
- /etc/mkinitcpio.conf: add resume hook after udev -> mkinitcpio -p linux
GRUB default:
  GRUB_DEFAULT=saved
  GRUB_SAVEDEFAULT=true

xsel
urxvt (or rxvt-unicode)
redshift
python-xdg
xbindkeys
mpv
bash-completion
ibus: Ubuntu im-config, Untick Use system keyboard layout
pulseaudio
pulseaudio-alsa
pavucontrol
google-chrome
noto-fonts
noto-fonts-cjk'''


def setup():
    run_script("change-power-settings.sh")
    # Intel vtune
    run_command("echo kernel.yama.ptrace_scope=0 | sudo tee /etc/sysctl.d/10-ptrace.conf > /dev/null")
    run_command("cp .Xdefaults.dpi ~")
    run_command("sudo systemctl enable systemd-timesyncd")
