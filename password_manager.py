from menu import menu, store, find
import sys

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
