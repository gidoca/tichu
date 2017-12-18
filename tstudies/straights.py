import random as r

from tlogic import Card
from tlogic.tichu import generate_deck
from tpatterns.straights import StraightRec


def street_any_hand(deck, ph=False):
    pr = StraightRec()
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
            oStraights = pr.recognize(oCards,ph)
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
        straights = StraightRec.__find_straight__(cards)
        print ("Straight?", straights)
        otherStraight = False
        if straights:
            found += 1
            for s in range(1,4):
                oCards = shuffle[s*14:(s+1)*14]
                oCards.sort(key=lambda x: x.height)
                oStraights = StraightRec.__find_straight__(oCards)
                otherStraight = otherStraight or oStraights
                print (s,oStraights)

            if otherStraight: oFound+=1

    print ("Probability of Straight:", found/float(k))
    print ("Probability of any other Straight:", oFound/float(found))


if __name__ == '__main__':
    deck = generate_deck()
    street_any_hand(deck)
    street_my_hand(deck)
