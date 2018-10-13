from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import Set, Callable

from tgame.server import TEvent
from tlogic.tcards import Card


class TICHU(Enum):
    BIG = auto
    SMALL = auto



class TPlayer(ABC):
#Longterm: player should get the complete game
# in order to figure out which cards are already gone
# however, for having a first interaction, the player only
# sees the cards played by now
    """
    Players are numbered from 0 to 3
    player 0 is playing with player 2
    1 is together with 3
    the round is 0->1->2->3->0->1... and so on.
    It apparently does not need to start with player zero
    due to the ruleset of tichu.

    """
    def __init__(self):
        self.cards = set()
        self.player_number = 0

    def init(self, cards: Set[Card], player_number: int ):
        self.cards = set(cards)
        self.player_number = player_number

    @abstractmethod
    def play(self, lastcards: Set[Card], card_receiver: Callable[[Set[Card], bool], bool], wish=None) -> Set[Card]:
        """
        The only mandatory function to implement.
        The Player is given the cards played by the last player
        that did not pass (obviously) or an empty set
        if

        :param card_receiver: function handle that tells the player if what it played is valid.
        this function can also be used to only validate the set but calling card_receiver(cards, test=True)
        :param lastcards:
        :param wish:
        :return: Set[Card]
        """
        pass;

    def make_wish(self) -> int:
        """
        After the server detects the majong being played,
        the Player is asked to state a wish (2-14)
        Be aware: Also a very stupid wish is valid :)
        :return:
        """


    def log(self, event : TEvent):

        """
        This enables a player to follow the course of the game.
        :param message:
        :param cards:
        :param player:
        :return:
        """
        pass;

