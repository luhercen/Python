#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task03"""


def bubble_sort(int_list):
    """orders numbers 1 by 1"""
    test = False

    while not test:
        test = True
        for i in range(0, len(int_list) - 1):

            if int_list[i] > int_list[i + 1]:

                test = False
                int_list[i], int_list[i + 1] = int_list[i + 1], int_list[i]

    return int_list
