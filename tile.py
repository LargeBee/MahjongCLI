from enum import Enum

class Suits(Enum):
    PIN = 1
    BAMBOO = 2
    CHARACTER = 3
    WIND = 4
    DRAGON = 5

class Values(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    EAST = 10
    SOUTH = 11
    WEST = 12
    NORTH = 13
    RED_DRAGON = 14
    GREEN_DRAGON = 15
    WHITE_DRAGON = 16

class Tile:
    def __init__(self, suit, value, red=False):
        self.suit = suit
        self.value = value
        self.red = red
