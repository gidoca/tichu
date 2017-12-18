from tpatterns.multiples import MultiRec
from tpatterns.tpatternrecognizer import TPatternRecognizer
from tlogic.tcards import Card
from typing import Set


class FullhouseRec(TPatternRecognizer) :
    pairRec = MultiRec(2, True)
    tripleRec = MultiRec(3, True)

    @classmethod
    def recognize(self, cards: Set[Card], phoenix=True) -> bool:

        if (phoenix):
            return FullhouseRec.__find_fullhouse_phoenix__(cards)
        else:
            return FullhouseRec.__find_fullhouse__(cards)



    @staticmethod
    def __find_fullhouse_phoenix__(cards: Set[Card]) -> bool:
        if (Card.has_phoenix(cards)):
            #special
            pass
        else:
            return FullhouseRec.__find_fullhouse__(cards);

    # Max. number of full houses with 14 cards is 2 anyways...
    # but this should be a general solution
    @staticmethod
    def __find_fullhouse__(cards: Set[Card]):
        num_pairs = FullhouseRec.pairRec.recognize(cards)
        num_triples = FullhouseRec.tripleRec.recognize(cards)

        if (num_triples>0):
            diff = num_pairs-num_triples;
            if (diff) >= 0:
                return min(num_pairs, num_triples);
            else:
                matching = num_pairs
                print('matching', matching)
                additional = (num_triples-num_pairs)//2;
                print('additional', additional)
                return matching+additional;









if __name__ == '__main__':

    cards1 = list(map(Card.from_string, ['r4', 'g4', 'b4', 'r2', 'g2', 'k2']))
    cards2 = list(map(Card.from_string, ['r4', 'g4', 'b4', 'r2', 'g2' ]))
    cards3 = list(map(Card.from_string, ['r4', 'g4', 'b4', 'r2', 'g2', 'k2', 'r3', 'k3', 'r5', 'g5', 'k5']))

    fhr = FullhouseRec()
    print(fhr.recognize(cards1))
    print(fhr.recognize(cards2))
    print(fhr.recognize(cards3))
