from unittest import TestCase

from tlogic.tcards import Card, tcards
from tpattern.multiples import MultiRec


class TestRecAllPatterns(TestCase):

    def straight_and_pairs(self):
        cards = tcards('g2 b2 r3 r4 r5 r6')
        # expect =


