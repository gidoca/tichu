from itertools import groupby
from typing import Set, Dict, List

from pychu.tlogic.tcards import Card, has_phoenix
from pychu.tlogic.tcard_names import phoenix
from pychu.tpattern.pattern import TPattern
from pychu.tpattern.tpatternrecognizer import TPatternRecognizer



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
        self.cards = cards
        if not cards:
            raise ValueError("At least one Card must be given!")
        elif len(cards) > 4:
            raise ValueError("There can not be more than 4 of the same height")

        prev_rank = None
        cnt_wo_phx = 0
        phx = False
        for c in cards:
            if c.__eq__(phoenix):
                phx = True
            elif prev_rank and prev_rank != c.rank:
                # todo accept phoenix
                raise ValueError("All heights must be the same")
            else:
                prev_rank = c.rank
                cnt_wo_phx += 1

        self.rank = prev_rank

        if cnt_wo_phx < 3:
            self.numberof = cnt_wo_phx + phx
        else:
            self.numberof = cnt_wo_phx

    def __repr__(self):
        return "{}@{}:{}".format(self.numberof, self.rank, self.cards)

    def find(self, cards, higher=True, exact=True):
        mm = MultiRec(self.numberof, exact=exact)
        res = mm.recognize(cards, True)

        return {k: res[k] for k in res if k > self.rank}

    def __gt__(self, other):
        if isinstance(other, TMulti):
            return self.numberof == other.numberof and self.rank > other.rank
        # Problem phoenix -> make a "TSingle" class?
        elif isinstance(other, PassOrEmpty):
            return True
        else:
            return False


class MultiRec(TPatternRecognizer):
    def __init__(self, m: int, exact=False):
        self.m = m;
        self.exact = exact;

    #todo: phoenix=True makes more sense
    #todo: add greedy flag (now the phx is only used when needed)
    #todo: is m needed?
    def recognize(self, cards: Set[Card], phoenix=False) -> Dict[int, List[Card]]:
        # do we count now
        if has_phoenix(cards):
            return self.recognize_ph(cards)
        else:
            return self.recognize_wo_ph(cards)

    def recognize_ph(self, cards: Set[Card]) -> Dict[int, List[Card]]:
        rec = MultiRec(self.m - 1)
        add_phx = lambda v: v if len(v)>= self.m else v + [phoenix]
        return {k:add_phx(v) for k,v in rec.recognize_wo_ph(cards).items()}

    def recognize_wo_ph(self, cards: Set[Card]) -> Dict[int, List[Card]]:
        keyfunc = lambda card: card.rank
        nonspec = lambda card: card.special is not phoenix
        sorted_cards = sorted(filter(nonspec, cards), key=keyfunc)


        if self.exact:
            matcher = lambda v: v == self.m
        else:
            matcher = lambda v: v >= self.m

        grouped_raw = {k: list(grp) for k, grp in groupby(sorted_cards, keyfunc)}

        grouped = {k: v for k, v in grouped_raw.items() if matcher(len(v))}

        # pairslist = {k: v for k, v in Counter(newlist).items() if matcher(v)}

        # return {k:TMulti(v) for k,v in grouped.items()}

        return grouped;

        # print(Counter(newlist))


if __name__ == '__main__':

    # That is a looping import..
    from pychu.tlogic.tcard_names import generate_deck

    deck = generate_deck()

    pr = MultiRec()
    pr.recognize(deck)
