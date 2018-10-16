from pytest import mark

from pychu.tlogic.tcards import tcards


#Todo: general mixings for  testing?
class TestDoubleStraights:

    @mark.parametrize('')

    def test_failing(self,c):
        """
        Pattern that do not even have the necessary cards
        :param c:
        :return:
        """
        tc = tcards(c)

    def test_leftovers(self, c):
        """
        Cards that can build a valid pattern but don't use all cards
        :param c:
        :return:
        """

    def test_valid(self, c):
        """
        Verify to accept some simple patterns
        :param c:
        :return:
        """

    def test_comparison(self, c1, c2, exp):
        """
        Check if the rank of two patterns is evaluated correctly
        :param c1:
        :param c2:
        :param exp:
        :return:
        """
    def test_phx(self, c1, c2, exp):
        """
        Specifically test patterns including the phx
        :param c1:
        :param c2:
        :param exp:
        :return:
        """
