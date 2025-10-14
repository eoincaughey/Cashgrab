
# Roulette mini-game

# left some comments to explain most parts of the code
# hopefully its not too cluttered and u can use some of the ideas to start making ur own other gamemode
# maybe more casino style games? you could try blackjack or slots or something idk whatever

from game_state import game_state
import random
import time
import sys
import os

def clear_screen():
    # Windows
    if os.name == 'nt':
        os.system('cls')
    # Mac/Linux
    else:
        os.system('clear')

def wait_for_keypress():
    input("")

def startnewRound():
    print("Press enter to continue.")
    wait_for_keypress()
    clear_screen()

def chooseValidColour(): # this function makes sure the user inputs a valid colour, otherwise it keeps asking them
    valid_choices = ["red", "black", "green"]
    while True:
        chosenColour = input("Choose a colour; red, black or green: ").lower()
        if chosenColour in valid_choices:
            return chosenColour
        print("Invalid input. Try again.")

def spinning_loading(duration=3, message=""):
    print(message, end="")
    for _ in range(duration):
        for dot in ". .. ...".split():
            print(f"\r{message}{dot}  ", end="")
            sys.stdout.flush()
            time.sleep(0.5)
    print("\r" + " " * 100, end="\r")

rBalance = 1000

def play(balance):

    clear_screen()
    print("Welcome to Roulette!")
    global rBalance;
    rBalance = int(input("Chip quantity to purchase (or '0' to cancel): ")) # input roulette balance

    if rBalance > balance: # check if user has enough balance to buy in
        print("You do not have enough balance to buy those chips.")
        return balance
    
    elif rBalance == 0:
        print("Transaction cancelled. Returning to menu.")
        time.sleep(1)
        return balance
    
    else: # if they do, let them buy in
        game_state["balance"] -= rBalance # deduct buy in from main balance

        print(f"You bought {rBalance} chips for £{rBalance}. Your balance is now £{game_state["balance"]}.")
        spinning_loading(1, "Starting game")

        while rBalance > 0: # main game loop
            
            while True: # this while True is an infinite loop that only breaks when the user inputs a valid bet amount
                        # basically just keeps checking for valid input and tells them if its invalid
                
                try:
                    bet = int((input("Enter your bet amount. Enter '0' to exit: ")))

                    if bet < 0:
                            print("Bet amount cannot be negative. Try again.") #self-explanatory
                            continue # goes back to start of while True loop

                    if bet == 0:

                        balance += rBalance

                        print(f"You cashed out your chips for £{rBalance}. Returning to desktop with £{game_state['balance']}.")
                        print("Press enter to return to menu.")
                        wait_for_keypress()
                        return game_state["balance"]

                    if bet > rBalance:
                            print("You cannot bet more chips than you have!") # self-explanatory
                            continue # goes back to start of while True loop

                    else:
                            rBalance -= bet
                            print(f"You placed a bet of {bet} chips.")
                            chosenColour = chooseValidColour() # call the function from start of code to get valid colour input ^
                            
                            colourList = ['red', 'black', 'green'] # List of colours
                            colourWeights = [16, 16, 1]  # Weights for red, black, and green

                            winningColour = random.choices(colourList, weights=colourWeights)[0] # that import random thing we were 
                                                                        # talking about where it chooses from list with the weights

                            if chosenColour == winningColour:
                                if winningColour == 'black' or winningColour == 'red':
                                    winnings = bet * 2 # if user wins on red OR black, they get double their bet
                                if winningColour == 'green':
                                    winnings = bet * 17 # if user wins on green, they get 17x their bet
                                rBalance += winnings # add winnings to roulette balance
                                spinning_loading(2, "Spinning") # call that wee spinning animation function yoke
                                print(f"You won! The winning colour was {winningColour}. Your balance is now {rBalance} chips.")
                                startnewRound()
                            else:
                                spinning_loading(2, "Spinning") # call the spin again but this time they lost
                                print(f"You lost the bet. The winning colour was {winningColour}. Your balance is now {rBalance} chips.")
                                startnewRound()

                                # also changed the whole balance wording system to just be chips instead. makes more sense i reckon
                                # so u dont get confused between main balance and roulette balance. then when u cash out it just says like
                                # you sold your chips for $x amount. W code

                except ValueError: #value error is for when the user inputs something that isnt a number, usually the whole program
                                   # just crashed if u do that, but valueerror catches exception and tells user to input valid number instead 
                    print("Invalid input. Please enter a valid number.") 

        print("Leaving the roulette table.") #bankrupt sounds a bit dramatic ngl but its shweet

        #balance += rBalance # add remaining chips to main balance again

        #return balance # return to main.py with updated balance