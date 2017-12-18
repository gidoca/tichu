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
                height = int(str[1])
                return Card(color=color, height=height);


def mapcolor(str: str):
    if str=='r':
        return Color.red;
    if str=='k': # Karbon
        return Color.black
    if str == 'b':
        return Color.blue
    if str == 'g':
        return Color.green


dragon = Card(special=Special.dragon, height=18)
phoenix = Card(special=Special.phoenix, height=17)
mahjong = Card(special=Special.mahjong, height=1)
dog = Card(special=Special.dog, height=-2)

