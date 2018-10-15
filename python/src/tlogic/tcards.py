from enum import Enum
from typing import Iterable, Union


class Color(Enum):
    """
    Represents the Tichu color scheme:

    """
    red = 'r', 'star'
    blue = 'b', 'house'
    green = 'g', 'emerald'
    black = 'k', 'sword'

    def __new__(cls, value, shape: str):
        color = object.__new__(cls)
        color._value_ = value
        color.shape = shape
        return color

    def __str__(self):
        return self.name[0]


class Special(Enum):
    mahjong = 1, 'maj'
    dog = 2, 'dog'
    dragon = 3, 'drn'
    phoenix = 4, 'phx'

    def __new__(cls, value, short: str):
        special = object.__new__(cls)
        special._value_ = value
        special.short = short
        return special

    def __str__(self):
        return self.short


class Card:
    # TODO special and None color is the same property
    def __init__(self, color=None, rank=None, special=None):
        self.special = special
        self.rank = rank
        self.color = color

    def __repr__(self):
        if self.special is not None:
            return str(self.special)
        else:
            return str(self.color) + str(self.rank)

    def __eq__(self, other):
        return self.__repr__() == other.__repr__()

    def __hash__(self):
        return self.__repr__().__hash__()

    @staticmethod
    def has_phoenix(cards):
        for card in cards:
            if card.special == Special.phoenix:
                return card
        return None


def tcard(card_str: str):
    if card_str.startswith('dr'):
        return dragon
    elif card_str.startswith('ph'):
        return phoenix
    elif card_str.startswith('ma'):
        return mahjong
    elif card_str.startswith('do'):
        return dog
    else:
        color = mapcolor(card_str[0])
        rank = int(card_str[1:])
        return Card(color=color, rank=rank);


def tcards(param: Union[str, Iterable[str]]):
    """

    :param param:  String separated by space or iterable of strings

    :return:
    """
    if isinstance(param, str):
        cardstrings = param.split(' ')
    else:
        cardstrings = param
    cards = list(map(tcard, cardstrings))
    return cards


def mapcolor(color: str) -> Color:
    return Color(color)


dragon = Card(special=Special.dragon, rank=18)
# That will be problematic when played onto a single card
phoenix = Card(special=Special.phoenix, rank=17)
mahjong = Card(special=Special.mahjong, rank=1)
dog = Card(special=Special.dog, rank=-2)
