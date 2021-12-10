import os
from tile import Tile, Suits, Values
from hand import Hand
from game import Game

def clear():
    os.system('cls||clear')

def main():
    my_game = Game()
    my_game.generate_walls()
    my_game.print()

    my_hand = Hand()
    for i in range(13):
        my_hand.add_tile(my_game.draw_from_wall())
    my_hand.print()

if __name__ == "__main__":
    main()