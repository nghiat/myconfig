import os
from scripts.subprocess_wrapper import run_command

note = r"""
Envvars: C:\Program Files\Google\Chrome\Application;C:\Program Files\Everything;D:\apps\vim;
clink (github)
vcxsrv
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

Start -> Type something -> Indexing option
"""

colors_templates = {
    ".minttyrc.template": "~/.minttyrc",
}

links = {
    "~/.vsvimrc": ".vsvimrc",
}

def setup():
    current_folder = os.path.dirname(os.path.realpath(__file__))
    run_command('schtasks /CREATE /TN Launch-Apps /xml "{}"'.format(os.path.join(current_folder, "Launch-Apps.xml")))
    run_command('schtasks /CREATE /TN xlaunch /xml "{}"'.format(os.path.join(current_folder, "xlaunch.xml")))
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
    # choco
    run_command('powershell -ExecutionPolicy Bypass -File {}'.format(os.path.join(current_folder, "chocolatey.ps1")))
    # Windows 10 old context
    run_command('reg add "HKEY_CURRENT_USER\Software\Classes\CLSID\{86ca1aa0-34aa-4e8b-a509-50c905bae2a2}\InprocServer32" /t REG_SZ /f')
