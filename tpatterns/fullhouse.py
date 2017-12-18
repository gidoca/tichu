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

    @staticmethod
    def __find_fullhouse__(cards: Set[Card]):
        num_pairs = FullhouseRec.pairRec.recognize(cards)
        num_triples = FullhouseRec.tripleRec.recognize(cards)
        return min(num_pairs, num_triples);


if __name__ == '__main__':

    cards1 = list(map(Card.from_string, ['r4', 'g4', 'b4', 'r2', 'g2', 'k2']))
    cards2 = list(map(Card.from_string, ['r4', 'g4', 'b4', 'r2', 'g2' ]))

    fhr = FullhouseRec()
    print(fhr.recognize(cards1))
    print(fhr.recognize(cards2))
