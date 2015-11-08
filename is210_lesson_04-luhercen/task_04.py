#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Task 04"""

import data

TRANSACTIONS = data.TRANSACTIONS

TOTAL = 0
MINIMUM = 0
MAXIMUM = 0

for DAY in TRANSACTIONS:
    DTOTAL = 0
    for INTRANS in DAY:
        DTOTAL = DTOTAL + int(INTRANS)
    TOTAL = TOTAL + DTOTAL
    if DTOTAL < MINIMUM:
        MINIMUM = DTOTAL
    if DTOTAL > MAXIMUM:
        MAXIMUM = DTOTAL
print
print TRANSACTIONS
print MAXIMUM
print MINIMUM
print TOTAL
