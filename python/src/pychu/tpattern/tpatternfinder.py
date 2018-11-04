from __future__ import annotations

import abc
from abc import abstractmethod
from typing import Set, List

from pychu.tlogic.tcards import Card
from pychu.tpattern.tpattern import TPattern


class TPatternFinder(abc.ABC):


    @abstractmethod
    # The number of occurances + if overlapping or not should be
    # communicated as well
    # -> Create a resultObject
    # does this make sense? filter afterwards would make the api here easier...
    # however, recognizing would be more efficient
    def recognize(self, cards: Set[Card], phoenix=False, existingPattern: TPattern = None) -> List[Set[Card]]:
        """

        :param cards: The set of cards to look into
        :param phoenix: Should the Phoenix be considered? If False(default) the presence of the phoenix is completely ignored
        :param existingPattern: If an existing pattern is given, only matches that beat the existing pattern are returned. For example:
        cards are "b4 g4 c5 k5" and the given pattern is "c4 k4" only [c5,k5] is returned.
        """












