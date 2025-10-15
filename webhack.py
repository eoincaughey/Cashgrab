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

    SSHcode = random.randint(100000,999999)

    print("=== SSH Breach Tool ===")
    print("Challenge key generated.")
    print(f"Definition: {definition}")

    while attempts < MAX_ATTEMPTS:
        print("\nHint:", masked_word(word, revealed))
        guess = input(f"Attempt {attempts + 1}/{MAX_ATTEMPTS} — Enter challenge key: ").strip().lower()

        if guess == word:
            spinning_loading(3, "Testing challenge key")
            print(f"\nChallenge key accepted. SSH code generated: {SSHcode}")
            SSHcodeTest = int(input("Enter generated SSH breach code: "))
            if SSHcodeTest == SSHcode:
                print("SSH code valid. Initiating breach sequence.")
                spinning_loading(6, "Breaching SSH node")
                return True
                
        else:
            attempts += 1
            if attempts < MAX_ATTEMPTS:
                print(f"Challenge key denied. {attempts + 1} solve attempts remaining.")
            else:
                print(f"\nChallenge key denied. Maximum attempts reached, terminating SSH breach.")

    return False



# Mock filesystem contents for your in-game root directory.


fs = {

    "app": [
        "PowerPoint.app",
        "Excel.app",
        "Word.app",
        "Edge.app"
    ],
    "bin": [
        "game_server",
        "daemon_launcher",
        "backup_tool",
        "log_rotator"
    ],
    "config": [
        "app.conf",
        "secrets.env (LOCKED)",
        "deploy_notes.txt",
        "feature_flags.json"
    ],
    "data": [
        "users.db",
        "saves/",
        "economy/ledger_2025.qry",
        "cache/"
    ],
    "logs": [
        "access.log",
        "error.log",
        "audit.log"
    ],
    "backup": [
        "nightly_2025-10-01.tar.gz",
        "weekly_2025-09-28.tar.gz"
    ],
    # /home subtree
    "home/.ssh": [
        "authorized_keys",
        "id_rsa.pub"
    ],
    "home/documents": [
        "resume.docx",
        "project_report.pdf",
        "meeting_notes.txt"
    ],
    "home/pictures": [
        "avatar_123.png",
        "banner.jpg",
        "screenshot_2025-10-01.png"
    ],
    "home/videos": [
        "intro.mp4",
        "promo_clip.mov"
    ],
}
path = ""
norm = ""

def open_dir(path):
    
    global norm

    path = input("Choose directory to navigate: ")
    norm = path.strip().strip("/")
    # Support calling 'home' to list top-level home entries
    if norm == "home":
        clear_screen()
        children = [p.split("/",1)[1] for p in fs.keys() if p.startswith("home/")]
        # unique and sorted
        children = sorted(set(children))
        print(f"/home/:")
        for c in children:
            print(c)

    if norm in fs:
        clear_screen()
        print(f"{norm}/:")
        for item in fs[norm]:
            print(item)

    elif f"home/{norm}" in fs:
        clear_screen()
        print(f"home/{norm}/:")
        for item in fs[f"home/{norm}"]:
            print(item)
    elif norm in ["root", "cd .."]:
        rootTree()
    elif norm != "home":
        print(f"No such directory mocked: '{path}'.")

# Example usage: print every root entry and then open each one.
def rootTree():
    root_entries = ["app","bin","config","data","logs","backup","home","home/.ssh","home/documents","home/pictures","home/videos"]
    if norm == "root" or "cd ..":
        clear_screen()
        print("root:")
        for e in root_entries:
            if e == "home":
                print("/home/")
            else:
                print(f"└─ {e}/")
        print("\n")
        open_dir(path)

    # Open each and show contents (example output)
    for e in root_entries:
        open_dir(e)
        print("-" * 30)

open_dir(path)