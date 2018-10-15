"""
A Grid of Tichu Cards

Contains the current selected

Can be feed a checker function in order to highlight
whether the selection is valid or not
"""
from typing import List

# noinspection PyUnresolvedReferences
from PyQt5.QtWidgets import QWidget, QGridLayout

from gui.QTCard import QTCard
from pychu.tlogic.tcards import Card


class TCardGrid( QWidget):
    def __init__(self, cards=None):
        if cards is None:
            cards = []
        self.cards = cards
        super().__init__()
        self.initUI()

    def initUI(self):
        list = QGridLayout(self)


        for i,card in enumerate(self.cards):
            qcard = QTCard(card)
            list.addWidget(qcard,0,i)


