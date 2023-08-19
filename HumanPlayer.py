import re

from Player import Player
from PlayerException import PlayerException


class HumanPlayer(Player):

    def __init__(self, name, identity):
        super().__init__(name, identity)

    def move(self):
        move = input("Enter position to play: ")
        pat = re.compile(r"[1-9]+")
        if re.fullmatch(pat, move):
            return move
        else:
            raise PlayerException("Invalid Input")
