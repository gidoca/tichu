from typing import Set

from tlogic.tcards import Card
from tpattern.multiples import MultiRec
from tpattern.tpatternrecognizer import TPatternRecognizer


def find_bombs(cards):
    buffer = []
    out = []
    first = True
    for card in cards:
        if first:
            first = False
            buffer.append(card)
        else:
            if lastCard.height-card.height == 0:
                buffer.append(card)
            else:
                if len(buffer) == 4:
                    out.append(buffer)
                buffer = [card,]
        lastCard = card
    return out

class PBombs(TPatternRecognizer):
    def recognize(self, cards: Set[Card], phoenix=False) -> int:
        if not phoenix:
            return find_bombs(cards)
        else:
            mr = MultiRec(4, phoenix)

        pass