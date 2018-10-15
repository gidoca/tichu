from enum import Enum
from typing import Iterable, Union, List


# todo: rename-> tcolor (avoids possible problems with GUI and stuff later on)
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
        return self.value


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
    __tichu_dict__ = {}

    __slots__ = 'color', 'rank', 'special'

    def __setattr__(self, key, value):
        raise TypeError


    def __new__(cls, color=None, rank=None, special=None):

        id_str = Card._id_(color, rank, special)
        if id_str in Card.__tichu_dict__:
            return Card.__tichu_dict__[id_str]
        else:
            o = object.__new__(cls)
            object.__setattr__(o, 'special', special)
            super(Card,o).__setattr__('rank', rank)
            super(Card,o).__setattr__('color', color)
            Card.__tichu_dict__[id_str] = o
            return o

    def __repr__(self):
        return self._id_(self.color, self.rank, self.special)

    @staticmethod
    def _id_(color=None, rank=None, special=None):
        if special is None:
            return str(color) + str(rank)
        else:
            return str(special)

    def __eq__(self, other):
        return self.__repr__() == other.__repr__()

    def __hash__(self):
        return self.__repr__().__hash__()


def has_phoenix(cards):
    for card in cards:
        if card.special == Special.phoenix:
            return card
    return None


def tcard(card_str: str) -> Card:
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


def tcards(param: Union[str, Iterable[str]]) -> List[Card]:
    """

    :param param:  String separated by space or iterable of strings

    :return:
    """
    if isinstance(param, str):
        if param == '':
            return []
        cardstrings = param.strip().split(' ')
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
