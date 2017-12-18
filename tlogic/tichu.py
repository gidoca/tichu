#!/bin/python

from tlogic.tcards import Color, Special, Card


def generate_deck():
    deck = []
    for color in Color:
        for i in range(2,15):
            print (i, color)
            deck.append (Card(color=color, height=i))
    deck.append(Card(special=Special.dragon, height=17))
    deck.append(Card(special=Special.phoenix, height=17))
    deck.append(Card(special=Special.mahjong, height=1))
    deck.append(Card(special=Special.dog, height=-2))

    for i, card in enumerate(deck):
        print (i,card)
    #print card.height, card.color
    return deck;


