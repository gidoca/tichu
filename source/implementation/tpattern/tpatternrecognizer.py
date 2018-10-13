import abc
from collections import namedtuple
from dataclasses import dataclass
from typing import Set, List
from tlogic.tcards import Card
from tpattern.pattern import TPattern


@dataclass
class TPatternRecResult:
    unique : int
    overlapping : int
    patterns : Set[TPattern]

    # def __str__(self):
    #     return self.unique + ' / ' + self.overlapping + "\n" + self.patterns

# Haha, to much java programming
# In python we could just have
# a function. But not sure if this would be better
class TPatternRecognizer(metaclass=abc.ABCMeta):


    @abc.abstractclassmethod
    # TODO: the result is more complicated.
    # The number of occurances + if overlapping or not should be
    # communicated as well
    # -> Create a resultObject
    def recognize(self, cards: Set[Card], phoenix=False, existingPattern: TPattern=None) -> TPatternRecResult:
        """

        :param cards: The set of cards to look into
        :param phoenix: Should the Phoenix be considered? If False(default) the presence of the phoenix is completely ignored
        :param existingPattern: If an existing pattern is given, only matches that beat the existing pattern are returned. For example:
        cards are "b4 g4 c5 k5" and the given pattern is "c4 k4" only 1 beating pattern is returned.
        """
        pass





