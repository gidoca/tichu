import abc
from abc import abstractmethod

from tlogic.tcards import Card
from typing import Set, Collection


class TPattern(metaclass=abc.ABCMeta):

    # Todo: leave this to the subclasses


    @abc.abstractmethod
    def find(self, cards, higher=True, exact=True):
        pass

