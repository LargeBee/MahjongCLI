import random
from tile import *

class Hand:
    def __init__(self, tiles=[]):
        self.tiles = tiles

    def print(self):
        print("Hand:")
        for tile in self.tiles:
            print(tile)

    def remove_tile(self, tile):
        self.tiles.remove(tile)
        self.sort_hand()
    
    def add_tile(self, tile):
        self.tiles.append(tile)
        self.sort_hand()

    def sort_hand(self):
        pass