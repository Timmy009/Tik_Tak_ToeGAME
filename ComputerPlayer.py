import random
from random import randint

from Player import Player


class ComputerPlayer(Player):
    def __init__(self, name, identity):
        super().__init__(name, identity)

    def move(self):
        return str(random.randint(1, 10))
