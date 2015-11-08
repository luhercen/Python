#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01"""


def bool_to_str(bvalue, short=False):
    """
    The following will return 'Yes'/'Y' or 'No'/'N' based on bvalue"""
    while short:
        if bvalue is True:
            return "Y"
        else:
            return "N"
    while not short:
        if bvalue is True:
            return "Yes"
        else:
            return "No"

print bool_to_str(False, short=True)
