
# game_state = {
#    "balance": 15000,
#    "reputation": 0,
#    "noOfEmailAddresses": 0,}

# this was game_state.py in v1.0.0 ^ info about changes at bottom of file

import json 
import os
import atexit

def clear_screen():
    # Windows
    if os.name == 'nt':
        os.system('cls')
    # Mac/Linux
    else:
        os.system('clear')

SAVE_FILE = "savegame.json"

game_state = { #actual game_state stored here v also in savegame file once program is closed.
    "balance": 15000,
    "reputation": 0,
    "noOfEmailAddresses": 0,
    }

if os.path.exists(SAVE_FILE):
    with open(SAVE_FILE, "r") as f: #opens the savegame file
        game_state = json.load(f) #reads the contents

def save_game():
    with open(SAVE_FILE, "w") as f: #opens the savegame file
        json.dump(game_state, f, indent=4) #dumps (writes) the contents back in to the json
    clear_screen()
    print("Game saved!")

atexit.register(save_game) #atexit is a module that runs when program is stopped

# amended as above in order to save the game_state
# as a .json file which can be persistent between runs.
# so now we can make savegames and keep the money value after
#the program is stopped.