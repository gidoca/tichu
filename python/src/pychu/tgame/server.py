import copy
import random as r
import time
from dataclasses import dataclass
from enum import Enum, auto
from typing import Set, List, Dict

from pychu.tgame.validator import CardsValidator
from pychu.tlogic.tcards import Card
from pychu.tlogic.tcard_names import dog, generate_deck, mahjong
from pychu.tplayer.tplayer import TPlayer


class TEventList(Enum):
    SmallTichu = auto(), 'announces a tiny tichu'
    BigTichu = auto(), 'announces a fat tichu'
    Play = auto(), 'plays'
    Pass = auto(), 'passes'
    Take = auto(), 'takes'
    Wish = auto(), 'wishes'

    # ok, one thing that is nicer in java
    # but at least we can tweak it
    def __new__(cls, keycode, third_person):
        enum = object.__new__(cls)
        enum._value_ = keycode
        enum.third_person = third_person
        return enum


@dataclass
class TEvent():
    event: TEventList
    player: int
    data: any = None
    message: str = None

    def __repr__(self):
        if self.data:
            return "P{} {} {}".format(self.player, self.event.third_person, self.data)
        else:
            return "P{} {}".format(self.player, self.event.third_person)


class TPlayerProxy:
    """
    Meta Player Representation on the server side:
    -> Keeps track of cards played
    -> Tichu announced
    -> Wishes
    -> Communicates with the connected player
    -> Verifies the validity of the movement
    """

    # keep it flat or not?

    def __init__(self, n: int, cards: Set[Card]):
        self.n = n
        self.hand = set(cards)
        self.stash = set()
        self.extplayer: TPlayer

    def finished(self):
        return not self.hand

    def remove_from_hand(self, cards):
        if self.hand.issuperset(cards):
            self.hand.difference_update(cards)
        else:
            raise ValueError("This Card is not in your hand anymore!")

    def takes(self, cards):
        self.stash.update(cards)

    def hasMajong(self):
        return mahjong in self.hand

    def play(self, last_cards) -> TEvent:
        # cards = [] if not table_buffer else table_buffer[-1]
        validator = CardsValidator(last_cards, self.hand)

        for penalty in range(3):
            self.extplayer.play(last_cards, validator.verify)

            if validator.played_cards is not None:
                if len(validator.played_cards) == 0:
                    return TEvent(TEventList.Pass, self.n)
                else:
                    cards = validator.played_cards
                    try:
                        self.remove_from_hand(cards)
                        return TEvent(TEventList.Play, self.n, cards)
                    except ValueError as e:
                        print(e)

            else:
                print("Player {} did wrong!".format(self.n))

        print("Player {} had its chance -> Forced passing!".format(self.n))
        return TEvent(TEventList.Pass, None)

    def register(self, player: TPlayer):
        self.extplayer = player
        player.init(copy.copy(self.hand), self.n)


class TRound:
    """
    TRound keeps track of all the cards during a complete Round.
    It distributes the cards at the beginning
    checks if cards are valid (e.g. cheating over remote client)
    """

    # Todo: TRound should only know ProxyPlayer
    def __init__(self, extplayers: List[TPlayer]):
        if len(extplayers) != 4:
            raise ValueError("4 Players expected!")
        self.players: List[TPlayer] = []
        self.card_log: List[Dict[int, Set[Card]]] = []
        self.extplayers = extplayers
        deck = generate_deck()
        shuffled_deck = r.sample(deck, 56)
        self.players: List[TPlayerProxy] = []

        for s in range(4):
            oCards = shuffled_deck[s * 14:(s + 1) * 14]
            self.players.append(TPlayerProxy(s, oCards))

        for i, player in enumerate(extplayers):
            self.players[i].register(player)

    def start(self):
        player_number = self.start_player()

        while self.active_players > 1:  # nplayers > 1
            player_number, cards = self.turn(player_number, 0)
            self.logEventParams(player_number, TEventList.Take, data=cards)
            self.card_log += cards

        print(self.show_cards())

        return

    def logEventParams(self, current_pl_number: int, event, data=None, message=None):
        ev = TEvent(event, current_pl_number, data, message)
        self.logEvent(ev)

    def logEvent(self, ev: TEvent):
        from pychu.tplayer.humanplayer import HumanPlayer
        if not any(isinstance(pl, HumanPlayer) for pl in self.players):
            print(ev)
        # for player in self.players:
        # player.log(ev)

    @property
    def active_players(self):
        pls = [not p.finished() for p in self.players]
        return sum(pls)

    def start_player(self):
        for i, player in enumerate(self.players):
            if player.hasMajong():
                return i
        raise Exception("No majong available anymore")

    def finished(self, pid):
        return self.players[pid].finished()

    def show_cards(self):
        out = ''
        for p in self.players:
            out += "Hand: {} | Stash: {}\n".format(p.hand, p.stash)

        return out


    def turn(self, pid: int, delay=0.3) -> (int, any):
        trick_owner = -1
        table_buffer = []
        last_cards = []
        while pid != trick_owner:
            # todo: move to the end
            if self.finished(pid):
                pid = (pid + 1) % 4
                continue

            time.sleep(delay)

            player: TPlayerProxy = self.players[pid]
            # this move is checked by the proxy player
            ev = player.play(last_cards)
            # therefore we trust if it was played the new player is owner of the trick
            if (ev.event == TEventList.Play):
                last_cards = ev.data
                trick_owner = pid
                table_buffer += (last_cards)

                if {dog}.issuperset(last_cards):
                    pid = trick_owner = (pid + 2) % 4  # partner
                    break;
            self.logEvent(ev)

            pid = (pid + 1) % 4

        player.takes(table_buffer)
        return trick_owner, table_buffer
