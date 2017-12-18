#!/bin/python

from tlogic.tcards import Color, Special, Card, dragon, phoenix, mahjong, dog


def generate_deck():
    deck = []
    for color in Color:
        for i in range(2,15):
            print (i, color)
            deck.append (Card(color=color, height=i))

    deck.append(dragon)
    deck.append(phoenix)
    deck.append(mahjong)
    deck.append(dog)

    for i, card in enumerate(deck):
        print (i,card)
    #print card.height, card.color
    return deck;


