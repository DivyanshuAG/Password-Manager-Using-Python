from menu import menu, store, find
from encryption import generate_hash, check_hash
import sys

generate_hash()

if not check_hash():
    sys.exit("Wrong Password")
while True:
    choice = menu()
    if choice == "1":
        store()
    elif choice == "2":
        find()
    elif choice.lower() == "q":
        sys.exit("Exiting.....")
        print("_" * 40)
    else:
        print("_" * 40)
        print("Please enter a valid option")
        print("_" * 40)
