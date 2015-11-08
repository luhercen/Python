#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task01"""


def evens_and_odds(numbers, show_even=True):
    """checking even or odds numbers"""
    oddoreven = []
    for num in numbers:
        if num % 2 == 0:
            if show_even is True:
                oddoreven.append(num)
        else:
            if show_even is False:
                oddoreven.append(num)
    return oddoreven
