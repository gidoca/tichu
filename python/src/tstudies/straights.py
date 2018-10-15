import random as r

from tlogic.thelpers import generate_deck
from tpattern.straights import StraightRec


# TODO: refactor into testfunctions?
from tstudies.study import existence


def street_any_hand(deck, ph=False):
    pr = StraightRec()

    return existence(deck, pr.recognize, "Straight", ph)


# TODO: make a general study
def street_my_hand(deck):
    # r.seed()
    k=10000
    found = 0; ifFound=0; allFound=0;
    for i in range(k):
        shuffled_deck = r.sample(deck, 56)
        myCards = shuffled_deck[:14]
        myCards.sort(key=lambda x: x.height)
        isMyStraight = StraightRec._find_straight_(myCards)
        # print ("Straight?", straights)
        otherStraight = False
        for s in range(1,4):
            oCards = shuffled_deck[s*14:(s+1)*14]
            oCards.sort(key=lambda x: x.height)
            oStraights = StraightRec._find_straight_(oCards)
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
