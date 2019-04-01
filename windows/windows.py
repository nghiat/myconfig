import os
from scripts.subprocess_wrapper import run_command

note = """clink
autohotkey
vs-ez
vcxsrv"""

colors_templates = {
    ".minttyrc.template": "~/.minttyrc",
}


def setup():
    current_folder = os.path.dirname(os.path.realpath(__file__))
    run_command("schtasks /CREATE /SC ONLOGON /TN Launch-Apps /TR {} /RL LIMITED".format(os.path.join(current_folder, "launch_apps.ahk")))
    run_command("schtasks /CREATE /SC ONLOGON /TN xlaunch /TR {} /RL LIMITED".format(os.path.join(current_folder, "config.xlaunch")))
    run_command('copy %HOMEPATH%\\myconfig\\windows\\urxvt.lnk "%AppData%\\Microsoft\\Windows\\Start Menu\\Programs"')
