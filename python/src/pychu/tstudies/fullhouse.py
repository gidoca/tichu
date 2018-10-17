import random as r
# TODO: this could be merged with all the other functions based on the same iteration over the cards
from pychu.tlogic.tcard_names import generate_deck
from pychu.tpattern.fullhouse import FullhouseRec


def full_house_myhand(deck, ph=False):
    pr = FullhouseRec
    k=10000
    found = 0; found2Hands = 0; found3Hands = 0; found4hands = 0
    for i in range(k):
        anyStraight = False
        shuffle = r.sample(deck, 56)
        numFound = 0
        for s in range(0,4):
            oCards = shuffle[s*14:(s+1)*14]
            oCards.sort(key=lambda x: x.height)
            # out += str.format (oCards,"->",)
            oStraights = pr.recognize(oCards,ph)
            if oStraights: numFound+=1
            # out += str.format (s,oStraights)

        if numFound>=1: found+=1
        if numFound>=2: found2Hands+=1
        if numFound>=3: found3Hands+=1
        if numFound>=4: found4hands+=1

    out = "";

    # also the counting should be reusable
    if ph: out += ("-----\nWith Phoenix\n----")
    out += str.format ("Probability of Fullhouse any Hand: {}\n", found/float(k))
    out += str.format ("Probability of Fullhouse in two Hands: {}\n", found2Hands/float(k))
    out += str.format ("Probability of Fullhouse in three Hands: {}\n", found3Hands/float(k))
    out += str.format ("Probability of Fullhouse in four Hands: {}\n", found4hands/float(k))
    out += str.format ("Probability of Fullhouse in three Hands if two: {}\n", found3Hands/float(found2Hands))
    out += str.format ("Probability of Fullhouse in three Hands if one: {}\n", found3Hands/float(found))
    out += str.format ("Probability of Fullhouse in two Hands if one: {}\n", found2Hands/float(found))
    out += str.format ("Probability of Fullhouse in four Hands if three: {}\n", found4hands/float(found3Hands))
    return out

if __name__ == '__main__':

    deck=generate_deck()
    out = full_house_myhand(deck)
    print(out)
