import random
from tile import *

class Hand:
    def __init__(self, tiles=None):
        self.tiles = tiles

    def generate_hand(self):
        self.tiles = []
        for i in range(13):
            self.tiles.append(Tile(random.choice(list(Suits)), random.choice(list(Values))))
        return self.tiles