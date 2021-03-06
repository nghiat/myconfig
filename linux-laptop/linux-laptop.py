from scripts.subprocess_wrapper import run_command, run_script

links = {
    "/etc/X11/xorg.conf.d/30-touchpad.conf": "30-touchpad.conf",
    "/etc/acpi/events/lid": "lid",
    "/etc/acpi/actions/lid.sh": "lid.sh",
}

note = """acpid, tlp
nvidia-prime
"""


def setup():
    run_script("laptop.sh")
    run_command("echo blacklist pcspkr | sudo tee /etc/modprobe.d/nobeep.conf > /dev/null")
