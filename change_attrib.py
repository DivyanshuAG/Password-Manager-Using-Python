import sys
import subprocess
import os


def change_file_attribute(filename):
    if sys.platform.startswith("win"):
        os.system("attrib +s +i +h {}".format(filename))


def read_only(filename):
    if sys.platform.startswith("win"):
        subprocess.check_call(["attrib", "+r", filename])
