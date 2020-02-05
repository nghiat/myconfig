import os
from scripts.subprocess_wrapper import run_command

note = """clink
autohotkey
vcxsrv
https://github.com/vim/vim-win32-installer/releases

Ultimate Windows Tweaker -> Customization -> This PC
Task Scheduler:
- Disable "Conditions->Start the task only if the computer is on AC power"
- Disable "Settings->Stop the task if it runs longer than"

Visual Studio:
  - Color Theme Editor
  - nghiatt.vssettings

FreeCommanderXE: Settings -> Shell Menu
"""

colors_templates = {
    ".minttyrc.template": "~/.minttyrc",
}

links = {
    "~/.vimrc": "vimrc",
    "~/AppData/Local/FreeCommanderXE/Settings/FreeCommander.ini": "FreeCommander.ini",
}

def setup():
    current_folder = os.path.dirname(os.path.realpath(__file__))
    run_command("schtasks /CREATE /SC ONLOGON /TN Launch-Apps /TR {} /RL LIMITED".format(os.path.join(current_folder, "launch_apps.ahk")))
    run_command("schtasks /CREATE /SC ONLOGON /TN xlaunch /TR {} /RL LIMITED".format(os.path.join(current_folder, "config.xlaunch")))
    run_command('copy %HOMEPATH%\\myconfig\\windows\\urxvt.lnk "%AppData%\\Microsoft\\Windows\\Start Menu\\Programs"')
    run_command('reg add "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\TimeZoneInformation" /v RealTimeIsUniversal /d 1 /t REG_QWORD /f')
