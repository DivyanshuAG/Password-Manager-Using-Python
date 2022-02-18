from encryption import generateKey, encryptPass, decryptPass
from database_manager import (
    create_table,
    store_password,
    find_password,
    find_using_email,
)
import subprocess
from colorama import Fore, Style
from change_attrib import change_file_attribute


def menu():
    # Creating required files
    generateKey()
    create_table()

    # Change file attributes
    change_file_attribute("Manager.db")
    change_file_attribute(".env")

    # Aesthetics
    print("-" * 40)
    print("-" * 40)
    print("-" * 40)
    print("1. Create New Password")
    print("2. Find a Password for a Service")
    print("3. Find All Passwords for an Email")
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
    print("Encrypted Password: " + encryptedPass.decode('utf-8'))
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


def find_email():
    data = ["Encrypted Password", "Email", "Username", "Url", "Service"]
    email = input("Email: ")
    results = find_using_email(email)
    print("-" * 40)
    if results:
        for row in results:
            for i in range(0, len(row)):
                print("{}: {}".format(data[i], row[i]))
            print("-" * 40)
    else:
        print("No Passwords Found")


def aesthetics():
    passMan = """
 ____               __  __
|  _ \ __ _ ___ ___|  \/  | __ _ _ __
| |_) / _` / __/ __| |\/| |/ _` | '_ \\
|  __/ (_| \__ \__ \ |  | | (_| | | | |
|_|   \__,_|___/___/_|  |_|\__,_|_| |_|

"""
    print(Fore.CYAN + "#" * 40)
    print(passMan)
    print("#" * 40)
    print()
    print(
        "PassMan, a FOSS Passwords Manager, is a portable software that allows you to effectively encrypt and store your passwords to a database, and retrieve your passwords from said database, with a simple menu based interface\n"
    )
    print("#" * 40)
    print()