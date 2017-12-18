from tlogic import Card
from tlogic.tichu import generate_deck
from tpatterns.tpatternrecognizer import TPatternRecognizer


from typing import Set
from collections import Counter



class MultiRec(TPatternRecognizer):
    def __init__(self, m: int, ex = False):
        self.m = m;
        self.exact = ex;

    def recognize(self, cards: Set[Card], phoenix=False) -> int:
        newlist = list(map(lambda card: card.height, cards))

        if(self.exact):
            matcher= lambda v: v == self.m
        else:
            matcher = lambda v: v >= self.m


        pairslist = {k: v for k, v in Counter(newlist).items() if matcher(v)}

        return len(pairslist);






        # print(Counter(newlist))







if __name__ == '__main__':
    deck = generate_deck()

    pr = PairsRec()
    pr.recognize(deck)








