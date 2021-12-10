import os
from game import Game
from tile import *

def clear():
    os.system('cls||clear')

def main():
    clear()
    my_game = Game()
    my_game.generate_walls()
    print("\n")
    #my_game.print()
    print("\n")

    my_game.hands[Winds.EAST].print()
    my_game.hands[Winds.SOUTH].print()

    my_game.hands[Winds.EAST].add_tile([Tile(Suits.BAMBOO, Values.EIGHT)])
    
    my_game.hands[Winds.EAST].print()
    my_game.hands[Winds.SOUTH].print()
    #my_game.init_hands()
    print("\n")
    #my_game.print_hands()


if __name__ == "__main__":
    main()