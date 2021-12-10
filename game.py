from tile import Winds

class Game:
    def __init__(self):
        self.live_wall = []
        self.dead_wall = []
        self.round_wind = Winds.EAST

    def generate_walls(self):
        pass