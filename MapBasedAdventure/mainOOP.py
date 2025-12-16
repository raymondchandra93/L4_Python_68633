class Player:

    # constructor & attributes/variables
    def __init__(self, start_location):
        self.location = start_location
        self.inventory = []

    # method/function
    def look(self, game):
        print(f"Player is at: {self.location}\n")
        print(game.descriptions[self.location])
    
    def show_inventory(self):
        if self.inventory:
            for item in self.inventory:
                print(f"You are carrying a '{item}'")
        else:
            print("You are carrying nothing")
    
    def go(self, direction, game):
        if direction in game.game_map[self.location]:
            # Go to different location
            self.location = game.game_map[self.location][direction]
            self.look()

        else:
            print(f"You cannot go {direction}")

""" Game Class """
class Game:
    # constructor & attributes/variables
    def __init__(self, game_map, descriptions, items):
        pass

player1 = Player("cabin")
print(player1.location)
player1.show_inventory()