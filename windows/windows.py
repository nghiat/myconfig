import os
from scripts.subprocess_wrapper import run_command

note = """clink (github)
autohotkey
vcxsrv
chocolatey processhacker strawberryperl
Put perl bin dir before git/bin in PATH because fzf :Tags doesn't work well with perl from git
https://tuxproject.de/projects/vim/

Ultimate Windows Tweaker -> Customization -> This PC
Task Scheduler:
- Disable "Conditions->Start the task only if the computer is on AC power"
- Disable "Settings->Stop the task if it runs longer than"

Visual Studio:
  - Color Theme Editor
  - nghiatt.vssettings
  - Disable git, IntelliSense

FreeCommanderXE: Settings -> Shell Menu

HiDPI:
- Right click -> Properties -> Change high DPI settings -> Override high ...
  + FreeCommander.exe

Windows 10: Settings -> Accounts -> Sign-in options -> Disble "Use my sign-in info ..."
clink set clink.default_bindings bash
"""

colors_templates = {
    ".minttyrc.template": "~/.minttyrc",
}

links = {
    "~/.vsvimrc": ".vsvimrc",
}

def setup():
    current_folder = os.path.dirname(os.path.realpath(__file__))
    run_command('schtasks /CREATE /SC ONLOGON /TN Launch-Apps /TR "AutoHotKey.exe \'{}\'" /RL LIMITED'.format(os.path.join(current_folder, "launch_apps.ahk"))) # Exe path is case-sensitive
    run_command('schtasks /CREATE /SC ONLOGON /TN xlaunch /TR "xlaunch.exe -run \'{}\'" /RL LIMITED'.format(os.path.join(current_folder, "config.xlaunch"))) # Exe path is case-sensitive
    run_command('copy "%HOMEPATH%\\myconfig\\windows\\urxvt.lnk" "%AppData%\\Microsoft\\Windows\\Start Menu\\Programs"')
    run_command('reg add "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\TimeZoneInformation" /v RealTimeIsUniversal /d 1 /t REG_QWORD /f')
    # Windows startup delay
    run_command('reg add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Serialize" /v StartupDelayInMSec /d 0 /t REG_DWORD /f')
    run_command('reg add "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Search" /v BingSearchEnabled /d 0 /t REG_DWORD /f')
    run_command('reg add "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Search" /v CortanaConsent /d 0 /t REG_DWORD /f')
    # Free Commander
    run_command('mkdir "%HOMEPATH%\\AppData\\Local\\FreeCommanderXE\\Settings"')
    run_command('copy "%HOMEPATH%\\myconfig\\windows\\FreeCommander.ini" "%HOMEPATH%\\AppData\\Local\\FreeCommanderXE\\Settings"')
    run_command('copy "%HOMEPATH%\\myconfig\\windows\\FreeCommander.shc" "%HOMEPATH%\\AppData\\Local\\FreeCommanderXE\\Settings"')
