from itertools import groupby

from tlogic.tcards import Card
from tpattern.pattern import TPattern
from tpattern.tpatternrecognizer import TPatternRecognizer, TPatternRecResult

from typing import Set


class PassOrEmpty():
    def __init__(self):
        pass

    def __gt__(self, other):
        if isinstance(other, TPattern):
            return True
        else:
            return False


class TMulti(TPattern):
    def __init__(self, cards):
        if len(cards) > 4:
            raise ValueError("There can not be more than 4 of the same height")
        else:
            self.rank = next(iter(cards)).rank

        for card in cards:
            if card.rank != self.rank:
                # todo accept phoenix
                raise ValueError("All heights must be the same")
        self.numberof = len(cards)

    def __repr__(self):
        return "{}x{}:{}".format(self.numberof, self.rank, self.cards)

    def find(self, cards, higher=True, exact=True):
        mm = MultiRec(self.numberof, exact=exact)
        res = mm.recognize(cards, True)

        return {k:res[k] for k in res if k > self.rank}

    def __gt__(self, other):
        if isinstance(other, TMulti):
            if other.numberof != self.numberof:
                raise ValueError('Multiple - Self: {} - Other: {}'.format(self.numberof, other.numberof))
            return self.rank > other.rank
        # Problem phoenix -> make a "TSingle" class?
        elif isinstance(other, PassOrEmpty):
            return True
        else:
            # TODO: think about a better exception to raise
            raise ValueError

    def getCards(self):
        return self.cards


class MultiRec(TPatternRecognizer):
    def __init__(self, m: int, exact=False):
        self.m = m;
        self.exact = exact;

    def recognize(self, cards: Set[Card], phoenix=False) -> int:
        # do we count now
        if Card.has_phoenix(cards):
            return self.recognize_ph(cards)
        else:
            return self.recognize_wo_ph(cards)

    def recognize_ph(self, cards: Set[Card]) -> TPatternRecResult:
        rec = MultiRec(self.m - 1)
        return rec.recognize_wo_ph(cards)

    def recognize_wo_ph(self, cards: Set[Card]) -> TPatternRecResult:
        keyfunc = lambda card: card.rank
        sorted_cards = sorted(cards, key=keyfunc)

        if self.exact:
            matcher = lambda v: v == self.m
        else:
            matcher = lambda v: v >= self.m

        grouped_raw = {k:list(grp) for k,grp in groupby(sorted_cards, keyfunc)}

        grouped = {k:v for k,v in grouped_raw.items() if matcher(len(v))}

        # pairslist = {k: v for k, v in Counter(newlist).items() if matcher(v)}

        return grouped

        # print(Counter(newlist))


if __name__ == '__main__':
    from tlogic.thelpers import generate_deck, PassOrEmpty

    deck = generate_deck()

    pr = MultiRec()
    pr.recognize(deck)
