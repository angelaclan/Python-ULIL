#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`minesweeper` module

:author: Chia-Ling Bragagnolo

:date:  

This module provides functions and a class for minesweeper's game's management.

"""

import random
from enum import Enum
from cell import Cell


################################################
# Type declaration
################################################

class GameState(Enum):
    """
    A class to define an enumerated type with three values :

    * ``winning``
    * ``losing``
    * ``unfinished``

    for the three state of minesweeper game.
    """
    winning = 1
    losing = 2
    unfinished = 3


##############################################
# Function for game's setup and management
##############################################


def neighborhood(x, y, width, height):
    """
    :param x: x-coordinate of a cell
    :type x: int
    :param y: y-coordinate of a cell
    :type y: int
    :param height: height of the grid
    :type height: int
    :param width: widthof the grid
    :type width: int
    :return: the list of coordinates of the neighbors of position (x,y) in a
             grid of size width*height
    :rtype: list of tuple
    :UC: 0 <= x < width and 0 <= y < height
    :Examples:

    >>> neighborhood(3, 3, 10, 10)
    [(2, 2), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4)]
    >>> neighborhood(0, 3, 10, 10)
    [(0, 2), (0, 4), (1, 2), (1, 3), (1, 4)]
    >>> neighborhood(0, 0, 10, 10)
    [(0, 1), (1, 0), (1, 1)]
    >>> neighborhood(9, 9, 10, 10)
    [(8, 8), (8, 9), (9, 8)]
    >>> neighborhood(3, 9, 10, 10)
    [(2, 8), (2, 9), (3, 8), (4, 8), (4, 9)]
    >>> neighborhood(5, 0, 10, 10)
    [(4, 0), (4, 1), (5, 1), (6, 0), (6, 1)]
    """

    points =  [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]
    an_iterator = filter(lambda point: point[0] < width and point[1] < height and point[0] > -1 and point[1] > -1, points)
    filtered_point = list(an_iterator)
    return filtered_point

class Minesweeper():
    """
    >>> game = Minesweeper(20, 10, 4)
    >>> game.get_width()
    20
    >>> game.get_height()
    10
    >>> game.get_nbombs()
    4
    >>> game.get_state() == GameState.unfinished 
    True
    >>> cel = game.get_cell(1, 2)
    >>> cel.is_revealed()
    False
    >>> 
    """

    def __init__(self, width=30, height=20, nbombs=99):
        """
        build a minesweeper grid of size width*height cells
        with nbombs bombs randomly placed.  

        :param width:[optional] horizontal size of game (default = 30)
        :type width: int
        :param height: [optional] vertical size of game (default = 20)
        :type height: int
        :param nbombs: [optional] number of bombs (default = 99)
        :type nbombs: int
        :return: a fresh grid of  width*height cells with nbombs bombs randomly placed.
        :rtype: Minesweeper
        :UC: width and height must be positive integers, and
             nbombs <= width * height
        :Example:

        >>> game = Minesweeper(20, 10, 4)
        >>> game.get_width()
        20
        >>> game.get_height()
        10
        >>> game.get_nbombs()
        4
        >>> game.get_state() == GameState.unfinished 
        True
        """
        self.width = width
        self.height = height
        self.nbombs = nbombs
        self.state = GameState.unfinished        

    def get_height(self):
        """
        :return: height of the grid in self
        :rtype: int
        :UC: none
        """
        return self.height

    def get_width(self):
        """
        :return: width of the grid in game
        :rtype: int
        :UC: none
            """
        return self.width
    
    def get_nbombs(self):
        """
        :return: number of bombs in game
        :rtype: int
        :UC: none
        """
        return self.nbombs

    def get_cell(self, x, y):
        """
        :param x: x-coordinate of a cell
        :type x: int
        :param y: y-coordinate of a cell
        :type y: int
        :return: the cell of coordinates (x,y) in the game's grid
        :type: cell
        :UC: 0 <= x < width of game and O <= y < height of game
        """
        
    
    def get_state(self):
        """
        :return: the state of the game (winning1, losing2 or unfinished3)
        :rtype: GameState
        :UC: none
        """
        return self.state

    def reveal_all_cells_from(self, x, y):
        """
        :param x: x-coordinate
        :param y: y-coordinate
        :return: none
        :side effect: reveal all cells of game game from the initial cell (x,y).
        :UC: 0 <= x < width of game and O <= y < height of game
        """
        

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)


