import random as r
def full_house_myhand(deck, ph=False):
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

if __name__ == '__main__':
    from tlogic import generate_deck, Card

    deck=generate_deck();
    full_house_myhand(deck)
