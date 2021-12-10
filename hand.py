import random
from tile import *

class Hand:
    def __init__(self, tiles=None):
        self.tiles = tiles

    def generate_random_valid_tile(self):
        return Tile(random.choice(list(Suits)), random.choice(list(Values)))

    def generate_random_hand(self):
        self.tiles = []
        for i in range(13):
            self.tiles.append(self.generate_random_valid_tile())
        return self.tiles