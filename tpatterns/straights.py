from tpatterns.tpatternrecognizer import TPatternRecognizer
from tlogic.tcards import Card
from typing import Set


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
        phoenixUsed = False
        phoenixPos = -2
        i = 0
        while i< len(cards):
            card = cards[i]
            if first:
                first = False
                buffer.append(card)
            else:
                if (lastcard.height-card.height) ==-2 :
                    if phoenix is not None and not phoenixUsed:
                        buffer.append(phoenix)
                        buffer.append(card)
                        phoenixUsed = True
                        phoenixPos = i-1
                    else:
                        if len(buffer) >= 5:
                            #print "straight!"
                            out.append(buffer)
                        #print buffer, "reset"
                        if phoenixUsed: i=phoenixPos
                        phoenixUsed = False
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
                        out.append(buffer)
                    #print buffer, "reset"
                    if phoenixUsed: i=phoenixPos
                    phoenixUsed = False
                    buffer = [card,]

            lastcard = card
            i += 1
        return out


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
