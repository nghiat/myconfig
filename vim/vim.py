import os
from os import path
from shutil import copy2

note = """fzf rg universal-ctags"""
colors_templates = {
        "./vimfiles/colors/ez.vim.template": "./vimfiles/colors/ez.vim",
}

links = {
    "~/.vimrc": "vimrc",
}

if os.name == "nt":
    links["~/vimfiles"] = "vimfiles"
else:
    links["~/.vim"] = "vimfiles"


def setup():
    copy2("local.vimrc", os.path.expanduser("~/local.vimrc"))
