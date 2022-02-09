import hashlib
from change_attrib import change_file_attribute, read_only
import sys


def DoesHashExist():
    try:
        if open("master.key", "rb").read() != "":
            return True
    except:
        return False


def generate_hash():
    if not DoesHashExist():
        masterPass = input("Set Master Password: ")
        print("Please do not forget this key, as your passwords cannot be recovered")
        sha256_MasterPass = hashlib.sha256(masterPass.encode()).hexdigest()
        sha256_MasterPass = bytes(sha256_MasterPass, "utf-8")
        with open("master.key", "wb") as file:
            file.write(sha256_MasterPass)
        read_only("master.key")
        change_file_attribute("master.key")


def check_hash():
    hash = open("master.key", "rb").read()
    MasterPasswordInputNow = input("Enter the Master Password: ")
    MasterPasswordInputNowHashed = bytes(
        hashlib.sha256(MasterPasswordInputNow.encode()).hexdigest(), "utf-8"
    )
    if MasterPasswordInputNowHashed == hash:
        return True
    else:
        return False
