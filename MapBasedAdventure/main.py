
""" Phase 1 """

# dictionary
player = {
    "location": "cabin",
    "inventory": []
}

game_map = {
    "cabin": {"east": "yard"}, 
    "yard": {"west": "cabin", "south": "barn", "east": "forest"}, 
    "barn": {"north": "yard"}, 
    "forest": {"west": "yard"}
}

descriptions = {
    "cabin": "You are in a quaint cabin. Go East -> Yard", 
    "yard": "You are in a spacious yard. Go West -> Cabin, Go South -> Barn, Go East -> Forest", 
    "barn": "You are in a dusty barn. Go North -> Yard", 
    "forest": "You are in a spooky forest. Go West -> Yard"
}

items = {
    "cabin": [],
    "yard": [],
    "barn": [],
    "forest": ["key"]
}

events = {
    "key barn": "You unlocked the treasure chest! Bring them back to cabin!",
    "chest cabin": "You bring the chest safely to the cabin! You win!!!!"
}

game_over = False
treasure_acquired = False

""" Phase 3 """

def look():
    print(f"Player is at: {player['location']}\n")
    print(descriptions[player['location']])

def go(direction):
    global game_over, treasure_acquired

    if direction in game_map[player["location"]]:
        # Go to different location
        player["location"] = game_map[player["location"]][direction]
        look()

        # If I am in a barn and treasure is not required, we will acquire the chest
        #if player["location"] == "barn" and treasure_acquired != True:
        #    print("Congrats, you open and collect the treasure!")
        #    treasure_acquired  = True

        # If I am back to cabin and I got a treasure chest, I win the game 
        #if player["location"] == "cabin" and treasure_acquired == True:
        #    print("Congrats, you return the chest safely! You win!!!!!")
        #    game_over = True
    else:
        print(f"You cannot go {direction}")

def get_item(item):
    if item in items[player["location"]]:
        items[player["location"]].remove(item)
        player["inventory"].append(item)
        print(f"You have sucessfully picked '{item}'")
    else:
        print(f"There is no '{item}' here")

def drop_item(item):
    if item in player["inventory"]:
        # put the item into the location
        items[player["location"]].append(item)
              
        # remove the item from the player's inventory
        player["inventory"].remove(item)
        print(f"You are no longer carrying the '{item}'")
    else:
        print(f"You don't have '{item}' in your inventory")

def inventory():
    if len(player["inventory"]) > 0:
        for item in player["inventory"]:
            print(f"You are carrying a '{item}'")
    else:
        print("You are carrying nothing")

def use_item(item):
    global game_over

    if item in player["inventory"]:
        # if I use the key in the barn, unlock the chest
        print(item + " " + player["location"])
        if item == "key" and item + " " + player["location"] in events:
            print(events[item + " " + player["location"]])
            player["inventory"].remove(item)
            player["inventory"].append("chest")

        # else if I use the chest in the cabin, I win the game
        elif item == "chest" and item + " " + player["location"] in events:
            print(events[item + " " + player["location"]])
            game_over = True

        # else
        else:
            print(f"You cannot use '{item}' in '{player["location"]}'")
    else:
        print(f"You don't have '{item}' in your inventory")

""" Phase 2 """

def main():
    global game_over

    while game_over == False:
        choice = input("What would you like to do?\n-> ").split(" ")

        if choice[0] == "go":
            go(choice[1])
        elif choice[0] == "look":
            look()
        elif choice[0] == "get":
            get_item(choice[1])
        elif choice[0] == "use":
            use_item(choice[1])
        elif choice[0] == "drop":
            drop_item(choice[1])
        elif choice[0] == "inventory":
            inventory()
        elif choice[0] == "quit":
            print("Goodbye! Thank you for playing!")
            game_over = True
        elif choice[0] == "help":
            print("Please follow the instructions below:")
            print("-------------------------------------\n")
            print("Enter 'go <space> <north OR south OR west OR east>' to go somewhere")
            print("Enter 'look' to view the room")
            print("Enter 'quit' to quit the game\n")
        else:
            print(f"I do not understand what you meant by '{choice}'\n")
main()