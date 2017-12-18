#!/bin/python
from enum import Enum
import random as r

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

deck = []
for color in Color:
    for i in range(2,15):
        print (i, color)
        deck.append ( Card( color=color, height=i) )
deck.append( Card(special=Special.dragon, height=17) )
deck.append( Card(special=Special.phoenix, height=17) )
deck.append( Card(special=Special.mahjong, height=1) )
deck.append( Card(special=Special.dog, height=-2) )

for i, card in enumerate(deck):
    print (i,card)
#print card.height, card.color

def street_any_hand(deck, ph=False):
    if ph: findFunction = Card.find_straight_phoenix
    else: findFunction = Card.find_straight
    k=10000
    found = 0; found2 = 0; found3 = 0; found4 = 0
    for i in range(k):
        anyStraight = False
        shuffle = r.sample(deck, 56)
        numFound = 0
        for s in range(0,4):
            oCards = shuffle[s*14:(s+1)*14]
            oCards.sort(key=lambda x: x.height)
            print (oCards,"->",)
            oStraights = findFunction(oCards)
            if oStraights: numFound+=1
            print (s,oStraights)

        if numFound>=1: found+=1
        if numFound>=2: found2+=1
        if numFound>=3: found3+=1
        if numFound>=4: found4+=1

    if ph: print ("-----\nWith Phoenix\n----")
    print ("Probability of Straight any Hand:", found/float(k))
    print ("Probability of Straight in two Hands:", found2/float(k))
    print ("Probability of Straight in three Hands:", found3/float(k))
    print ("Probability of Straight in four Hands:", found4/float(k))
    print ("Probability of Straight in three Hands if two:", found3/float(found2))
    print ("Probability of Straight in three Hands if one:", found3/float(found))
    print ("Probability of Straight in two Hands if one:", found2/float(found))
    print ("Probability of Straight in four Hands if three:", found4/float(found3))


def street_my_hand(deck):
    k=10000
    found = 0; oFound=0
    for i in range(k):
        shuffle = r.sample(deck, 56)
        cards = shuffle[:14]
        cards.sort(key=lambda x: x.height)
        straights = Card.find_straight(cards)
        print ("Straight?", straights)
        otherStraight = False
        if straights: 
            found += 1
            for s in range(1,4):
                oCards = shuffle[s*14:(s+1)*14]
                oCards.sort(key=lambda x: x.height)
                oStraights = Card.find_straight(oCards)
                otherStraight = otherStraight or oStraights
                print (s,oStraights)

            if otherStraight: oFound+=1

    print ("Probability of Straight:", found/float(k))
    print ("Probability of any other Straight:", oFound/float(found))

    
def find_bombs(cards):
    buffer = []
    out = []
    first = True
    for card in cards:
        if first:
            first = False
            buffer.append(card)
        else:
            if lastCard.height-card.height == 0:
                buffer.append(card)
            else:
                if len(buffer) == 4:
                    out.append(buffer)
                buffer = [card,]
        lastCard = card
    return out


def bomb(deck):
    k=10000
    handbombs = 0;anybombs = 0; 
    for i in range(k):
        shuffle = r.sample(deck, 56)
        first = True
        bAnybombs = False
        for s in range(4):
            cards = shuffle[s*14:(s+1)*14]
            cards.sort(key=lambda x: x.height)
            bombs = find_bombs(cards)
            if bombs: print (bombs)
            bAnybombs = bAnybombs or bombs
            if first: 
                first=False
                if bombs: handbombs+=1
        if bAnybombs: anybombs+=1


    print ("Handbombe:", handbombs/float(k))
    print ("AnyBombs:", anybombs/float(k))


street_my_hand(deck)
street_any_hand(deck)
street_any_hand(deck, ph=True)
#bomb(deck)
