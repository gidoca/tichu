#!/usr/bin/python3

# TODO: this will have a parameter for number of AI and human players
# now defaulting to 3 AI and one human player

# there needs also to be a mechanism for outputing user messages
import sys
import time
from enum import Enum
from typing import List, Set, Dict

print (sys.path)

import tlogic
# noinspection PyUnresolvedReferences
from tplayer.humanplayer import HumanPlayer
from pychu.tplayer.server import TCardTable, TEventList, TEvent
# noinspection PyUnresolvedReferences
from tplayer.stupidai import StupidAI
# noinspection PyUnresolvedReferences
from tplayer.tplayer import TPlayer
from pychu.tlogic.tcards import Card, dog


class State(Enum):
    PreSchupfing = 0
    Schupfing = 1
    PrePlaying = 2


class CardsValidator:
    table_cards = []
    played_cards_valid = []
    valid_move = False

    def __init__(self, table_cards: List[Card]):
        self.table_cards = table_cards

    def card_receiver(self, played_cards, avail_cards):
        valid = self.check(played_cards, wish=None, avail_cards=avail_cards)
        if valid:
            self.played_cards_valid = played_cards
            self.valid_move = True
        return valid

    def check(self, played_cards, wish=None, avail_cards=None):
        table_pattern = tlogic.thelpers.rec_pattern_unique(self.table_cards)
        played_pattern = tlogic.thelpers.rec_pattern_unique(played_cards)
        return played_pattern > table_pattern


class TRound:
    players: List[TPlayer] = []

    card_log: List[Dict[int,Set[Card]]] = []

    ct: TCardTable = TCardTable()

    def __init__(self, players: List[TPlayer]):
        if len(players) != 4:
            raise ValueError("4 Players expected!")
        self.players = players
        for i, player in enumerate(players):
            cards = self.ct.players[i].hand
            player.init(cards, i)

    def start(self):
        player_number = self.ct.start_player()

        while self.ct.active_players > 1:  # nplayers > 1
            player_number, cards = self.gameLoop(player_number)
            self.logEvent(player_number, TEventList.Take, cards, None)
            self.card_log += cards

    # todo: datastrcuture for logging movements
    # logging stash cards
    # todo: table (or list) for finished
    def gameLoop(self, player_number: int) -> int:
        penalty = 0;
        pid = player_number
        card_owner = -1
        top_cards: Set[Card] = set()
        collected_cards: Dict[Set[Card]] = []
        while  pid != card_owner:  # what if a player has finished?
            time.sleep(0.3)

            # ToDO: Subround Object
            current_pl = self.players[pid]
            validator = CardsValidator(top_cards)
            current_pl.play(top_cards, validator.card_receiver)
            # ToDo: better Protocol -> more logic in validator
            if validator.valid_move:
                if len(validator.played_cards_valid) == 0:
                    self.logEvent(pid, TEventList.Pass, None)
                else:
                    top_cards = validator.played_cards_valid
                    collected_cards += top_cards
                    self.ct.plays(pid, top_cards)
                    self.logEvent(pid, TEventList.Play, top_cards)
                    card_owner = pid
                    if {dog}.issuperset(top_cards):
                        card_owner = (pid+2)%4 # partner
                        pid += 1

                pid = (pid + 1) % 4

            else:
                print("Player {} did wrong!".format(pid))
                penalty += 1
                if penalty == 3:
                    print("Player {} had its chance -> Forced passing!".format(pid))
                    self.logEvent(pid, TEventList.Pass, None)
                    pid = (pid + 1) % 4

        return card_owner, collected_cards

    def logEvent(self, current_pl_number, event, data=None, message=None):
        ev = TEvent(event, current_pl_number, data, message)
        if not any(isinstance(pl, HumanPlayer) for pl in self.players):
            print(ev)
        for player in self.players:
            player.log(ev)


def terminal():
    print('Welcome to Pichu'
          'Listen and repeat...')

    players = [StupidAI(), StupidAI(), StupidAI(), StupidAI()]

    tround = TRound(players)
    tround.start()


if __name__ == '__main__':
    terminal()
