from __future__ import annotations
from itertools import groupby
from typing import Set, Dict, List

from pychu.tlogic.tcard_names import phoenix
from pychu.tlogic.tcards import Card, has_phoenix
from pychu.tpattern.tpattern import TPattern, TPatternEmpty


class TMulti(TPattern):

    cardinality = None
    rank = None
    essential_cards = None
    redundant_cards = None

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
            elif prev_rank is not None and prev_rank != c.rank:
                # todo accept phoenix
                raise ValueError("All heights must be the same")
            else:
                prev_rank = c.rank
                cnt_wo_phx += 1

        self.rank = prev_rank

        if cnt_wo_phx < 3:
            self.cardinality = cnt_wo_phx + phx
        else:
            self.cardinality = cnt_wo_phx


    def __repr__(self):
        return "{}@{}:{}".format(self.cardinality, self.rank, self.cards)

    def find(self, cards, higher=True):
        mm = TMultiFinder(self.cardinality, False)
        res, left = mm.recognize(cards, True)

        return {k: res[k] for k in res if k > self.rank}, left

    def __gt__(self, other):
        if isinstance(other, TMulti):
            return self.cardinality == other.cardinality and self.rank > other.rank
        # Problem phoenix -> make a "TSingle" class?
        elif isinstance(other, TPatternEmpty):
            return True
        else:
            return False











# hm, create a plain function?
# Not sure if multifinding in stead of fix finders for 1,2,3,4 makes life any easier.

class TMultiFinder():

    # TODO: Greedy flag
    # Howto handle phoenix?
    # REdesign exact flag into rather make num a range...
    def __init__(self, num: int, exact: bool):
        self.m = num
        self.exact = exact


    def recognize(self, cards: Set[Card], phoenix=True) -> (Dict[int, List[Card]], Set[Card]):

        # do we count now
        if has_phoenix(cards):
            return self.recognize_ph(cards)
        else:
            return self.recognize_wo_ph(cards)

    def recognize_ph(self, cards: Set[Card]) -> Dict[int, List[Card]]:
        #TODO: also check m (without phoenix)
        rec = TMultiFinder(self.m, self.exact)
        add_phx = lambda v: v if len(v)>= self.m else v + [phoenix]
        ca_wo_ph = list(cards); ca_wo_ph.remove(phoenix)
        vals, leftovers = rec.recognize_wo_ph(ca_wo_ph)
        if vals:
            if self.exact:
                return vals, leftovers
            else:
                return {k:add_phx(v) for k,v in vals.items()}, leftovers
        else:
            rec = TMultiFinder(self.m-1, self.exact)
            vals, leftovers = rec.recognize_wo_ph(ca_wo_ph)
            return {k:add_phx(v) for k,v in vals.items()}, leftovers

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


        leftovers = [o for k,v in grouped_raw.items() if not matcher(len(v)) for o in v]
        # pairslist = {k: v for k, v in Counter(newlist).items() if matcher(v)}

        # return {k:TMulti(v) for k,v in grouped.items()}

        return grouped, leftovers;



