from unittest import TestCase

from tlogic import Card


class TestCard(TestCase):
    def testSetCapabilities(self):
        l = Card.mstr('g2 k2 ma ph')
        s1= set(l)
        s1.remove(Card.from_string('g2'))
        s2 = set(Card.mstr('k2 ma ph'))
        self.assertSetEqual(s1, s2)


