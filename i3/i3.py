from scripts.subprocess_wrapper import run_command
import getpass

links = {
    "~/.xinitrc": ".xinitrc",
    "~/.xserverrc": ".xserverrc",
    "~/.config/dunst/dunstrc": "dunstrc",
    "~/.config/i3/config": "i3",
    "~/.config/i3/i3status.conf": "i3status.conf",
    "~/gnome_keyring.sh": "gnome_keyring.sh",
    "/etc/systemd/system/i3lock@.service": "i3lock@.service",
}

def setup():
    run_command("sudo systemctl enable i3lock@{}.service".format(getpass.getuser()))
    run_command("systemctl --user enable redshift")

note = """
i3
network-manager-applet
compton
gnome-keyring
dunst
rofi
xorg-xset
xautolock
ttf-dejavu
volumeicon
xf86-input-synaptics
acpid
light (sudo usermod -a -G video nghia)
arandr
xinit (or xorg-xinit)
udisks2
gvfs
gvfs-mtp
gvfs-smb
lxsession
"""
