#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" week 13"""


def selection(iterable):
    """Task 01 implement a selection sort"""
    sorttool = 0
    while sorttool != len(iterable):
        for thevals in range(sorttool, len(iterable)):
            if iterable[thevals] < iterable[sorttool]:
                iterable[sorttool], iterable[thevals] = iterable[
                    thevals], iterable[sorttool]
        sorttool = sorttool + 1
    return iterable


def quick(iterable):
    """Task 02  Implement   a quicksort"""
    small = []
    pivotlist = []
    big = []
    if len(iterable) <= 1:
        return iterable
    else:
        pivot = iterable[0]
        for theval in iterable:
            if theval < pivot:
                small.append(theval)
            elif theval > pivot:
                big.append(theval)
            else:
                pivotlist.append(theval)
        small = quick(small)
        big = quick(big)
        return small + pivotlist + big
