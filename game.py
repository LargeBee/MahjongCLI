from tile import *

class Game:
    def __init__(self):
        self.live_wall = []
        self.dead_wall = []
        self.round_wind = Winds.EAST
    
    def print_walls(self):
        print("Live Wall:")
        for tile in self.live_wall:
            print(tile)
        print("Dead Wall:")
        for tile in self.dead_wall:
            print(tile)

    def generate_walls(self):
        tiles = []
        for suit in Suits:
            match suit:
                case Suits.PIN | Suits.BAMBOO | Suits.CHARACTER:
                    for v in Values:
                        tiles += [Tile(suit, v)] * 4
                case Suits.WIND:
                    for w in Winds:
                        tiles += [Tile(suit, w)] * 4
                case Suits.DRAGON:
                    for d in Dragons:
                        tiles += [Tile(suit, d)] * 4
        self.live_wall = tiles[:-14]
        self.dead_wall = tiles[-14:]
        

