<<<<<<< HEAD
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
    bankID = "0001"
    pinCode = "1111"

    clear_screen()
    print("=== safeMoney eBanking ===")

    for i in range(3):
        bankID = input("eBanking ID: ")
        pinCode = input("PIN: ")

        if bankID == bankID and pinCode == pinCode:
            print(f"\nLogin successful! Your current balance is £{game_state["balance"]}\n")
            print("Press enter to log out.")
            wait_for_keypress()
            return
        else:
            print("Invalid credentials. Try again.\n")

    print("Too many failed attempts. Terminating session.")
    input("Press Enter to continue...")
    wait_for_keypress()
=======
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
    bankID = "0001"
    pinCode = "1111"

    clear_screen()
    print("=== safeMoney eBanking ===")

    for i in range(3):
        bankID = input("eBanking ID: ")
        pinCode = input("PIN: ")

        if bankID == bankID and pinCode == pinCode:
            print(f"\nLogin successful! Your current balance is £{game_state["balance"]}\n")
            print("Press enter to log out.")
            wait_for_keypress()
            return
        else:
            print("Invalid credentials. Try again.\n")

    print("Too many failed attempts. Terminating session.")
    input("Press Enter to continue...")
    wait_for_keypress()
>>>>>>> c3c416a88a1d162004d8e05cd506037914d6e02c
    return