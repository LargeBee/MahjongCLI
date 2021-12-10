import os
from tile import Tile, Suits, Values
from hand import Hand
from game import Game

def clear():
    os.system('cls||clear')

def main():
    myGame = Game()
    myGame.generate_walls()
    myGame.print_walls()


if __name__ == "__main__":
    main()