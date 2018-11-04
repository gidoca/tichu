#!/bin/python
from typing import Collection

from pychu.tlogic.tcards import Card
from pychu.tpattern.fullhouse import TFullHouse
from pychu.tpattern.multiples import TMulti
from pychu.tpattern.tpattern import TPatternEmpty
from pychu.tpattern.straights import TStraight
from pychu.tpattern.tdoublestraight import TDoubleStraight


def ident_pattern_unique(cards: Collection[Card]) :
    """
    for single recognition (eg. on the table)
    :param cards:
    :return: the respective pattern
    or a value exception
    """
    num_cards = len(cards)
    # checking for length makes things too complicated. just assume there is only one pattern present
    # (e.g. no cards left after the pattern is found!)

    if num_cards == 0:
        return TPatternEmpty()
    else:
        for pat in [TDoubleStraight, TFullHouse, TMulti, TStraight]:
            try:
                return pat(cards)
            except Exception as ex:
                pass
                # print(ex)

        return None


def rec_pattern_multi(cards: Collection[Card]):
    pass
