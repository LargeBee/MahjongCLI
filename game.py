import random
from tile import *
from hand import Hand

class Game:
    def __init__(self):
        self.live_wall = []
        self.dead_wall = []
        self.round_wind = Winds.EAST
        self.hands = {
            Winds.EAST: Hand(Winds.EAST),
            Winds.SOUTH: Hand(Winds.SOUTH),
            Winds.WEST: Hand(Winds.WEST),
            Winds.NORTH: Hand(Winds.NORTH)
        }
    
    def print(self):
        print("Live Wall:")
        for tile in self.live_wall:
            print(tile)
        print("Dead Wall:")
        for tile in self.dead_wall:
            print(tile)

    def draw_from_live_wall(self, n=1):
        tiles = []
        for i in range(n):
            tiles.append(self.live_wall.pop(0))
        return tiles

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
        random.shuffle(tiles)
        self.live_wall = tiles[:-14]
        self.dead_wall = tiles[-14:]

    def init_hands(self):
        for i in range(3):
            for k, hand in self.hands.items():
                hand.add_tile(self.draw_from_live_wall(4))
        for k in self.hands.keys():
                hand.add_tile(self.draw_from_live_wall())

    def print_hands(self):
        for k in self.hands.keys():
            self.hands[k].print()

        

