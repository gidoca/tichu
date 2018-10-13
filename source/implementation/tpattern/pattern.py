import abc

from tlogic.tcards import Card
from typing import Set, Collection


class TPattern(metaclass=abc.ABCMeta):

    def __init__(self, cards: Collection[Card]):
        self.cards = cards

    @abc.abstractclassmethod
    def getCards(self) -> Set[Card]:
        pass

    @abc.abstractmethod
    def find(self, cards, higher=True, exact=True):
        pass

