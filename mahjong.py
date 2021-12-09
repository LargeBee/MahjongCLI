from tile import Tile, Suits, Values
from hand import Hand


def main():
    myHand = Hand()
    for handTile in myHand.generate_hand():
        print("{} of {}".format(handTile.value, handTile.suit))

if __name__ == "__main__":
    main()