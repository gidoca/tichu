import random as r
from typing import Callable, Set

from pychu.tlogic.tcards import Card
# TODO: refactor into testfunctions?
from pychu.tlogic.tcard_names import generate_deck
from pychu.tpattern.straights import TStraightFinder
from pychu.tstudies.straights import street_any_hand


def existence(deck: Set[Card], recognize_f: Callable[[Set[Card], bool], bool],name: str, ph=False, ):
    k=10000
    found = 0; found2 = 0; found3 = 0; found4 = 0
    for i in range(k):
        anyStraight = False
        shuffle = r.sample(deck, 56)
        numFound = 0
        for s in range(0,4):
            oCards = shuffle[s*14:(s+1)*14]
            oCards.sort(key=lambda x: x.height)
            # print (oCards,"->",)
            oStraights = recognize_f(oCards,ph)
            if oStraights: numFound+=1
            # print (s,oStraights)

        if numFound>=1: found+=1
        if numFound>=2: found2+=1
        if numFound>=3: found3+=1
        if numFound>=4: found4+=1

    out = "Straight in any hand"
    if ph: out += str.format("-----\nWith Phoenix\n----")
    out += str.format("Probability of {} any Hand: {}\n",name, found/float(k))
    out += str.format("Probability of {} in two Hands: {}\n",name, found2/float(k))
    out += str.format("Probability of {} in three Hands: {}\n",name, found3/float(k))
    out += str.format("Probability of {} in four Hands: {}\n",name, found4/float(k))
    out += str.format("Probability of {} in three Hands if two: {}\n",name, found3/float(found2))
    out += str.format("Probability of {} in three Hands if one: {}\n",name, found3/float(found))
    out += str.format("Probability of {} in two Hands if one: {}\n",name, found2/float(found))
    out += str.format("Probability of {} in four Hands if three: {}\n",name, found4/float(found3))

    return out


def street_my_hand(deck):
    k=10000
    found = 0; ifFound=0; allFound=0;
    for i in range(k):
        shuffle = r.sample(deck, 56)
        myCards = shuffle[:14]
        myCards.sort(key=lambda x: x.height)
        isMyStraight = TStraightFinder._find_straight_(myCards)
        # print ("Straight?", straights)
        otherStraight = False
        for s in range(1,4):
            oCards = shuffle[s*14:(s+1)*14]
            oCards.sort(key=lambda x: x.height)
            oStraights = TStraightFinder._find_straight_(oCards)
            otherStraight = otherStraight or oStraights
            # print (s,oStraights)

        if isMyStraight:
            found += 1
        if otherStraight:
             allFound+=1
             if isMyStraight:
                ifFound+=1

    out = str.format("Straights in ma Haand, k={}\n", k)
    out+= str.format("Probability of Straight: {} {}\n", found/float(k), found)
    out+= str.format("Probability of any other Straight if I had one: {} {}\n", ifFound/float(found), ifFound)
    out+= str.format("Probability of any other Straight (1 of 3 players): {} {}\n", allFound/float(k), allFound)
    return out


if __name__ == '__main__':
    deck = generate_deck()
    print(street_any_hand(deck))
    print(street_my_hand(deck))
