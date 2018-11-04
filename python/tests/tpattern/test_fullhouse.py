import pytest
from pytest import mark

from pychu.tlogic.tcards import tcards
from pychu.tpattern.fullhouse import TFullHouse
from tpattern.test_pattern import _find_


class TestFullHouse():

    @mark.parametrize('c1,c2,exp', [
        ('r2 g2 b2 r5 g5', 'r10 g10 k10 r3 g3', True),
        ('rgbk2 rgbk5', 'rgk3 rbg10', True),
        ('rgbk2 rgbk5', 'rgk3 rg10', False),
    ])
    def test_compare(self, c1, c2, exp):
        fh1 = TFullHouse(tcards(c1))
        fh2 = TFullHouse(tcards(c2))
        assert exp == fh2.gt_table(fh1)

    @mark.parametrize('c', [
        'r2 b2 g5 k5',
        '',
        'r2 g2 k7 ph',
        'gb2 g5 ph',
        'rg2 k7 g8 ph' #Phoenix can only be used once
    ])
    def test_invalid(self, c):
        with pytest.raises(ValueError):
            tc = tcards(c)
            fh = TFullHouse(tc)
            print(fh)

    @mark.parametrize('c,rank', [
        ('r2 g2 ph g3 k3',3),
        ('rgk2 gk3',2),
        ('rgk13 rk2',13),
        ('rgk14 rkg2',14)
    ])
    def test_creation(self, c,rank):
        tc = tcards(c)
        fh = TFullHouse(tc)
        assert rank == fh.rank

    @mark.parametrize('cards',[
        'rgb3 kgb2 r5 g6',
        'kgb2 rgb3 g5',
        'gbr2 gb5 ph',
        'gbr2 gb5 ph r6',
    ])
    def test_leftovers(self,cards):
        with pytest.raises(ValueError):
            tc = tcards(cards)
            fh = TFullHouse(tc)
            print(fh)

    @mark.parametrize('table, hand, exp', [
        ('rgb3 kg2', 'rgb5 br2', ['rgb5 br2']),
        ('rgb3 kg2', 'rg5 br2', []),
        ('rgb3 kg2', 'rgb5 br2 kgb10', ['rgb5 br2 kgb10']), #Full house can only return one combo due to the no constraint between pairs and triples
    ])

    def test_find(self, table, hand, exp):
        _find_(TFullHouse, table, hand, exp)


