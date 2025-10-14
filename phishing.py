from game_state import game_state
import random
import sys
import time
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

formattedDT = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())

def locate_emails():

    addresses_found = random.randint(5, 1000)  # Random number of email addresses found

    clear_screen()
    spinning_loading(6, "Locating email addresses for sale")
    print(f"Found {addresses_found} email addresses for sale.")
    print(f"Current balance: £{game_state['balance']}")

    while True:
        exportBool = input(f"Purchase address list for £{addresses_found * 3}? (Y/N): ").lower()

        if exportBool == 'y':
            spinning_loading(5, "Transaction in progress")
            game_state['balance'] -= addresses_found * 3

            spinning_loading(3, "Exporting email addresses to .csv file")
            print(f"Transcation success. Saved email addresses to 'addressList_{formattedDT}.csv'.")
            time.sleep(2)
            print(f"New balance: £{game_state['balance']}")

            print(f"Press enter to return to mail client.")
            wait_for_keypress()

            hasAddresses = True
            game_state['noOfEmailAddresses'] += addresses_found

            break  # exit loop after valid input
        elif exportBool == 'n':
            print("Located addresses have been wiped.")
            break  # exit loop after valid input
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def send_mass_email():
    if game_state['noOfEmailAddresses'] <= 0:
        clear_screen()
        print("You have no email addresses to send to. Locate addresses for sale first.")
        print("Press enter to return.")
        wait_for_keypress()
        return

    clear_screen()
    print(f"You have {game_state['noOfEmailAddresses']} email addresses in your contacts list.")
    while True:
        try:
            num_emails = int(input("Enter the number of addresses to phish (or '0' to cancel): "))
            if num_emails < 0:
                print("Number of emails cannot be negative. Try again.")
                continue
            if num_emails == 0:
                print("Email sending cancelled.")
                return
            if num_emails > game_state['noOfEmailAddresses']:
                print("You cannot send more emails than you have addresses for. Try again.")
                continue

            success_rate = random.uniform(0, 0.15)  # Random success rate between 0% and 15%
            successful_emails = int(num_emails * success_rate)
            earnings = successful_emails * 493  # Assume each successful phishing email earns £493

            spinning_loading(5, "Sending emails")
            print(f"Sent {num_emails} emails.")
            print("Waiting for responses. This may take a while...")
            time.sleep(3)
            spinning_loading(5, "Processing responses")

            spinning_loading(4, "Responses receieved, calculating success rate")
            print(f"Calculated success rate at {success_rate:.2%}.")
            spinning_loading(9, f"Success rate {success_rate:.2%}, calculating earnings")
            print(f"Successful attempts: {successful_emails}. Earnings: £{earnings}.")

            game_state['balance'] += earnings
            game_state['reputation'] += successful_emails // 10  # Increase reputation for every 10 successful emails
            game_state['noOfEmailAddresses'] -= num_emails  # Decrease available email addresses

            print(f"Remaining email addresses: {game_state['noOfEmailAddresses']}.")
            print(f"New balance: £{game_state['balance']}. Reputation: {game_state['reputation']}.")
            
            print("Press enter to return to client.")
            wait_for_keypress()
            break  # exit loop after successful sending
        except ValueError:
            print("Invalid input. Please enter a valid number.")