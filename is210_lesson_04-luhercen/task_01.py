#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01"""

import data

print data.SHAKESPEARE

MAXIMUM_WORDS = 0
MINIMUM_WORDS = 50000
AVERAGE_WORDS = 0
NUM_CRISPIAN = 0

TOTAL_LINES = 0
TOTAL_WORDS = 0


for i in data.SHAKESPEARE.split('\n'):
    TOTAL_LINES += 1
    if "Crispian" in i:
        NUM_CRISPIAN += 1

    splitNum = len(i.split())
    TOTAL_WORDS += splitNum
    if splitNum > MAXIMUM_WORDS:
        MAXIMUM_WORDS = splitNum
    if splitNum < MINIMUM_WORDS or TOTAL_LINES == 1:
        MINIMUM_WORDS = splitNum

AVERAGE_WORDS = float(TOTAL_WORDS) / float(TOTAL_LINES)

print
print MAXIMUM_WORDS
print MINIMUM_WORDS
print AVERAGE_WORDS
print NUM_CRISPIAN
