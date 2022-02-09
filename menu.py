from encryption import generateKey, encryptPass, decryptPass
from database_manager import create_table, store_password, find_password
from change_attrib import change_file_attribute
import subprocess


def menu():
    # Creating required files
    generateKey()
    create_table()

    # Change file attributes
    change_file_attribute("Manager.db")
    change_file_attribute('.env')

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
