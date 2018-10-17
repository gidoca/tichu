import random as r


# TODO: this is logic
# -> replace by multiples rec.
from pychu.tlogic.tcard_names import generate_deck
from pychu.tpattern.bombs import find_bombs


def bomb(deck):
    k=10000
    handbombs = 0;anybombs = 0;
    for i in range(k):
        shuffled_deck = r.sample(deck, 56)
        bAnybombs = False
        for s in range(4):
            cards = shuffled_deck[s*14:(s+1)*14]
            cards.sort(key=lambda x: x.height)
            bombs = find_bombs(cards)
            # if bombs: print (bombs)
            bAnybombs = bAnybombs or bombs
            # This might be wrong
            if s == 0:
                if bombs: handbombs+=1
        if bAnybombs: anybombs+=1


    out = ""
    out += str.format("Handbombe: {}\n", handbombs/float(k))
    out += str.format("AnyBombs: {}\n", anybombs/float(k))
    return out


if __name__ == '__main__':
    deck = generate_deck()
    out = bomb(deck)
    print(out)
