#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    """ Invalid class """
    print "Invalid age"


def get_age(birthyear):
    """ getting age"""

    age = datetime.datetime.now().year - birthyear

    if age > 0:
        return age
    else:
        raise InvalidAgeError
