from pychu.tlogic.tcard_names import generate_deck
from pychu.tpattern.tdoublestraight import TDoubleStraightFinder
from pychu.tstudies.study import existence


def straight_myhand(deck, ph=False):
    pr = TDoubleStraightFinder()
    return existence(pr.recognize, ph, "dstraight")

if __name__ == '__main__':
    deck = generate_deck()
    print(straight_myhand(deck))

