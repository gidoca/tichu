from typing import Set, Collection

from pychu.tlogic.tcards import Card, Special, has_phoenix
from pychu.tpattern.multiples import PassOrEmpty
from pychu.tpattern.pattern import TPattern
from pychu.tpattern.tpatternrecognizer import TPatternRecognizer, TPatternRecResult


class TStraight(TPattern):

    def __init__(self, cards: Collection[Card]):
        self.cards = cards
        le = len(cards)
        if le < 5:
            raise ValueError('At least five cards are needed for a '
                             'straight. Only {} were given'.format(le))

        self.numcards = len(cards)

        # Check consistency of given cards!

        sorted_cards = sorted(cards, key=lambda card: card.rank)
        sorted_cards_iter = iter(sorted_cards)
        first_card = next(sorted_cards_iter)
        self.lowest = first_card.rank
        phx = has_phoenix(sorted_cards)

        redundant_ranks = []
        self.phx_rank = None

        last_rank = self.lowest
        for current_card in sorted_cards_iter:
            if current_card.special == Special.phoenix:
                continue
            diff = current_card.rank - last_rank
            if diff == 0:
                redundant_ranks.append(current_card.rank)
            elif diff == 1:
                last_rank = current_card.rank
            elif diff == 2 and phx:
                phx = False
                last_rank = current_card.rank
            else:
                raise ValueError("Inconsistent Straight")

        # if phx was not used to build the straight
        # it can make the straight longer
        if phx:
            # append phx to the end (if not already ace)
            if last_rank < 14:
                last_rank += 1
                self.phx_rank = last_rank
            elif self.lowest > 2:
                self.lowest -= 1
                self.phx_rank = self.lowest

        self.highest = last_rank

    def find(self, cards, higher=True, exact=True):
        pass

    # general question: raise error or just return false?
    def __gt__(self, other):
        if isinstance(other, TStraight):
            if other.numcards > self.numcards:
                return False
            else:
                return self.highest > other.highest
        # Maybe this is too complicated
        elif isinstance(other, PassOrEmpty):
            return True
        else:
            return False
            # todo
            # raise ValueError("Different Patter - Not comparable")


class StraightRec(TPatternRecognizer):

    @classmethod
    def recognize(self, cards: Set[Card], phoenix=True) -> bool:

        if (phoenix):
            return StraightRec.__find_straight_phoenix__(cards)
        else:
            return StraightRec._find_straight_(cards)

    @staticmethod
    def __find_straight_phoenix__(cards):
        buffer = []
        out = []
        first = True
        phoenix = has_phoenix(cards)
        phoenix_used = False
        phoenix_pos = -2
        i = 0
        while i < len(cards):
            card = cards[i]
            if first:
                first = False
                buffer.append(card)
            else:
                if (lastcard.rank - card.rank) == -2:
                    if phoenix is not None and not phoenix_used:
                        buffer.append(phoenix)
                        buffer.append(card)
                        phoenix_used = True
                        phoenix_pos = i - 1
                    else:
                        if len(buffer) >= 5:
                            # print "straight!"
                            out.append(buffer)
                        # print buffer, "reset"
                        if phoenix_used: i = phoenix_pos
                        phoenix_used = False
                        buffer = [card, ]

                elif (lastcard.rank - card.rank) == -1:
                    buffer.append(card)
                # print "appending", card
                elif (lastcard.rank - card.rank) == 0:
                    #                    print "pass"
                    pass
                else:
                    if len(buffer) >= 5:
                        # print "straight!"
                        # todo create new Straight object
                        out.append(buffer)
                    # print buffer, "reset"
                    if phoenix_used: i = phoenix_pos
                    phoenix_used = False
                    buffer = [card, ]

            lastcard = card
            i += 1
        length = len(out)
        # without phoenix a
        return TPatternRecResult(length, length, out)

    @staticmethod
    def _find_straight_(cards):
        buffer = []
        out = []
        first = True
        for card in cards:
            if first:
                first = False
                buffer.append(card)
            else:
                #                print lastcard.rank, card.rank
                if (lastcard.rank - card.rank) == -1:
                    buffer.append(card)
                # print "appending", card
                elif (lastcard.rank - card.rank) == 0:
                    #                    print "pass"
                    pass
                else:
                    if len(buffer) >= 5:
                        # print "straight!"
                        out.append(buffer)
                    # print buffer, "reset"
                    buffer = [card, ]
            lastcard = card
        return out
