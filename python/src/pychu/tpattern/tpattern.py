from __future__ import annotations

from abc import ABC, abstractmethod, abstractproperty
from typing import Dict, Set

from pychu.tlogic.tcards import Card


class TPattern(ABC):

    """
    Pattern that uses all the Cards given

    By Convention all Patterns have a __init__
    that takes exactly the cards[iterable] as positional argument
    IndexedSet is used for storage
    """

    @abstractproperty
    def cardinality(self) -> int:
        """
        The power of a pattern. E.g. straights the length,
        :return:
        """
        pass

    @abstractproperty
    def rank(self):
        """
        Lowest card of the pattern
        :return:
        """
        pass

    @abstractmethod
    def find(self, cards, higher=True):
        pass

    """
    Pattern that has a few redundant cards
    however no leftover cards
    """

    # Todo: leave this to the subclasses
    @abstractproperty
    def redundant_cards(self) -> Dict[int,Set[Card]]:
        """
        Cards that are substituteable
        :return:
        """
        pass

    @abstractproperty
    def essential_cards(self)-> Set[Card]:
        """
        Cards only available once!
        :return:
        """
        pass


    def gt_table(self, other: TPattern):
        """
        Only greater if pattern matches exactly
        :param other:
        :return:
        """
        if isinstance(other, self.__class__):
            return self.cardinality == other.cardinality and self.rank > other.rank
        elif isinstance(other, TPatternEmpty):
            return True
        else:
            return False #or an exception? Na, it is not beating for whatever reasons.

    def gt_hand(self, other: TPattern):
        """
        Greater if it is of higher rank and at least the same cardinality
        Especially usefull for knowing if one could beat the other pattern at all
        :param other:
        :return:
        """
        if isinstance(other, self.__class__):
            return self.cardinality >= other.cardinality and self.rank > other.rank
        elif isinstance(other, TPatternEmpty):
            return True
        else:
            return False

    def select_optimal_combination(self, table_pattern, constraints ):
        pass


    def __repr__(self):

        return self.__class__.__name__ + str(self.essential_cards) + str(self.redundant_cards)


class TPatternEmpty():
    def __init__(self):
        pass


