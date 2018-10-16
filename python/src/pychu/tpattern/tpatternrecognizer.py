import abc
from typing import Set, List

from pychu.tlogic.tcards import Card
from pychu.tpattern.pattern import TPattern


# Haha, to much java programming
# In python we could just have
# a function. But not sure if this would be better
class TPatternRecognizer(metaclass=abc.ABCMeta):

    @abc.abstractclassmethod
    # The number of occurances + if overlapping or not should be
    # communicated as well
    # -> Create a resultObject
    # does this make sense? filter afterwards would make the api here easier...
    # however, recognizing would be more efficient
    def recognize(self, cards: Set[Card], phoenix=False, existingPattern: TPattern = None) -> List[TPattern]:
        """

        :param cards: The set of cards to look into
        :param phoenix: Should the Phoenix be considered? If False(default) the presence of the phoenix is completely ignored
        :param existingPattern: If an existing pattern is given, only matches that beat the existing pattern are returned. For example:
        cards are "b4 g4 c5 k5" and the given pattern is "c4 k4" only 1 beating pattern is returned.
        """
        pass
