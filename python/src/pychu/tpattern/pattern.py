import abc


class TPattern(metaclass=abc.ABCMeta):

    # Todo: leave this to the subclasses


    @abc.abstractmethod
    def find(self, cards, higher=True, exact=True):
        pass

