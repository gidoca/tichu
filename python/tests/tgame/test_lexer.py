from collections import namedtuple

from pytest import mark, fixture

from pychu.tgame.lexer import TichuLexer


class TestLexer:

    @fixture
    def lexer(self):
        return TichuLexer()

    def test_empty(self, lexer):
        self._test_('',[], lexer)

    @mark.parametrize('inp,exp',[
        ('k2', [('#000000','k2')]),
        ('g2', [('#00ff00','g2')]),
        ('r2', [('#ff0000','r2')]),
        ('b2', [('#0000ff','b2')]),

    ])
    def test_simple(self, inp, exp, lexer):
        self._test_(inp, exp, lexer)


    def _test_(self, inp, exp, lexer):
        MockDoc = namedtuple('MockDocument', 'lines')
        doc = MockDoc([inp])
        res = lexer.lex_document(doc)(0)
        assert exp == res
