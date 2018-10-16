import sys
from typing import Set

from pychu.tgame.server import TEvent
# noinspection PyUnresolvedReferences
from pychu.tplayer.tplayer import TPlayer
from pychu.tlogic.tcards import Card, tcards


class HumanPlayer(TPlayer):
    """
    A simple human player taking commands from stdin
    """

    # This might make testability already difficult
    def init(self, cards: Set[Card], player_number: int):
        super().init(cards, player_number)
        print("You are player {}".format(self.player_number))

    def play(self, lastcards: Set[Card], cards_validator):
        """


        :rtype: Set[Card]
        :param lastcards:
        """
        validpattern = False
        while not validpattern:
            inp = input("What would you like to play on {}\n"
                        "Write 'pass' for pass\n"
                        "Your Cards: {}\n".format(lastcards or '{}', sorted(self.cards, key=lambda c: c.rank)))
            try:
                if inp == "pass" or inp == "p":
                    cards = []
                else:
                    cards = tcards(inp)

                validpattern = cards_validator(cards, self.cards)


            except:
                print(sys.exc_info())
                print("'{}' is invalid! Try again!")

        self.cards.difference_update(cards)

    def log(self, e: TEvent):
        print(e)

