from game_state import game_state
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

servers = [
    {"id": "EU01", "city": "Stockholm", "country": "Sweden"},
    {"id": "EU02", "city": "Berlin", "country": "Germany"},
    {"id": "EU03", "city": "Paris", "country": "France"},
    {"id": "EU04", "city": "London", "country": "UK"},
    {"id": "NA01", "city": "New York", "country": "USA"},
    {"id": "NA02", "city": "Los Angeles", "country": "USA"},
    {"id": "AS01", "city": "Tokyo", "country": "Japan"}
    ]

connectionStatus = "DISCONNECTED"
connectedOrDisconnected = "Connect to"
current_server = None

def chooseServer():
    clear_screen()
    print("Available servers:\n")
    for i, s in enumerate(servers, start=1):
        print(f"{i}. {s['id']}, {s['country']} ({s['city']})")
    
    global current_server
    current_server = input("\nEnter the server ID to select: ")
    matched = [s for s in servers if s['id'] == current_server]
    if matched:
        current_server = matched[0]
        print(f"\nServer selected: {current_server['city']}, {current_server['country']}")
    else:
        print("\nPlease select a valid server ID. Press enter to retry.")
        wait_for_keypress()
        chooseServer()

def connectToggle():
    global connectionStatus, connectedOrDisconnected

    if current_server != None:
        if connectionStatus == "DISCONNECTED":
            #print(f"Server selected: {servers['id']}")
            spinning_loading(3, "Connecting to server")
            connectionStatus = "CONNECTED"
        else:
            connectionStatus = "DISCONNECTED"
            #print(f"Server selected: {servers['id']}")
            spinning_loading(3, "Disconnecting from server")

        if connectionStatus == "CONNECTED":
            connectedOrDisconnected = "Disconnect from"
        else:
            connectedOrDisconnected = "Connect to"
    else:
        print("You must select a server to connect to. Press enter to view server list.")
        wait_for_keypress()
        chooseServer()
        connectToggle()
    
def menu():
    while True:
        clear_screen()
        print("\n--- VästVPN Client ---")
        print(f"1. {connectedOrDisconnected} server")
        print(f"2. Server Location List")
        print("3. Manage your subscription")
        print("4. Back")

        print()
        if current_server != None:
            city = current_server["city"]
            country = current_server["country"]
            print(f"Server: {city}, {country}")
        print(f"{connectionStatus}")

        choice = input("Choose an option: ")

        if choice == "1":
            connectToggle()

        elif choice == "2":
            chooseServer()

        elif choice == "3":
            break
            # manage subscriptions here
                
        elif choice == "4":
            break

        else:
            print("Directory does not exist.")