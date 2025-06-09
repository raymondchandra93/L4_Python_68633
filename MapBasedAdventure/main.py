
""" Phase 1 """

names = ["A", "B", "C"]

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

game_over = False

""" Phase 3 """

def look():
    print(f"Player is at: {player['location']}\n")

def go(direction):
    if direction in game_map[player["location"]]:
        pass
    else:
        pass

""" Phase 2 """

def main():
    global game_over

    while game_over == False:
        choice = input("What would you like to do?\n-> ").split(" ")

        if choice[0] == "go":
            go(choice[1])
        elif choice[0] == "look":
            look()
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