#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Task 03"""

import data

PASSWORD = data.PASSWORD
ACCESS = False
ERRALLOWED = 3

while not ACCESS:
    QUESTION = "What is your password ({} attempts left)?".format(ERRALLOWED)
    ANSWER = raw_input(QUESTION)

    if ANSWER != PASSWORD:
        ERRALLOWED -= 1
        if ERRALLOWED == 0:
            print "Access is denied, please try again later."
            break
    else:
        ACCESS = True
        print "Access is granted."
