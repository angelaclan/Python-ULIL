#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`card` module 

:author: ` YOUR NAME
         Univ. Lille <http://portail.fil.univ-lille1.fr>`_

:date: 2017, september. Last revision: 2017, september


"""



import random



class Card(object):
      
    VALUES = ("Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Knight", "Queen", "King")  
    COLORS = ("spade", "heart", "diamond", "club")
      
    def __init__(self):
        self.random()
    
    def random(self):
       self.value = random.choices(self.VALUES)[0]
       self.color = random.choices(self.COLORS)[0]
           
    def get_color(self):
        print(self.color)

    def get_value(self):
        print(self.value)

    def printCard(self):
        print ([self.value , self.color])

    def compare_value(self, card):
        if self.value > card.value:
            return 1 
        elif self.value < card.value:
            return -1
        else:
            return 0

    def compare_color(self, card):
        if self.color > card.color:
            return 1
        elif self.color < card.color:
            return -1
        else: return 0       

    def compare(self, card):
        return self.compare_value(card) 
            