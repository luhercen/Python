#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""task08"""


from data import FRUIT


def get_cost_per_item(shoplist):
    """list of items shop list"""

    return {key: FRUIT.get(key) * val for key, val in shoplist.iteritems()
            if key in FRUIT}


def get_total_cost(shoplist):
    """list of items shop list"""
    return sum(get_cost_per_item(shoplist).itervalues())
