#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):
    """customlogger class"""
    def __init__(self, logfilename):
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """ log messages"""
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """ flush """
        handled = []

        try:
            fhandler = open(self.logfilename, 'a')
        except IOError as erg:
            self.log('File cannot be opened')
            raise erg
        try:
            for index, entry in enumerate(self.msgs):
                fhandler.write(str(entry) + '\n')
                handled.append(index)
        except IOError as newerg:
            self.log("Another IOError")
            raise newerg
        except MemoryError:
            self.log('Not Enough Memory')
        finally:
            fhandler.close()

        for index in handled[::-1]:
            del self.msgs[index]
