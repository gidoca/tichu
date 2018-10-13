from idlelib.debugger_r import tracebacktable
from inspect import Traceback
from typing import Set, Callable

from tgame.tplayer import TPlayer
from tlogic.tcards import Card
from tlogic.thelpers import rec_pattern_unique


class StupidAI(TPlayer):

    def play(self, table_cards: Set[Card], card_receiver: Callable[[Set[Card]], bool], wish=None) -> None:
        cards = []
        if len(table_cards) == 0:
            cards = self.start()
        else:
            cards = self.react(table_cards)

        card_receiver(cards, self.cards)
        self.cards.difference_update(cards)

    def react(self, table_cards):
        pattern = rec_pattern_unique(table_cards)
        possible_cards = pattern.find(self.cards)
        try:
            first = next(iter(possible_cards))

            cards = set(possible_cards[first])

        except Exception as e:
            print(e)
            cards = set()

        return cards

    def start(self):
        # single
        card = min(self.cards, key=lambda c: c.rank)
        cards = {card}
        return cards
