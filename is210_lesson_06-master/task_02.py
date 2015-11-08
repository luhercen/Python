#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task02"""

import data
import task_01


def get_average(num):
    """getting the average"""
    total = 0.0
    numlen = len(num)
    for number in num:
        total = total + number
    return float(total / numlen)

TOTAL_AVG = get_average(data.TASK_O1)
EVEN_AVG = get_average(task_01.evens_and_odds(data.TASK_O1))
ODD_AVG = get_average(task_01.evens_and_odds(data.TASK_O1, False))

print "Task 02 Report\n" + \
      "-------------------------------\n" + \
      "Total AVG: {:>13,.02f}\n".format(TOTAL_AVG) + \
      "Even AVG:  {:>13,.02f}\n".format(EVEN_AVG) + \
      "Odd AVG:   {:>13,.02f}".format(ODD_AVG)
