import os
from game import Game
from tile import *

def clear():
    os.system('cls||clear')

def main():
    clear()
    my_game = Game()
    my_game.generate_walls()
    print(my_game)
    my_game.init_hands()
    my_game.print_hands()


if __name__ == "__main__":
    main()