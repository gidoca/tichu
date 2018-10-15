from unittest import TestCase

import pytest
import pytest as pt

from tlogic.tcards import tcards
from tpattern.straights import StraightRec, TStraight


class TestStraights():
    @pytest.fixture
    def rec(self):
        return StraightRec()

    # todo: parameterize!
    def test_basic(self, rec):
        cards = tcards('r2 r3 r4 g5 g6')
        res = rec.recognize(cards)
        assert len(res) == 1
        p = res[0]
        assert p.combos == 1
        assert len(p.redundant_ranks) == 0

    def test_redundant(self, rec):
        cards = tcards('r2 g2 r3 g3 r4 g5 g6')
        res = rec.recognize(cards)
        pt.assume(len(res) == 1)
        p = res[0]
        pt.assume(p.combos == 1)
        pt.assume(len(p.redundant_ranks) == 2)

    @pytest.mark.parametrize('c1,c2,exp', [
        ('r2 r3 r4 r5 g6', 'r2 r3 r4 r5 g6 g7', True),
        ('r2 r3 r4 r5 g6', 'r2 r3 r4 r5 g6 phx', True),
        ('r10 b11 g12 r13 g14', 'r10 b11 g12 r13 g14 ph', False)
    ])
    def test_compare(self, c1, c2, exp):
        st1 = TStraight(tcards(c1))
        st2 = TStraight(tcards(c2))
        assert (st2 > st1) is exp

    def test_illegal_straight(self):
        with pytest.raises(ValueError):
            st1 = TStraight(tcards('b11 g12 r13 g14'))
