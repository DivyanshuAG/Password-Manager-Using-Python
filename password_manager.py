from menu import menu, store, find, find_email, aesthetics
from encryption import generate_hash, check_hash
from colorama import Style
import sys

aesthetics()
generate_hash()
if not check_hash():
    print(Style.RESET_ALL+"Wrong Password")
    sys.exit()
while True:
    choice = menu()
    if choice == "1":
        store()
    elif choice == "2":
        find()
    elif choice == "3":
        find_email()
    elif choice.lower() == "q":
        print(Style.RESET_ALL)
        sys.exit("Exiting.....")
    else:
        print("-" * 40)
        print("Please enter a valid option")
        print("-" * 40)
