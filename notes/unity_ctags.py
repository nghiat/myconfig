from pathlib import Path

import concurrent.futures
import glob
import os
import shutil
import subprocess
import sys
import threading


print_lock = threading.Lock()


def decompile(cmd):
    with print_lock:
        print(f'Running: "{cmd}"')
    p = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    with print_lock:
        print(f'"{cmd}" output: ' + p.stdout)


def main():
    if shutil.which("ilspycmd") == None:
        print("Missing ilspycmd")
        if shutil.which("dotnet") == None:
            print("Missing dotnet to install ilspycmd")
            return
        print("Installing ilspycmd")
        p = subprocess.run("dotnet tool install ilspycmd -g", shell=True, capture_output=True, text=True)
        if p.return_code != 0:
            print("Error installing ilspycmd")
            return
    in_dir = sys.argv[1]
    out_dir = sys.argv[2]
    dll_files = glob.glob(os.path.join(in_dir, "*.dll"))
    executor = concurrent.futures.ProcessPoolExecutor(max_workers=4)
    futures = []
    for dll in dll_files:
        output_subdir = Path(dll).stem
        output_fulldir = os.path.join(out_dir, output_subdir)
        cmd = f"ilspycmd -o {output_fulldir} -p {dll}"
        futures.append(executor.submit(decompile, cmd))
    concurrent.futures.as_completed(futures)


if __name__ ==  "__main__":
    main()
