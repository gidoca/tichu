from unittest import TestCase

import pytest
import pytest_assume

from tlogic.tcards import Card, tcards
from tpattern.multiples import MultiRec


class TestMultiRec(TestCase):
    def test_4simple(self):
        cards = tcards('k2 r2 b2 g2')
        pr = MultiRec(4)
        out = pr.recognize(cards)
        self.assertEqual({1:cards}, out)
    def test_4simpleph(self):
        cards = tcards('k2 r2 b2 b3')
        pr = MultiRec(4)
        out = pr.recognize(cards)
        self.assertEqual({}, out)
    def test_trix2(self):
        tri2 = tcards('k2 r2 b2')
        tri3 = tcards('r3 g3 b3')
        distraction = tcards('g5 b8 r9 k10 k11 k13')
        cards = distraction + tri2 + tri3
        pr = MultiRec(3)
        out = pr.recognize(cards)
        pytest.assume(len(out) == 2)
        pytest.assume(out[0].rank == 2)
        pytest.assume(out[1].rank == 3)
    def test_3fail(self):
        cards = tcards('k2 r2 b3 g3')
        pr = MultiRec(3)
        out = pr.recognize(cards)
        self.assertEqual(1, out)
    def test_2x2(self):
        cards = tcards('k2 r2 b3 g3')
        pr = MultiRec(2)
        out = pr.recognize(cards)
        self.assertEqual(2, out)

    def test_4ph(self):
        cards = tcards('k2 g2 ph b3 g3')
        pr = MultiRec(2)
        out = pr.recognize(cards, True)
        self.assertEqual(2, out)



