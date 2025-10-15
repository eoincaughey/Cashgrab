#good luck!

from game_state import game_state
import time
import sys
import os

def wait_for_keypress():
    input("")
#call wait_for_keypress() when you want the program to wait for user to press enter
#you can pair it with a line above that says print("Press enter to return/continue/etc.")
#remember python runs sequentially, so print needs to be before it waits for the keypress
#after wait for keypress is called you can call the next function
#you can see how i used it in Line 32 in the ebanking.py

def clear_screen():
    # Windows
    if os.name == 'nt':
        os.system('cls')
    # Mac/Linux
    else:
        os.system('clear')
#this is used to clear the entire terminal, use it for moving through menus or whatever
#call it with clear_screen()

def spinning_loading(duration=3, message=""):
    print(message, end="")
    for _ in range(duration):
        for dot in ". .. ...".split():
            print(f"\r{message}{dot}  ", end="")
            sys.stdout.flush()
            time.sleep(0.5)
    print("\r" + " " * 100, end="\r")
# Use this for the loading messages. It generates a message and then . . . after
# The syntax to call it is spinning_loading(time in seconds, "Message")
# the above will produce a > Message... loading animation

