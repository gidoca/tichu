from pychu.tlogic.tcard_names import generate_deck
from pychu.tpattern.doublestraight import DoubleStraightRec
from pychu.tstudies.study import existence


def straight_myhand(deck, ph=False):
    pr = DoubleStraightRec()
    return existence(pr.recognize, ph, "dstraight")

if __name__ == '__main__':
    deck = generate_deck()
    print(straight_myhand(deck))

