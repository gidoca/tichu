from pytest import mark

from pychu.tlogic.tcards import tcards
from pychu.tlogic.thelpers import ident_pattern_unique
from pychu.tpattern.fullhouse import TFullHouse
from pychu.tpattern.multiples import TMulti
from pychu.tpattern.straights import TStraight
from pychu.tpattern.tdoublestraight import TDoubleStraight






class TestRecAllPatterns():
    @mark.parametrize('cards, clazz', [
        ('g2 b2 r3 r4 r5 r6', TStraight),
        ('gr2 bg3', TDoubleStraight),
        ('drn', TMulti),
        ('ma', TMulti),
        ('grb2 bg4', TFullHouse),
        ('grb2 bg3', TDoubleStraight)
    ])
    def test_basics(self, cards, clazz):
        tc = tcards(cards)
        pat = clazz(tc)
        assert pat.__repr__() == ident_pattern_unique(tc).__repr__()
        print(pat)


def _find_(clazz, table, hand, exp):
    ts = clazz(tcards(table))
    res = ts.find(tcards(hand))
    f = lambda x: clazz(tcards(x))
    exp2 = list(map(f, exp))
    # exp2 = {k:tcards(v) for k,v in exp.items()}
    assert exp2 == res