#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""continuation"""

import os
import pickle


class PickleCache(object):
    """continuation on work for week 10"""
    def __init__(self, file_path="datastore.pkl"):
        """class picklecache"""
        self.__file_path = file_path
        self.__file_object = None
        self.__data = {}

    def set(self, key, value):
        """ Task 05: Add a Set Method """
        self.__data[key] = value

    def get(self, key):
        """ Task 06: Add a Get Method """
        if key in self.__data:
            return self.__data[key]
        else:
            print "Error: No value found for key: '{}'".format(key)

    def delete(self, key):
        """ Task 07: Add a Delete Method """
        if key in self.__data:
            del self.__data[key]

    def open(self):
        """ Task 08: Add the Open Method """
        if os.path.exists(self.__file_path):
            if os.path.getsize(self.__file_path) > 0:
                self.__file_object = open(self.__file_path, "rb")
                self.__data = pickle.load(self.__file_object)
                self.__file_object.close()
        self.__file_object = open(self.__file_path, "wb")

    def flush(self, reopen=True):
        """ Task 09: Create a Flush Method """
        pickle.dump(self.__data, self.__file_object)
        self.__file_object.close()
        self.__file_object = None
        if reopen:
            self.open()

    def close(self):
        """ Task 10: Create a Close Method """
        self.flush(reopen=False)
