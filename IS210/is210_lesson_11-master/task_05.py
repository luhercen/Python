#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 05 module"""


class CustomError(Exception):
    """ Error Exception """
    def __init__(self, msg, cause):
        Exception.__init__(self, msg)
        self.cause = cause
