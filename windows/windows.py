import os
from scripts.subprocess_wrapper import run_command
from scripts.colors import generate_iterm2_presets

note = """clink
autohotkey
vcxsrv
chocolatey procexp
https://tuxproject.de/projects/vim/

Run the following command (cause running ColorTool.exe from here raises error):
    ColorTool.exe -b -q ez.itermcolors && del *.itermcolors

Ultimate Windows Tweaker -> Customization -> This PC
Task Scheduler:
- Disable "Conditions->Start the task only if the computer is on AC power"
- Disable "Settings->Stop the task if it runs longer than"

Visual Studio:
  - Color Theme Editor
  - nghiatt.vssettings

FreeCommanderXE: Settings -> Shell Menu

HiDPI:
- Right click -> Properties -> Change high DPI settings -> Override high ...
  + FreeCommander.exe

Windows 10: Settings -> Accounts -> Sign-in options -> Disble "Use my sign-in info ..."
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
    # Windows startup delay
    run_command('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Serialize" /v StartupDelayInMSec /d 0 /t REG_DWORD /f')
    run_command('reg add "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Search" /v BingSearchEnabled /d 0 /t REG_DWORD /f')
    run_command('reg add "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Search" /v CortanaConsent /d 0 /t REG_DWORD /f')
    # Colortool
    generate_iterm2_presets()
