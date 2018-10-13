from typing import Set

from tlogic.tcards import Card
from tpattern.pattern import TPattern


class PFullHouse(TPattern):
    def __init__(self, triple: TTriple, pair: TPair):
        self.triple = triple
        self.pair = pair

    def getCards(self) -> Set[Card]:
        return self.triple.getCards() + self.pair.getCards()



