#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 04 module"""


class BaseException(Exception):
    """ parent class"""
    pass


class StringError(BaseException, TypeError):
    """ son class"""
    pass


class NumberError(BaseException, TypeError):
    """ son class"""
    pass


class NonZeroError(NumberError):
    """ error class """
    pass
