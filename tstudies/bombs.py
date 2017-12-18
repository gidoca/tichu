import random as r


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