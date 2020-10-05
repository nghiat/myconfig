from scripts.file import copy_if_not_exist
from scripts.subprocess_wrapper import run_command

links = {
    "~/.bash_profile": ".bash_profile",
    "~/.bashrc": ".bashrc",
    "~/.gdbinit": ".gdbinit",
    "~/.inputrc": ".inputrc",
    "~/.tmux.conf": ".tmux.conf",
}

note = '''
tmux
tmux <prefix>-I
gem install tmuxinator'''


def setup():
    run_command("git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm")
    copy_if_not_exist(".tmux_local.conf", "~/.tmux_local.conf")
