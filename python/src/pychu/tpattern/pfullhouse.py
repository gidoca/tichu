from pychu.tpattern.tpattern import TPattern


class PFullHouse(TPattern):
    """
    There is only one (not unique fullhouse) in a set of card
    """
    def __init__(self, triple: TPattern, pair: TPattern):
        self.triple = triple
        self.pair = pair






