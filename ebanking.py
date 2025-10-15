from game_state import game_state
import os

def wait_for_keypress():
    input("")

def clear_screen():
    # Windows
    if os.name == 'nt':
        os.system('cls')
    # Mac/Linux
    else:
        os.system('clear')

def menu():
    while True:
        clear_screen()
        print("=== safeMoney eBanking ===")
        print("1. Login with eBanking ID and PIN")
        print("2. Exit safeMoney eBanking")
        
        choice = input("Choose an option: ")

        if choice == "1":
            login()
        elif choice == "2":
            break
        else:
            print ("Please choose option 1 or 2.")
            continue

def login():
    while True:
        bankID = "0001"
        pinCode = "1111"

        clear_screen()
        print("=== safeMoney eBanking ===")

        for i in range(3):
            
            ID = input("eBanking ID: ")
            PIN = input("PIN: ")

            if bankID == ID and pinCode == PIN:
                print(f"\nLogin successful! Your current balance is £{game_state["balance"]}\n")
                print("Press enter to log out.")
                wait_for_keypress()
                return
            else:
                print("Invalid credentials. Press enter to retry.\n")
                wait_for_keypress()
                clear_screen()

        print("Too many failed attempts. Terminating session.")
        input("Press Enter to continue...")
        wait_for_keypress()
