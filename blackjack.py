from game_state import game_state 
import random
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

def start(game_state):
    if game_state['balance'] <= 0:
        print("You have no money to play blackjack.")
        return game_state['balance']

    updated_balance = play(game_state['balance'])

    if updated_balance is None:
        updated_balance = game_state['balance']

    game_state['balance'] = updated_balance
    return game_state['balance']

def startnewRound():
    print("Press enter to continue.")
    wait_for_keypress()
    clear_screen()

def spinning_loading(duration=3, message=""):
    print(message, end="")
    for _ in range(duration):
        for dot in ". .. ...".split():
            print(f"\r{message}{dot}  ", end="")
            sys.stdout.flush()
            time.sleep(0.5)
    print("\r" + " " * 100, end="\r")

bBalance = 1000

def play(balance):

    global bBalance;
    clear_screen()
    print("Welcome to Blackjack!")
    print(f"Your current balance is: £{balance}")
    bBalance = int(input("Chip quantity to purchase (or '0' to cancel): "))

    if bBalance > balance: # check if user has enough balance to buy in
        print("You do not have enough balance to buy those chips.")
        return balance
    
    elif bBalance == 0:
        print("Transaction cancelled. Returning to menu.")
        time.sleep(1)
        return balance
    
    else: # if they do, let them buy in
        game_state["balance"] -= bBalance # deduct buy in from main balance

        print(f"You bought {bBalance} chips for £{bBalance}. Your balance is now £{game_state["balance"]}.")
        spinning_loading(1, "Starting game")

    while bBalance > 0:
        while True:
            clear_screen()
            # Get the player's bet
            while True:
                try:
                    bet = int((input("Enter your bet amount. Enter '0' to exit: ")))

                    if bet == 0:
                        game_state["balance"] += bBalance # add remaining chips to main balance
                        print(f"You cashed out your chips for £{bBalance}. Returning to desktop with £{game_state['balance']}.")
                        print("Press enter to return to menu.")
                        wait_for_keypress()
                        return game_state["balance"]
                    
                    elif bet <= bBalance:
                        break

                    else:
                        print(f"Invalid bet amount. Please enter a value between 1 and {bBalance}.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            
            # Deal initial cards
            player_cards = [random.randint(1, 11), random.randint(1, 11)]
            dealer_cards = [random.randint(1, 11), random.randint(1, 11)]
            
            spinning_loading(2, "Dealing cards")
            print(f"Your cards: {player_cards} (Total: {sum(player_cards)})")
            print(f"Dealer's visible card: {dealer_cards[0]}")
            
            # Player's turn
            while True:

                if sum(player_cards) > 21:
                        bBalance -= bet
                        time.sleep(1)
                        print(f"You bust! Your balance is now {bBalance} chips.")
                        startnewRound()
                        break

                if sum(player_cards) == 21:
                        bBalance += int(1.5 * bet)
                        time.sleep(1)
                        print(f"Blackjack! You win! Your balance is now {bBalance} chips.")
                        startnewRound()
                        break

                while sum(player_cards) < 21:

                    choice = input("Do you want to (h)it or (s)tand? ").lower()
            
                    if choice == 'h':
                        new_card = random.randint(1, 11)
                        player_cards.append(new_card)
                        print(f"You drew a {new_card}. Your cards: {player_cards} (Total: {sum(player_cards)})")
                
                    elif choice == 's':
                        print(f"You stand with {player_cards} (Total: {sum(player_cards)})")
                        spinning_loading(1, "Dealer's turn")
                        break

                    else:
                        print("Invalid choice. Please enter 'h' or 's'.")
                        break

                    if sum(player_cards) > 21:
                        bBalance -= bet
                        time.sleep(1)
                        print(f"You bust! Your balance is now {bBalance} chips.")
                        startnewRound()
                        break

                    if sum(player_cards) == 21:
                        bBalance += int(1.5 * bet)
                        time.sleep(1)
                        print(f"Blackjack! You win! Your balance is now {bBalance} chips.")
                        startnewRound()
                        break

                if sum(player_cards) < 21:
                    print(f"Dealer's cards: {dealer_cards} (Total: {sum(dealer_cards)})")
                
                while sum(player_cards) < 21 and sum(dealer_cards) < 17:
                    new_card = random.randint(1, 11)
                    dealer_cards.append(new_card)
                    print(f"Dealer draws a {new_card}. Dealer's cards: {dealer_cards} (Total: {sum(dealer_cards)})")
                    time.sleep(1)
                break
            
            if  sum (player_cards) < 21 and sum(dealer_cards) == sum(player_cards):
                time.sleep(1)
                print(f"Push! Your bet is returned. Your balance is now {bBalance} chips.")
                startnewRound()
                break

            if  sum (player_cards) < 21 and sum(dealer_cards) > 21:
                bBalance += bet
                time.sleep(1)
                print(f"Dealer busts! You win! Your balance is now {bBalance} chips.")
                startnewRound()
                break

            if  sum (player_cards) < 21 and sum(dealer_cards) > sum(player_cards):
                bBalance -= bet
                time.sleep(1)
                print(f"Dealer wins! Your balance is now {bBalance} chips.")
                startnewRound()
                break

            if  sum (player_cards) < 21 and sum(dealer_cards) < sum(player_cards):
                bBalance += bet
                time.sleep(1)
                print(f"You win! Your balance is now {bBalance} chips.")
                startnewRound()
                break
            
            break # break out of the while True loop to start a new round
    
    print("Leaving the blackjack table.") #bankrupt sounds a bit dramatic ngl but its shweet       