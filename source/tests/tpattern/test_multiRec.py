from unittest import TestCase

from tlogic import Card
from tpattern.multiples import MultiRec


class TestMultiRec(TestCase):
    ##
    def test_4simple(self):
        cards = Card.mstr('k2 r2 b2 g2')
        pr = MultiRec(4)
        out = pr.recognize(cards)
        self.assertEqual(1, out)
    def test_4simpleph(self):
        cards = Card.mstr('k2 r2 b2 b3')
        pr = MultiRec(4)
        out = pr.recognize(cards)
        self.assertEqual(0, out)
    def test_3simple(self):
        cards = Card.mstr('k2 r2 b2 g3')
        pr = MultiRec(3)
        out = pr.recognize(cards)
        self.assertEqual(1, out)
    def test_3fail(self):
        cards = Card.mstr('k2 r2 b3 g3')
        pr = MultiRec(3)
        out = pr.recognize(cards)
        self.assertEqual(1, out)
    def test_2x2(self):
        cards = Card.mstr('k2 r2 b3 g3')
        pr = MultiRec(2)
        out = pr.recognize(cards)
        self.assertEqual(2, out)

    def test_4ph(self):
        cards = Card.mstr('k2 g2 ph b3 g3')
        pr = MultiRec(2)
        out = pr.recognize(cards, True)
        self.assertEqual(2, out)



