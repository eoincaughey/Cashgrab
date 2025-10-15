
from game_state import game_state
import blackjack
import roulette
import ebanking
import phishing
import webhack
import vpn
import time
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

def mainMenu():
    while True:
        clear_screen()
        print("=== Desktop ===")
        print("1. Mail Client")
        print("2. Online Casino")
        print("3. eBanking Portal")
        print("4. SSHush Web Client")
        print("5. VästVPN Client")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            phishing.menu()
        elif choice == "2":
            casinoMenu()
        elif choice == "3":
            ebanking.menu()
        elif choice == "4":
            webhack.menu()
        elif choice == "5":
            vpn.menu()
        elif choice == "6":
            print("Shutting down...")
            time.sleep(2)
            sys.exit()
            break
        else:
            print("Directory does not exist.")

def casinoMenu():
    clear_screen()
    print("\n--- Online Casino ---")
    print("1. Play Roulette")
    print("2. Play Blackjack")
    print("3. Play Slots (Coming Soon)")
    print("4. Back")

    choice = input("Choose an option: ")

    if choice == "1":
        spinning_loading(2, "Loading Roulette")
        roulette.start(game_state)
    elif choice == "2":
        spinning_loading(2, "Loading Blackjack")
        blackjack.start(game_state)
    elif choice == "3":
        print("Coming soon...")
        time.sleep(1)
        casinoMenu()

    elif choice == "4":
        return
    else:
        print("Directory does not exist.")

mainMenu()

