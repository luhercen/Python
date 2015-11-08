#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" week 14 task 02"""

import numpy


def numpy_task02(themean, standev, numval):
    """this will return a normally distributed numberss, chosen ramndomly.
    this is useful to for example compare stadistical data"""

    return numpy.random.normal(themean, standev, numval)
