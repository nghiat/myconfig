from scripts.subprocess_wrapper import run_script, run_command

links = {
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
    run_command("cp ~/myconfig/linux-general/.tmux_local.conf ~")
