#!/bin/python
from typing import Collection, List

from pychu.tlogic.tcards import Card
from pychu.tpattern.multiples import TMulti, PassOrEmpty
from pychu.tpattern.pattern import TPattern


class DoubleStraight(object):
    pass


def rec_pattern_unique(cards: Collection[Card]) -> TPattern:
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
        return PassOrEmpty()
    else:
        for pat in [TMulti, DoubleStraight]:
            try:
                return pat(cards)
            except Exception as ex:
                print(pat, cards, ex)
                continue


def rec_pattern_multi(cards: Collection[Card]) -> List[TPattern]:
    pass
