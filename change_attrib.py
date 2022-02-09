import sys
import os
import win32api
import win32con


def change_file_attribute(filename):
    if sys.platform.startswith("win"):
        if not win32api.GetFileAttributes(filename) & win32con.FILE_ATTRIBUTE_SYSTEM:
            os.system("attrib +s +i +h {}".format(filename))
