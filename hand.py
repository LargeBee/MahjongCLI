from tile import *

class Hand:
    def __init__(self, seat_wind=Winds.EAST, tiles=[]):
        self.seat_wind = seat_wind
        self.tiles = tiles

    def __str__(self):
        return "\n{} Hand:\n{}".format(self.seat_wind.name.title(), '\n'.join([str(x) for x in self.tiles]))

    def remove_tile(self, tile):
        self.tiles.remove(tile)
        #self.sort_hand()
    
    def add_tile(self, tile):
        self.tiles += tile
        #self.sort_hand()

    #def sort_hand(self):
    #    pass