import copy
import random as r
import time
from dataclasses import dataclass
from enum import Enum, auto
from typing import Set, List, Dict, overload

from pychu.tlogic.tcards import Card, mahjong, dog
from pychu.tlogic.thelpers import generate_deck, rec_pattern_unique
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
            self.extplayer.play(last_cards, validator.card_receiver )

            if validator.valid_move:
                if len(validator.played_cards_valid) == 0:
                    return TEvent(TEventList.Pass, self.n)
                else:
                    cards = validator.played_cards_valid
                    self.remove_from_hand(cards)
                    return TEvent(TEventList.Play, self.n, cards)

            else:
                print("Player {} did wrong!".format(self.n))

        print("Player {} had its chance -> Forced passing!".format(self.n))
        return TEvent( TEventList.Pass, None)

    def register(self, player: TPlayer):
        self.extplayer = player
        player.init(copy.copy(self.hand), self.n)



class TRound:
    class TCardTable:
        """
        TRound keeps track of all the cards during a complete Round.
        It distributes the cards at the beginning
        checks if cards are valid (e.g. cheating over remote client)
        """
    players: List[TPlayer] = []

    card_log: List[Dict[int,Set[Card]]] = []

    ct: TCardTable = TCardTable()

    def __init__(self, extplayers: List[TPlayer]):
        if len(extplayers) != 4:
            raise ValueError("4 Players expected!")
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
        while  pid != trick_owner:
            # todo: move to ct
            if self.finished(pid):
                pid = (pid+1)%4
                continue

            time.sleep(delay)

            player : TPlayerProxy= self.players[pid]
            # this move is checked by the proxy player
            ev = player.play(last_cards)
            # therefore we trust if it was played the new player is owner of the trick
            if(ev.event == TEventList.Play):
                last_cards = ev.data
                trick_owner = pid
                table_buffer += (last_cards)

                if {dog}.issuperset(last_cards):
                    pid = trick_owner = (pid+2)%4 # partner
                    break;
            self.logEvent(ev)

            pid = (pid + 1) % 4

        player.takes(table_buffer)
        return trick_owner, table_buffer


class CardsValidator:
    table_cards = []
    played_cards_valid = []
    valid_move = False

    def __init__(self, table_cards: List[Card], avail_cards):
        self.table_cards = table_cards
        self.available_cards = avail_cards

    def card_receiver(self, played_cards, ):
        valid = self.check(played_cards, wish=None)
        if valid:
            self.played_cards_valid = played_cards
            self.valid_move = True
        return valid

    def check(self, played_cards, wish=None, avail_cards=None):
        table_pattern = rec_pattern_unique(self.table_cards)
        played_pattern = rec_pattern_unique(played_cards)
        return played_pattern > table_pattern