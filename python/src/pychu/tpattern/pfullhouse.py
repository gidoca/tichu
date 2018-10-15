from typing import Set

from pychu.tlogic.tcards import Card
from pychu.tpattern.pattern import TPattern


class PFullHouse(TPattern):
    def __init__(self, triple: TPattern, pair: TPattern):
        self.triple = triple
        self.pair = pair

    def getCards(self) -> Set[Card]:
        return self.triple.getCards + self.pair.getCards



