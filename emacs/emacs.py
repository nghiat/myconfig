from scripts.file import copy_if_not_exist
import os

colors_templates = {
    "./.emacs.d/ez-theme.el.template": "./.emacs.d/ez-theme.el",
    "./.emacs.d/ez-dark-theme.el.template": "./.emacs.d/ez-dark-theme.el"
}

links = {
    "~/.emacs.d": ".emacs.d",
}
if os.name == "nt":
    links["%APPDATA%/.emacs.d"] = ".emacs.d"

note = """pip install yapf flake8
hunspell en-us de-de-frami fr
Not sure about .emacs.d on Windows, it can either be ~ or APPDATA"""


def setup():
    copy_if_not_exist(".emacs.d/init.d/init-local.el.template", ".emacs.d/init.d/init-local.el")
