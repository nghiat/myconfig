import os
from scripts.file import copy_if_not_exist

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
    copy_if_not_exist("local.vimrc.template", "~/local.vimrc")
