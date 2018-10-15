import itertools

from pytest import mark

from pychu.tlogic.tcards import tcard, Color, Special, Card





ranks = map(str, range(2, 15))
colors = 'rgbk'
simple_card_strings = map(''.join, itertools.product(colors, ranks))
special_strs = 'maj dog phx drn'.split()
card_strings = list(itertools.chain(special_strs, simple_card_strings))

print(card_strings)


class TestCard():

    def test_set_capabilities(self):
        l = tcard('g2 k2 ma ph')
        s1 = set(l)
        s1.remove(tcard('g2'))
        s2 = set(tcard('k2 ma ph'))
        assert s1 == s2

    @mark.parametrize('c', card_strings)
    def test_from_str(self, c):
        tc = tcard(c)
        assert c == tc.__repr__()

    # that is focking noice!
    @mark.parametrize('rank', range(2, 15))
    @mark.parametrize('color', Color)
    def test_from_params(self, rank, color):
        tc = Card(color=color, rank=rank)
        assert rank == tc.rank
        assert color == tc.color
        assert color.value+str(rank) == tc.__repr__()

    @mark.parametrize('special', Special)
    def test_special(self, special):
        c = Card(special=special)
        assert special == c.special
        assert 2 >= c.rank > 14

