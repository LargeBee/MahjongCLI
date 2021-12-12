import os
from game import Game
from tile import *

def clear():
    os.system('cls||clear')

def main():
    clear()
    my_game = Game()
    my_game.generate_walls()
    my_game.init_hands()
    print(my_game)

if __name__ == "__main__":
    main()