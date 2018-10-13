#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
First try of creating a Qt gui (via python)
"""

import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QAction, qApp, QWidget, QMenuBar

from gui import TCardGrid
from tlogic import Card


class TiQu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Init GUI…', 10)
        self.setWindowTitle('TiQu')
        self.setToolTip('This will be well, a Tichu App')
        btOk = QPushButton('Ok', self)
        btOk.setToolTip('Gagi')

        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setStatusTip('Exitting... Exciting!')
        exitAct.triggered.connect(qApp.quit)

        self.menuBar = QMenuBar()
        file = self.menuBar.addMenu('&Gagi')
        file.addAction(exitAct)

        cards = Card.mstr('g2 b3 k5')

        qcardgrid = TCardGrid(cards)
        self.setCentralWidget(qcardgrid)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = TiQu()
    w.resize(250, 150)
    w.move(300, 300)
    w.show()

    sys.exit(app.exec())
