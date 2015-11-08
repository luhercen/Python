#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task03"""


import time


class Snapshot(object):
    """ Simply sets 'created' to the current time """

    def __init__(self):
        self.created = time.time()