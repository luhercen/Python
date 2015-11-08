#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Task 04 """

DAY = raw_input("What day is today? : ")
TIME = int(raw_input("What time is it? (Enter without a column. Ex:0630) : "))

if DAY == 'Sat' or 'Sun' and TIME < 600:
    SNOOZE = True

else:
    SNOOZE = False

print SNOOZE
