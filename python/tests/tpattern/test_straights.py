import pytest
import pytest as pt
from pytest import mark

from pychu.tlogic.tcards import tcards
from pychu.tpattern.straights import StraightRec


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

    @mark.parametrize('c1,c2,exp', [
        ('r2 r3 r4 r5 g6', 'r2 r3 r4 r5 g6 g7', True),
        ('r2 r3 r4 r5 g6', 'r2 r3 r4 r5 g6 phx', True),
        ('r2 r3 r4 r5 g6', 'r3 r4 r5 g6 phx', True),
        ('r3 r4 r5 g6 phx','r2 r3 r4 r5 g6',  False),
        ('r10 b11 g12 r13 g14', 'r10 b11 g12 r13 g14 ph', False),
        ('k9 r10 b11 g12 r13', 'r10 b11 g12 r13 g14 ph', True)
    ])
    def test_compare(self, c1, c2, exp):
        st1 = TStraight(tcards(c1))
        st2 = TStraight(tcards(c2))
        assert (st2 > st1) is exp

    @mark.parametrize('c', [
        'b11 g12 r13 g14',
        'r8 b11 g12 r13 g14 ',
        'r8 phx b11 g12 r13 g14 '
    ])
    def test_illegal_straight(self, c):
        with pytest.raises(ValueError):
            st1 = TStraight(tcards(c))
