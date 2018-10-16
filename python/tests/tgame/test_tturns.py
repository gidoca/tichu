# TTurn is rather gonna be a data object
# or might even be left out in python
# due to using dicts
# Hence tests are not too useful
# class TestTTurn():
#     def

# In order for this test to give valid result
# the TPattern Classes must all work expectedly
from pychu.tgame.server import TTurn


class TestTurnValidator:

    def test_rejection(self,cards):
        """
        Give an invalid pattern of cards, e.g.::

            [{mah}, {k2, r2}]
            [{phx}, {mah}]
            [{k14}, {drn}, {phx}]

        or a straight with a different length and so on
        (this should already be checked by in the pattern class)
        should raise a value error

        :param cards:
        :return:
        """
        tt = TTurn()
    def test_valid(self, cards):
        """
        Just give a list of valid patterns

        :param cards:
        :return:
        """

class TestTurn:

    def test_win(self, cards):
        """
        Verify if a "win" of a turn is noted correctly

        :param cards:
        :return:
        """

    def test_bombs(self, cards):
        """
        Verify that bombs are allowed outside normal playing mode
        -> Self bombing
        -> Bombing if it is not the turn
        :param cards:
        :return:
        """



