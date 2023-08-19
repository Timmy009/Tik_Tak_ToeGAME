import re
from abc import ABC, abstractmethod

from PlayerException import PlayerException


class Player(ABC):

    def __init__(self, name, identity):
        pat = re.compile(r"[A-Za-z]+")
        if re.fullmatch(pat, name):
            self.name = name
        else:
            raise PlayerException("Invalid Input")
        if re.fullmatch(pat, identity):
            self.identity = identity
        else:
            raise PlayerException("Invalid Input")

    @abstractmethod
    def move(self):
        pass

    def get_player_name(self):
        return self.name

    def get_player_identity(self):
        return self.identity
