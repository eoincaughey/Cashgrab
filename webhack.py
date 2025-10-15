#good luck!

from game_state import game_state
import time
import sys
import os
import random
import time

#config

REVEAL_COUNT = 2 #number of letters to show
MAX_ATTEMPTS = 4 #number of guesses allowed

WORD_BANK =[
    {"word": "socket", "category": "computer", "definition": "An endpoint for sending/receiving data across a network."},
    {"word": "oracle", "category": "myth", "definition": "A person or thing providing wise counsel."},
    {"word": "zygote", "category": "biology", "definition": "A cell formed by the union of two gametes."},
    {"word": "apple", "category": "fruit", "definition": "A round fruit with red or green skin."},
    {"word": "entropy", "category": "physics", "definition": "A measure of disorder or randomness."},
    {"word": "python", "category": "programming", "definition": "A high-level programming language."},
    {"word": "nebula", "category": "astronomy", "definition": "A cloud of gas and dust in space."},
    {"word": "quasar", "category": "astronomy", "definition": "A massive and extremely remote celestial object."},
    {"word": "pomegranate", "category" : "fruit", "definition": "A tropical fruit full of seeds."},
    {"word": "tricycle", "category" : "vehicle", "definition": "Stupid bike with more than 2 wheels."},
    {"word": "ishowspeed", "category" : "memes", "definition": "A youtuber who screams a lot."},
    {"word": "algorithm", "category" : "computer science", "definition": "A step-by-step procedure for calculations."},
    {"word": "photosynthesis", "category" : "biology", "definition": "Process by which green plants make food using sunlight."},
    {"word": "eclipse", "category" : "astronomy", "definition": "An event where one celestial body moves into the shadow of another."},
    {"word": "hologram", "category" : "technology", "definition": "A three-dimensional image formed by light beams."},
    {"word": "tornado", "category" : "weather", "definition": "A violently rotating column of air extending from a thunderstorm to the ground."},
    {"word": "chameleon", "category" : "animal", "definition": "A lizard known for its ability to change color."},
    {"word": "symphony", "category" : "music", "definition": "An elaborate musical composition for a full orchestra."},
    {"word": "vaccine", "category" : "medicine", "definition": "A substance used to stimulate the production of antibodies and provide immunity against diseases."},
    {"word": "labyrinth", "category" : "mythology", "definition": "A complex network of winding passages; a maze."},
    {"word": "irnbru", "category" : "drink", "definition": "A scottish delicacy."},
    {"word": "meatsy", "category" : "memes", "definition": "Battle scars, AW DEAR!"}
]

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

def choose_word():
    return random.choice(WORD_BANK)

def reveal_letters(word):
    n = len(word)
    reveal_count = min(REVEAL_COUNT, n -1) if n > 1 else n 
    positions = random.sample(range(n), reveal_count)
    return positions 

def masked_word(word, revealed_positions):
    return " ".join(ch if i in revealed_positions else "_" for i, ch in enumerate(word)) 


def play_webhack(): 
    entry = choose_word()
    word = entry["word"].lower()
    definition = entry["definition"]

    revealed = reveal_letters(word)
    attempts = 0 

    print("--- New Word Chosen ---")
    print(f"Defintion: {definition}")

    while attempts < MAX_ATTEMPTS:
        print("\nWord:", masked_word(word, revealed))
        guess = input(f"Attempt {attempts + 1}/{MAX_ATTEMPTS} — Guess the word: ").strip().lower()

        if guess == word:
            print(f"\n✅ Correct! The word was '{word}'. Well done.")
            return True
        else:
            attempts += 1
            if attempts < MAX_ATTEMPTS:
                print("❌ Incorrect. Try again.")
            else:
                print(f"\n❌ Out of guesses. The correct word was '{word}'. Better luck next time.")

    return False

