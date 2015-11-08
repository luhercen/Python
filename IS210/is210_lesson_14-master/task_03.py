#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""week 14 task 03"""

import numpy


def numpy_task03(thefile):
    """ the mean and standard devi from file """
    try:
        data = numpy.loadtxt(thefile)

    except IOError:
        print 'no file'

    return int(data.mean()), int(data.std())
