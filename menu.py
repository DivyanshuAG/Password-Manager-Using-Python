from encryption import generateKey, encryptPass, decryptPass
from database_manager import create_table, store_password, find_password
from master import generate_hash, check_hash
import subprocess


def menu():
    # Creating required files
    generate_hash()
    if not check_hash():
        sys.exit("Wrong Password")
    generateKey()
    create_table()

    # Hiding unnecessary files
    hide_file("master.key")
    hide_file("secret.key")
    hide_file("Manager.db")

    # Aesthetics
    print("_" * 40)
    print("_" * 18 + "Password Manager" + "_" * 18)
    print("_" * 40)
    print("1. Create New Password")
    print("2. Find a Password for a Service")
    print("Q. Quit")
    print("_" * 40)
    return input(": ")


def store():
    email = input("Email: ")
    username = input("Username: ")
    password = input("Password: ")
    url = input("URL: ")
    service = input("Service: ")
    if len(username) < 1:
        username = ""
    encryptedPass = encryptPass(password)
    store_password(encryptedPass, email, username, url, service)
    print("_" * 40)
    print(
        "Password Encrypted and Stored",
    )
    print("_" * 40)


def find():
    service = input("Service: ")
    encryptedPass = find_password(service)
    if encryptedPass == "":
        print("No Password Found")
    else:
        passw = decryptPass(encryptedPass)
        subprocess.run("clip", universal_newlines=True, input=passw)
        print("_" * 40)
        print(
            "Password has been copied to clipboard",
        )
        print("_" * 40)

def hide_file(filename):
    subprocess.check_call(["attrib","+H",filename])