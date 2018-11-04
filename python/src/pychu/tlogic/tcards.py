from enum import Enum
from numbers import Number
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


class PHeight:
    def __gt__(self, other):
        if isinstance(other, Number):
            return other-14.1 > 0
        else:
            return False

    def __eq__(self, other):
        return False

    def __lt__(self, other):
        if isinstance(other, Number):
            return other-14.1 > 0
        else:
            return False
    def __hash__(self):
        return 14.1.__hash__()

    __str__ = lambda x: 'x'


class Special(Enum):

    mahjong = 1, 'maj'
    dog = 0.5, 'dog' # zero gives False in python
    dragon = 15, 'drn'

    phoenix = PHeight(), 'phx' # this is a placeholder

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

        if special and not rank:
            rank = special.value
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
        # Wrapped single phoenix
        # The alternative would be to just make the pattern
        # AAAARG...
        elif special == Special.phoenix and rank:
            return str(special) + str(rank)
        else:
            return str(special)

    def __eq__(self, other):
        return self.__repr__() == other.__repr__()

    def __hash__(self):
        return self.__repr__().__hash__()


def has_phoenix(cards):
    from pychu.tlogic.tcard_names import phoenix
    return phoenix in cards


def tcard(card_str: str) -> Card:
    # otherwise there would be a circular import, sigh.
    # one thing that was easier in java ;-)
    from pychu.tlogic.tcard_names import dog, dragon, phoenix, mahjong
    if card_str.startswith('dr'):
        return dragon
    elif card_str.startswith('ph'):
        return phoenix
    elif card_str.startswith('ma'):
        return mahjong
    elif card_str.startswith('do'):
        return dog
    else:
        color = Color(card_str[0])
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
        if '|' in param:
            groups = param.strip().split('|')
            return list(map(tcards, groups)) # recursion :)

        cardstrings = param.strip().split(' ')
    else:
        cardstrings = param
    cards = [out for a in cardstrings for out in __tcard__(a)]
    return cards


def __tcard__(inp: str) -> List[Card]:
    """
    Helper function to unpack
    :return: 
    """
    import re

    match = re.match(r'([rgbk]{1,4})(\d{1,2})', inp)

    if match:
        rank = match.group(2)
        return (tcard(color+rank) for color in match.group(1))
    else:
        return (tcard(inp),)

if __name__ == '__main__':
    from pychu.tlogic.tcard_names import b4, b3, k2, phoenix

    li = [k2, k2, b3, b4, b4]
    print (li)

    print(k2 in li)

    print (tcard('k2') in li)










