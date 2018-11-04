from enum import Enum, auto


# What is it good for?
class TablePattern(Enum):
    Single = auto()
    Pair = auto()
    Triple = auto()
    FullHouse = auto()
    Straight = auto()
    DoubleStraight = auto()
    Bomb = auto ()
    StraightBomb = auto()
