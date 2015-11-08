#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides utilities for getting lists of data."""


import random


def get_random(length=1000):
    """Returns a list of unique random numbers of a specified length.

    Args:
        length (integer): The length of the list to be returned.

    Returns:
        list: A list of random numbers.

    Examples:
        >>>> get_random(3)
        [2, 3, 1]
    """
    return random.sample(xrange(length), length)
