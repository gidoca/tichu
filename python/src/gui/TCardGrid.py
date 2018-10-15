"""
A Grid of Tichu Cards

Contains the current selected

Can be feed a checker function in order to highlight
whether the selection is valid or not
"""
from typing import List

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QListView, QListWidget, QAbstractItemView, QGridLayout

from gui.QTCard import QTCard
from tlogic import Card


class TCardGrid( QWidget):
    def __init__(self, cards: List[Card] = []):
        self.cards = cards
        super().__init__()
        self.initUI()

    def initUI(self):
        list = QGridLayout(self)


        for i,card in enumerate(self.cards):
            qcard = QTCard(card)
            list.addWidget(qcard,0,i)


