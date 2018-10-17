#!/usr/bin/python3

# TODO: this will have a parameter for number of AI and human players

# there needs also to be a mechanism for outputing user messages
from enum import Enum

from pychu.tgame.server import TRound
from pychu.tplayer.humanplayer import HumanPlayer
from pychu.tplayer.stupidai import StupidAI


class State(Enum):
    PreSchupfing = 0
    Schupfing = 1
    PrePlaying = 2


def terminal():
    print('Welcome to Pichu'
          'Listen and repeat...')

    players = [HumanPlayer(), StupidAI(), StupidAI(), StupidAI()]

    tround = TRound(players)
    tround.start()


if __name__ == '__main__':
    terminal()
