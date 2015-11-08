#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""is211 assignment 1"""


class ListDivideException(Exception):
    """ exceptions """
    pass


def listDivide(numbers, divide=2):

    divnums = 0
    for i in numbers:
        if i % divide == 0:
            divnums += 1

    return divnums


def testListDivide():
    """ testing the list divie """

    try:
        assert listDivide([1, 2, 3, 4, 5]) == 2
        assert listDivide([2, 4, 6, 8, 10]) == 5
        assert listDivide([30, 54, 63, 98, 100], divide=10) == 2
        assert listDivide([]) == 0
        assert listDivide([1, 2, 3, 4, 5], 1) == 5
    except:
        raise ListDivideException

if __name__ == '__main__':
    testListDivide()
