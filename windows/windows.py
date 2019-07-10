import os
from scripts.subprocess_wrapper import run_command

note = """clink
autohotkey
vcxsrv
QTTabBar
Preview pane
Folder Options: Quick access
Edit and run: edit_with_vim.reg

Visual Studio:
  - Color Theme Editor
  - nghiatt.vssettings
"""

colors_templates = {
    ".minttyrc.template": "~/.minttyrc",
}


def setup():
    current_folder = os.path.dirname(os.path.realpath(__file__))
    run_command("schtasks /CREATE /SC ONLOGON /TN Launch-Apps /TR {} /RL LIMITED".format(os.path.join(current_folder, "launch_apps.ahk")))
    run_command("schtasks /CREATE /SC ONLOGON /TN xlaunch /TR {} /RL LIMITED".format(os.path.join(current_folder, "config.xlaunch")))
    run_command('copy %HOMEPATH%\\myconfig\\windows\\urxvt.lnk "%AppData%\\Microsoft\\Windows\\Start Menu\\Programs"')
    run_command('reg IMPORT preview.reg')
    run_command('taskkill /f /im explorer.exe')
    run_command('start explorer.exe')


