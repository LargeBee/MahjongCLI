import random
from tile import *
from hand import Hand

class Game:
    def __init__(self):
        self.live_wall = []
        self.dead_wall = []
        self.round_wind = Winds.EAST
        self.hands = [
            Hand(Winds.EAST, []),
            Hand(Winds.SOUTH, []),
            Hand(Winds.WEST, []),
            Hand(Winds.NORTH, [])
        ]

    def __str__(self):
        return "Live Wall:\n{}\n\nDead Wall:\n{}"\
            .format(\
            '\n'.join([str(x) for x in self.live_wall]),\
            '\n'.join([str(x) for x in self.dead_wall]))

    def print_hands(self):
        for hand in self.hands:
            print(hand)

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
            for hand in self.hands:
                hand.add_tile(self.draw_from_live_wall(4))
        for hand in self.hands:
                hand.add_tile(self.draw_from_live_wall())

        

