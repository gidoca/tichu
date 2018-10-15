from tpattern.tpatternrecognizer import TPatternRecognizer
from tlogic import Card
from collections import Counter

from typing import Set


class DoubleStraightRec(TPatternRecognizer):

    @classmethod
    def recognize(self, cards: Set[Card], phoenix=False):

        # sort carts by height


        # sorted_cards = sorted(cards, lambda card: card.height)

        # put them in a dictionary by height

        by_height = Counter(map(lambda c: c.height, cards))
        by_height_minpair = [k for k, v in by_height.items() if v >= 2]



        # num_cards = len(sorted_cards)

        lengths = []
        i , j= 0,0
        maxidx = len(by_height_minpair)



        while (i < maxidx - 1):
            j = 0;
            while (i + j < maxidx-1):
                last_val = by_height_minpair[i + j]
                next_val = by_height_minpair[i + j + 1]
                # this only works if we don't want to know
                # details like the lenght or if there
                # is another double straight
                if (next_val - last_val) > 1:
                    break;
                else:
                    j += 1;

            if j>0:
                lengths.append(j+1);

            i += j + 1
        return lengths




        # while (j < maxidx):
        #    j+=1
        #    next_val = by_height_minpair.get(j)
        #    if (next_val-last_val) > 1:
        #        return 0


if __name__ == '__main__':
    cards1 = map(tcard, 'r2 g2 r3 k3 k5 k9'.split(' '))
    cards2 = map(tcard, 'r2 g2 r3 k3 k5 k9 r4 g4'.split(' '))
    cards3 = map(tcard, 'r2 g3 r3 k3 k5 k9'.split(' '))
    cards4 = map(tcard, 'r2 g2 r3 k3 k5 k9 r4 g4 r5 r10 g10 k11 g11'.split(' '))
    pr = DoubleStraightRec()

    print(pr.recognize(cards1))
    print(pr.recognize(cards2))
    print(pr.recognize(cards3))
    print(pr.recognize(cards4))
