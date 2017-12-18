from enum import Enum


class Color(Enum):
    red = 1
    blue = 2
    green = 3
    black = 4
    def __str__(self):
        return self.name[0]


class Special(Enum):
    mahjong = 1
    dog = 2
    dragon = 3
    phoenix = 4
    def __str__(self):
        return self.name[0:2]


class Card:
    # TODO special and None color is the same property
    def __init__(self, color=None, height=-1, special=None):
        self.special = special
        self.height = height
        self.color = color

    def __repr__(self):
        if self.special is not None:
            return str(self.special)
        else:
            return str(self.color)+str(self.height)


    # TODO move to helper class
    @staticmethod
    def has_phoenix( cards ):
        for card in cards:
            if card.special == Special.phoenix:
                return card
        return None

