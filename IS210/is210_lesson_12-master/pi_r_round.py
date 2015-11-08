#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
is210 Section 01 Week 12
Bench marking methods
Works Cited:
    The following Pi calculation functions were sourced from the "Captian
    DeadBones Chronicles" blog posting "Computing Pi With Python".
    http://thelivingpearl.com/2013/05/28/computing-pi-with-python/
    Minor changes were made to conform with lesson plan.
"""

import math
from decimal import Decimal
import time
import sys


class Timer2Class(object):
    """ timer class """
    timer = time.clock if sys.platform[:3] == 'win' else time.time

    def __init__(self, func, *args, **kwargs):
        """ init """
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def total(self):
        """ total """
        _reps = self.kwargs.pop('_reps', 1000)
        repslist = list(range(_reps))
        start = self.timer()
        for _ in repslist:
            ret = self.func(*self.args)
        elapsed = self.timer() - start
        return (elapsed, ret)

    def bestof(self):
        """ the best of """
        _reps = self.kwargs.pop('_reps', 5)
        best = 2 ** 32
        for _ in range(_reps):
            start = self.timer()
            ret = self.func(*self.args)
            elapsed = self.timer() - start
            if elapsed < best:
                best = elapsed
        return (best, ret)

    def bestoftotal(self):
        """ the best of total """
        _reps1 = self.kwargs.pop('_reps1', 5)
        return (self.func.__name__, min(self.total() for i in range(_reps1)))


def stdlib(depth):
    """
    Calculate Pi using the math.pi from Python standard library
    :param depth:
    :return:
    """
    var_a = Decimal(1.0)
    var_b = Decimal(1.0 / math.sqrt(2))
    var_t = Decimal(1.0) / Decimal(4.0)
    var_p = Decimal(1.0)

    for _ in range(depth):
        var_at = Decimal((var_a + var_b) / 2)
        var_bt = Decimal(math.sqrt(var_a * var_b))
        var_tt = Decimal(var_t - var_p * (var_a - var_at) ** 2)
        var_pt = Decimal(2 * var_p)

        var_a = var_at
        var_b = var_bt
        var_t = var_tt
        var_p = var_pt

    var_pi = (var_a + var_b) ** 2 / (4 * var_t)

    return str(var_pi)


def bbp(depth):
    """
    Calculate Pi using the Bailey–Borwein–Plouffe formula
    http://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula
    :param depth:
    :return:
    """
    var_pi = Decimal(0)
    k = 0
    while k < depth:
        var_pi += (Decimal(1) / (16 ** k)) * (
            (Decimal(4) / (8 * k + 1)) -
            (Decimal(2) / (8 * k + 4)) -
            (Decimal(1) / (8 * k + 5)) -
            (Decimal(1) / (8 * k + 6))
        )
        k += 1
    return str(var_pi)


def bellard(depth):
    """
    New school Pi calculation method discovered in 1997 by Fabrice Bellard in
    1997. Usually clocks in 43% faster than the BBP formula.
    http://en.wikipedia.org/wiki/Bellard%27s_formula
    :param depth:
    :return:
    """
    var_pi = Decimal(0)
    k = 0
    while k < depth:
        var_pi += (Decimal(-1) ** k / (1024 ** k)) * (
            Decimal(256) / (10 * k + 1) +
            Decimal(1) / (10 * k + 9) -
            Decimal(64) / (10 * k + 3) -
            Decimal(32) / (4 * k + 1) -
            Decimal(4) / (10 * k + 5) -
            Decimal(4) / (10 * k + 7) -
            Decimal(1) / (4 * k + 3)
        )
        k += 1
    var_pi = var_pi * 1 / (2 ** 6)
    return str(var_pi)


def chudnovsky(depth):
    """
    World record holding formula for calculating 5 trillion digits of Pi in
    August 2010. It's a heavy hitter on CPU. This one is about quality over
    quantity.
    http://en.wikipedia.org/wiki/Chudnovsky_algorithm
    :param depth:
    :return:
    """
    var_pi = Decimal(0)
    k = 0
    while k < depth:
        var_pi += (Decimal(-1) ** k) * (
            Decimal(math.factorial(6 * k)) /
            (
                (math.factorial(k) ** 3) * (math.factorial(3 * k))
            ) * (13591409 + 545140134 * k) /
            (640320 ** (3 * k))
        )
        k += 1
    var_pi = var_pi * Decimal(10005).sqrt() / 4270934400
    var_pi **= -1
    return var_pi


if __name__ == "__main__":
    DEPTH_N = 1000
    for test in (stdlib, bbp, bellard, chudnovsky):
        timer2 = Timer2Class(test, DEPTH_N, _reps1=1, _reps=3)
        print timer2.bestoftotal()
