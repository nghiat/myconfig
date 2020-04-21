from scripts.colors import generate_iterm2_presets

links = {
    "~/Library/ApplicationSupport/iTerm2/Scripts/AutoLaunch/switch_color.py": "switch_color.py",
}

note = '''sudo pmset -a disablesleep 0'''


def setup():
    generate_iterm2_presets()
