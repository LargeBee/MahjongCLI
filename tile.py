from enum import Enum

class Suits(Enum):
    PIN = 1
    BAMBOO = 2
    CHARACTER = 3
    HONOUR = 4


class Tile:
    def __init__(self, suit, value, red = False):
        self.suit = suit
        self.value = value
        self.red = red