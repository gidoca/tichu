import abc
from collections import namedtuple
from typing import Set
from tlogic import Card



# Haha, to much java programming
# In python we could just have
# a function. But not sure if this would be better
class TPatternRecognizer(metaclass=abc.ABCMeta):


    @abc.abstractclassmethod
    # TODO: the result is more complicated.
    # The number of occurances + if overlapping or not should be
    # communicated as well
    # -> Create a resultObject
    def recognize(self, cards: Set[Card], phoenix=False) -> int:
        pass
