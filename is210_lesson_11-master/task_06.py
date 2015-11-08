#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 06 module"""


def exception_test(arg1, arg2, arg3):
    """ Exception Test """
    caught = False
    try:
        arg1[arg2].index(arg3)
    except (TypeError, LookupError):
        caught = True
    return caught
