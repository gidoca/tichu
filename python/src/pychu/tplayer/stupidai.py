from typing import Set, Callable

# noinspection PyUnresolvedReferences
from pychu.tlogic.tcards import Card
from pychu.tlogic.thelpers import rec_pattern_unique
from pychu.tpattern.multiples import MultiRec
from pychu.tplayer.tplayer import TPlayer


class StupidAI(TPlayer):

    def play(self, table_cards: Set[Card], card_receiver: Callable[[Set[Card]], bool], wish=None) -> None:
        cards = []
        if self.hand:
            if len(table_cards) == 0:
                cards = self.start()
            else :
                cards = self.react(table_cards)

        card_receiver(cards)
        self.hand.difference_update(cards)

    def react(self, table_cards):
        pattern = rec_pattern_unique(table_cards)
        possible_cards = pattern.find(self.hand)
        try:
            first = next(iter(possible_cards))

            cards = set(possible_cards[first])

        except Exception as e:
            print(e)
            cards = set()

        return cards

    def start(self):
        triples = MultiRec(3, True).recognize(self.hand)
        pairs = MultiRec(2, True).recognize(self.hand)
        singles = MultiRec(1, True).recognize(self.hand)
        tmin = min(triples.items()) if triples else (100,set())
        pmin = min(pairs.items()) if pairs else (99,set())
        smin = min(singles.items()) if singles else (98,set())

        cards = min((tmin,pmin,smin))

        card = min(self.hand, key=lambda c: c.rank)
        # cards = {card}
        return cards[1]
