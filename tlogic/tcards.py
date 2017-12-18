from enum import Enum


class Color(Enum):
    red = 1
    blue = 2
    green = 3
    black = 4
    def __str__(self):
        return self.name[0]


class Special(Enum):
    mahjong = 1
    dog = 2
    dragon = 3
    phoenix = 4
    def __str__(self):
        return self.name[0:2]


class Card:
    # TODO special and None color is the same property
    def __init__(self, color=None, height=-1, special=None):
        self.special = special
        self.height = height
        self.color = color

    def __repr__(self):
        if self.special is not None:
            return str(self.special)
        else:
            return str(self.color)+str(self.height)


    # TODO move to helper class
    @staticmethod
    def has_phoenix( cards ):
        for card in cards:
            if card.special == Special.phoenix:
                return card
        return None

    @staticmethod
    def find_straight_phoenix( cards ):
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
    def find_straight( cards ):
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