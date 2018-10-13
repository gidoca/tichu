from tpattern.multiples import PassOrEmpty
from tpattern.pattern import TPattern
from tpattern.tpatternrecognizer import TPatternRecognizer, TPatternRecResult
from tlogic.tcards import Card
from typing import Set, Collection


class TStraight(TPattern):

    def __init__(self, cards: Collection[Card]):
        if len(cards) < 5:
            raise ValueError

        self.numcards = len(cards)

        #Check consistency of given cards!

        sorted_cards = sorted(cards, lambda card: card.height)
        sorted_cards_iter = iter(sorted_cards)
        first_card = next(sorted_cards_iter)
        self.lowest = first_card.rank
        last_rank = self.lowest

        for following_card in sorted_cards_iter:
            last_rank += 1
            if last_rank != following_card.rank:
                raise ValueError("Inconsistent Straight")

        self.highest = last_rank

    def __gt__(self, other):
        if isinstance(other, TStraight):
            if other.numcards != self.numcards:
                # Questionable
                raise ValueError("Straight of different length!")
            else:
                return self.lowest > other.lowest # eq to self.highest > self.highest
        # Maybe this is too complicated
        elif isinstance(other, PassOrEmpty):
            return True
        else:
            raise ValueError("Different Patter - Not comparable")







class StraightRec(TPatternRecognizer) :

    @classmethod
    def recognize(self, cards: Set[Card], phoenix=True) -> bool:

        if (phoenix):
            return StraightRec.__find_straight_phoenix__(cards)
        else:
            return StraightRec.__find_straight__(cards)



    @staticmethod
    def __find_straight_phoenix__(cards):
        buffer = []
        out = []
        first = True
        phoenix = Card.has_phoenix( cards )
        phoenix_used = False
        phoenix_pos = -2
        i = 0
        while i< len(cards):
            card = cards[i]
            if first:
                first = False
                buffer.append(card)
            else:
                if (lastcard.height-card.height) ==-2 :
                    if phoenix is not None and not phoenix_used:
                        buffer.append(phoenix)
                        buffer.append(card)
                        phoenix_used = True
                        phoenix_pos = i-1
                    else:
                        if len(buffer) >= 5:
                            #print "straight!"
                            out.append(buffer)
                        #print buffer, "reset"
                        if phoenix_used: i=phoenix_pos
                        phoenix_used = False
                        buffer = [card,]

                elif (lastcard.height-card.height) ==-1 :
                    buffer.append(card)
                #print "appending", card
                elif (lastcard.height-card.height) ==0:
                    #                    print "pass"
                    pass
                else:
                    if len(buffer) >= 5:
                        #print "straight!"
                        # todo create new Straight object
                        out.append(buffer)
                    #print buffer, "reset"
                    if phoenix_used: i=phoenix_pos
                    phoenix_used = False
                    buffer = [card,]

            lastcard = card
            i += 1
        length = len(out)
        # without phoenix a
        return TPatternRecResult(length, length, out)


    @staticmethod
    def __find_straight__(cards):
        buffer = []
        out = []
        first = True
        for card in cards:
            if first:
                first = False
                buffer.append(card)
            else:
                #                print lastcard.height, card.height
                if (lastcard.height-card.height) ==-1 :
                    buffer.append(card)
                #print "appending", card
                elif (lastcard.height-card.height) ==0:
                    #                    print "pass"
                    pass
                else:
                    if len(buffer) >= 5:
                        #print "straight!"
                        out.append(buffer)
                    #print buffer, "reset"
                    buffer = [card,]
            lastcard = card
        return out
