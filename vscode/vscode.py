import os
import platform
from scripts.subprocess_wrapper import run_command

note = """code.cmd on Windows"""

colors_templates = {
    "./ez-theme/themes/ez-theme.json.template": "./ez-theme/themes/ez-theme.json",
    "./ez-theme/themes/ez-dark-theme.json.template": "./ez-theme/themes/ez-dark-theme.json",
}

links = {
    "~/.vscode/extensions/ez-theme": "ez-theme",
}

extension_ids = [
    "christian-kohler.path-intellisense",
    "donjayamanne.githistory",
    "HookyQR.beautify",
    "ms-python.python",
    "ms-vscode.cpptools",
    "npclaudiu.vscode-gn",
    "vscode-icons-team.vscode-icons",
    "vscodevim.vim",
    "xaver.clang-format",
    "muuvmuuv.vscode-sundial",
    "ms-vscode.hexeditor",
]

files = ["keybindings.json", "settings.json"]


def create_links(prefix_path):
    results = {}
    for filename in files:
        links[os.path.join(prefix_path, filename)] = filename

code_cmd = "code"

if platform.system() == "Windows":
    create_links("~/AppData/Roaming/Code/User")
    code_cmd = "code.cmd"
elif platform.system() == "Linux":
    create_links("~/.config/Code/User")
elif platform.system() == "Darwin":
    create_links("~/Library/Application Support/Code/User")


def setup():
    for id in extension_ids:
        run_command(code_cmd + " --install-extension " + id)


def clean():
    for id in extension_ids:
        run_command(code_cmd + " --uninstall-extension " + id)
