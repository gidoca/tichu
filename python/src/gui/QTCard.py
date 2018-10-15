"""
Display of a Tichu Card
"""
from PyQt5.QtCore import QtGui
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout

from tlogic import Card


class QTCard(QWidget):
    def __init__(self, card: Card):
        self.card = card
        super().__init__()
        self.initUI()
        self.selected = False

    def initUI(self):
        self.setFixedSize(80,160)
        text = self.card.__str__()
        layout = QGridLayout(self)
        layout.addWidget(QLabel(text), 0, 0)
        layout.addWidget(QLabel(text), 0, 1)
        layout.addWidget(QLabel(text), 1, 0)
        layout.addWidget(QLabel(text), 1, 1)
        self.setBgColor(QtGui.white)

    def setBgColor(self, color):

        pal = self.palette()
        self.setAutoFillBackground(True)
        pal.setColor(self.backgroundRole(), color )
        self.setPalette(pal)
        # pal.setBrush()

    def toggleSelection(self):
        if self.selected:
            self.setBgColor(QtGui.green)
        else:
            self.setBgColor(QtGui.white)

        self.selected = not self.selected


    def mousePressEvent(self, mouse_event: QtGui.QMouseEvent):
        print(mouse_event)
        self.toggleSelection()






