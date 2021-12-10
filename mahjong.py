import os
from game import Game
from tile import *

def clear():
    os.system('cls||clear')

def main():
    my_game = Game()
    my_game.generate_walls()
    my_game.print()

    for i in range(13):
        my_game.hands[Winds.EAST].add_tile(my_game.draw_from_wall())
    my_game.hands[Winds.EAST].print()

if __name__ == "__main__":
    main()