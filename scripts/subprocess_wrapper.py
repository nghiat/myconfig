import os
import subprocess


def run_command(args):
    shell_exec = os.getenv("SHELL")
    sp = subprocess.Popen(args,
                          shell=True,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT)
    print("Running: " + args)
    print(sp.communicate()[0].decode("utf-8", "ignore"))


def run_script(script_path):
    abs_path = os.path.abspath(script_path)
    run_command(abs_path)
