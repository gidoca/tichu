import abc
from collections import namedtuple
from typing import Set
from tlogic import Card



class TPatternRecognizer(metaclass=abc.ABCMeta):


    @abc.abstractclassmethod
    # TODO: the result is more complicated.
    # The number of occurances + if overlapping or not should be
    # communicated as well
    # -> Create a resultObject
    def recognize(self, cards: Set[Card], phoenix=False) -> int:
        pass
