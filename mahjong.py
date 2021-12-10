import os
from tile import Tile, Suits, Values
from hand import Hand

def clear():
    os.system('cls||clear')

def main():
    myHand = Hand()
    clear()
    for handTile in myHand.generate_hand():
        print("{} of {}".format(handTile.value, handTile.suit))

if __name__ == "__main__":
    main()