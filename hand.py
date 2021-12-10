from tile import *

class Hand:
    def __init__(self, seat_wind=Winds.EAST, tiles=[]):
        self.seat_wind = seat_wind
        self.tiles = tiles

    def print(self):
        print("\nHand {0}:".format(self.seat_wind))
        for tile in self.tiles:
            print(tile)

    def remove_tile(self, tile):
        self.tiles.remove(tile)
        #self.sort_hand()
    
    def add_tile(self, tile):
        self.tiles += tile
        #self.sort_hand()

    #def sort_hand(self):
    #    pass