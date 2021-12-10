import random
from tile import *

class Hand:
    def __init__(self, tiles=None):
        self.tiles = tiles

    def remove_tile(self, tile):
        self.tiles.pop(tile)
        self.sort_hand()
    
    def add_tile(self, tile):
        self.tiles.append(tile)
        self.sort_hand()

    def sort_hand(self):
        pass