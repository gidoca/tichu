from enum import Enum


class Color(Enum):
    red = 1
    blue = 2
    green = 3
    karbon = 4
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
    def __init__(self, color=None, rank=None, special=None):
        self.special = special
        self.rank = rank
        self.color = color

    def __repr__(self):
        if self.special is not None:
            return str(self.special)
        else:
            return str(self.color)+str(self.rank)

    def __eq__(self, other):
        return self.__repr__() == other.__repr__()

    def __hash__(self):
        return self.__repr__().__hash__()


    @staticmethod
    def has_phoenix( cards ):
        for card in cards:
            if card.special == Special.phoenix:
                return card
        return None

    @staticmethod
    def from_string(str: str):
            if(str=='dr'):
               return dragon
            elif(str == 'ph'):
                return phoenix
            elif(str=='ma'):
                return mahjong
            elif(str == 'do'):
                return dog
            else:
                color = mapcolor(str[0])
                rank = int(str[1:])
                return Card(color=color, rank=rank);

    @staticmethod
    def mstr(param: str):
        cardstrings = param.split(' ')
        cards = list(map(Card.from_string, cardstrings))
        return cards


def mapcolor(str: str):
    if str=='r':
        return Color.red;
    if str=='k': # Karbon
        return Color.karbon
    if str == 'b':
        return Color.blue
    if str == 'g':
        return Color.green


dragon = Card(special=Special.dragon, rank=18)
# That will be problematic when played onto a single card
phoenix = Card(special=Special.phoenix, rank=17)
mahjong = Card(special=Special.mahjong, rank=1)
dog = Card(special=Special.dog, rank=-2)

