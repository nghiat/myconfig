import os
from shutil import copy2


def copy_if_not_exist(src, dest):
    full_dest = os.path.expanduser(dest)
    if not os.path.exists(full_dest):
        copy2(src, full_dest)
        print("Copy from {} to {}".format(src, full_dest))
    else:
        print("Can't copy from {} to {}, dest exists".format(src, full_dest))
