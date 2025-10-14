from game_state import game_state
import blackjack
import roulette
import ebanking
import phishing
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

def startRoulette(game_state):

    if game_state['balance'] <= 0:
        print("You have no money to play roulette.")
        return game_state['balance']

    updated_balance = roulette.play(game_state['balance'])

    if updated_balance is None:
        updated_balance = game_state['balance']

    game_state['balance'] = updated_balance
    return game_state['balance']

def startBlackjack(game_state):
    if game_state['balance'] <= 0:
        print("You have no money to play blackjack.")
        return game_state['balance']

    updated_balance = blackjack.play(game_state['balance'])

    if updated_balance is None:
        updated_balance = game_state['balance']

    game_state['balance'] = updated_balance
    return game_state['balance']

#Main menu function
def mainMenu():
    while True:
        clear_screen()
        print("\n=== Desktop ===")
        print("1. Mail Client")
        print("2. Online Casino")
        print("3. eBanking Portal")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            mailclientMenu()
        elif choice == "2":
            casinoMenu()
        elif choice == "3":
            ebanking.menu()
        elif choice == "4":
            print("Shutting down...")
            time.sleep(2)
            sys.exit()
            break
        else:
            print("Directory does not exist.")

#Mail client - locates email addresses for sale, lets you send phishing emails to them to earn money
def mailclientMenu():
    clear_screen()
    print("\n--- 'Gone Phishing' - Mail Client ---")
    print("1. Locate addresses for sale")
    print("2. Send mass email from .csv file")
    print("3. Check contacts list")
    print("4. Back")

    choice = input("Choose an option: ")

    if choice == "1":
        phishing.locate_emails()
        mailclientMenu()

    elif choice == "2":
        phishing.send_mass_email()
        mailclientMenu()

    elif choice == "3":
        if game_state['noOfEmailAddresses'] > 0:
            clear_screen()
            print(f"You have {game_state['noOfEmailAddresses']} email addresses in your contacts list.")
            print("Press enter to return.")
            wait_for_keypress()
            mailclientMenu()
        else:
            clear_screen()
            print("Your contacts list is empty. Press enter to return.")
            wait_for_keypress()
            mailclientMenu()

    elif choice == "4":
        return

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
        startRoulette(game_state)
    elif choice == "2":
        spinning_loading(2, "Loading Blackjack")
        startBlackjack(game_state)
    elif choice == "3":
        print("Coming soon...")
        time.sleep(1)
        casinoMenu()

    elif choice == "4":
        return
    else:
        print("Directory does not exist.")

mainMenu()

