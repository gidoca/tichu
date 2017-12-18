import abc
from typing import Set
from tlogic import Card


class TPatternRecognizer(metaclass=abc.ABCMeta):

    @abc.abstractclassmethod
    def recognize(self, cards: Set[Card], phoenix=False) -> bool:
        pass
