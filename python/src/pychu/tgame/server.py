import random as r
from dataclasses import dataclass
from enum import Enum, auto
from typing import Set, List

from pychu.tlogic.tcards import Card, tcard, mahjong
from pychu.tlogic.thelpers import generate_deck


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


class TServerPlayer:
    # keep it flat or not?

    def __init__(self, n: int, cards: Set[Card]):
        self.n = n
        self.hand = set(cards)
        self.stash = set()

    def finished(self):
        return not self.hand

    def plays(self, cards):
        if self.hand.issuperset(cards):
            self.hand.difference_update(cards)
        else:
            raise ValueError("This Card is not in your hand anymore!")

    def takes(self, cards):
        self.stash.update(cards)

    def hasMajong(self):
        return mahjong in self.hand



class TCardTable:
    """
    TCardTable keeps track of all the cards during a complete Round.
    It distributes the cards at the beginning
    checks if cards are valid (e.g. cheating over remote client)
    Gives info who's is next

    """

    def __init__(self):
        deck = generate_deck()
        shuffled_deck = r.sample(deck, 56)
        self.players: List[TServerPlayer] = []
        self.table_buffer = []

        for s in range(4):
            oCards = shuffled_deck[s * 14:(s + 1) * 14]
            self.players.append(TServerPlayer(s, oCards))

    @property
    def active_players(self):
        pls = [not p.finished() for p in self.players]
        return sum(pls)

    def plays(self, pid: int, cards: Set[Card]):
        player = self.players[pid]
        player.plays(cards)
        self.table_buffer += cards

    def takes(self, pid: int):
        player = self.players[pid]
        player.takes(self.table_buffer)
        self.table_buffer.clear()

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
