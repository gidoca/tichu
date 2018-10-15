import pytest
from pytest import mark

from pychu.tlogic.tcards import tcards
from pychu.tpattern.fullhouse import TFullHouse


class TestFullHouse():

    @mark.parametrize('c1,c2,exp', [
        ('r2 g2 b2 r5 g5', 'r10 g10 k10 r3 g3', True)
    ])
    def test_compare(self, c1, c2, exp):
        fh1 = TFullHouse(tcards(c1))
        fh2 = TFullHouse(tcards(c2))
        assert (fh2 > fh1) is exp

    @mark.parametrize('c', [
        'r2 b2 g5 k5',
        '',
        'r2 g2 k7 ph'
    ])
    def test_invalid(self, c):
        with pytest.raises(ValueError):
            fh = TFullHouse(tcards)

    @mark.parametrize('c', [
        'r2 g2 ph g3 k3'
    ])
    def test_creation(self, c):
        tc = tcards(c)
        fh = TFullHouse(tc)
        assert fh

