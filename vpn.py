from game_state import game_state
import time
import main
import sys
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

def spinning_loading(duration=3, message=""):
    print(message, end="")
    for _ in range(duration):
        for dot in ". .. ...".split():
            print(f"\r{message}{dot}  ", end="")
            sys.stdout.flush()
            time.sleep(0.5)
    print("\r" + " " * 100, end="\r")


servers = [
    {"id": "EU01", "city": "Stockholm", "country": "Sweden"},
    {"id": "EU02", "city": "Berlin", "country": "Germany"},
    {"id": "EU03", "city": "Paris", "country": "France"},
    {"id": "EU04", "city": "London", "country": "UK"},
    {"id": "EU05", "city": "Amsterdam", "country": "Netherlands"},
    {"id": "EU06", "city": "Madrid", "country": "Spain"},
    {"id": "EU07", "city": "Rome", "country": "Italy"},
    {"id": "EU08", "city": "Vienna", "country": "Austria"},
    {"id": "EU09", "city": "Warsaw", "country": "Poland"},
    {"id": "NA01", "city": "New York", "country": "USA"},
    {"id": "NA02", "city": "Los Angeles", "country": "USA"},
    {"id": "SA01", "city": "São Paulo", "country": "Brazil"},
    {"id": "AS01", "city": "Tokyo", "country": "Japan"},
    {"id": "AS02", "city": "Seoul", "country": "South Korea"},
    {"id": "AS03", "city": "Mumbai", "country": "India"}
    ]

connectionStatus = "DISCONNECTED"
connectedOrDisconnected = "Connect to"

def connectToggle():
    global connectionStatus, connectedOrDisconnected

    if connectionStatus == "DISCONNECTED":
        connectionStatus = "CONNECTED"
    else:
        connectionStatus = "DISCONNECTED"

    if connectionStatus == "Connected":
        connectedOrDisconnected = "Disconnect from"
    else:
        connectedOrDisconnected = "Connect to"

def menu():
    clear_screen()
    print("\n--- VästVPN Client ---")
    print(f"{connectionStatus}")
    print("1. Server Location List")
    print(f"2. {connectedOrDisconnected} server")
    print("3. Manage your subscription")
    print("4. Back")

    choice = input("Choose an option: ")

    if choice == "1":

        menu()

    elif choice == "2":
        connectToggle()
        menu()

    elif choice == "3":
        if game_state['noOfEmailAddresses'] > 0:
            clear_screen()
            print(f"You have {game_state['noOfEmailAddresses']} email addresses in your contacts list.")
            print("Press enter to return.")
            wait_for_keypress()
            menu()
        else:
            clear_screen()
            print("Your contacts list is empty. Press enter to return.")
            wait_for_keypress()
            menu()

    elif choice == "4":
        return

    else:
        print("Directory does not exist.")