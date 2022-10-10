import os
import sys
from scripts.file import copy_if_not_exist
from scripts.subprocess_wrapper import run_script

colors_templates = {
        "./vimfiles/colors/ez.vim.template": "./vimfiles/colors/ez.vim",
}

links = {
    "~/.vimrc": "vimrc",
}

if os.name == "nt":
    note = """fzf rg universal-ctags"""
    links["~/vimfiles"] = "vimfiles"
else:
    links["~/.vim"] = "vimfiles"


def setup():
    if not os.path.exists("vimfiles/swap"):
        os.mkdir("vimfiles/swap")
    copy_if_not_exist("local.vimrc.template", "~/local.vimrc")
    if sys.platform.startswith("linux"):
        run_script("install.sh")
