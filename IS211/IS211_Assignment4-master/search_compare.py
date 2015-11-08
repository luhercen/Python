#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""is211 Assignment 4, search and compare """


import random
import time


def sequential_search(a_list, item):
    """ STRUCTURE TAKEN FROM THE BOOK SAMPLE to calculate
     how long function takes:
    def sequential_search(a_list, item):
    pos = 0
    found = False
    while pos < len(a_list) and not found:
    if a_list[pos] == item:
    found = True
    else:
    pos = pos+1
    return found
    """

    timstarts = time.time()
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos += 1

    timends = time.time()
    timetaken = timends - timstarts

    return timetaken, found

def ordered_sequential_search(a_list, item):


    """ STRUCTURE TAKEN FROM THE BOOK SAMPLE to calculate
     how long function takes:
    def ordered_sequential_search(a_list, item):
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
    if a_list[pos] == item:
    found = True
    else:
    if a_list[pos] > item:
    stop = True
    else:
    pos = pos+1
    return found
    """

    timstarts = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos += 1

    timends = time.time()
    timetaken = timends - timstarts

    return timetaken, found

def binary_search_iterative(a_list, item):


    """ STRUCTURE TAKEN FROM THE BOOK SAMPLE to calculate
    how long function takes:
    def binary_search(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
    midpoint = (first + last) // 2
    if a_list[midpoint] == item:
    found = True
    else:
    if item < a_list[midpoint]:
    last = midpoint - 1
    else:
    first = midpoint + 1
    return found
    """

    timstarts = time.time()
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    timends = time.time()
    timetaken = timends - timstarts

    return timetaken, found

def binary_search_recursive(a_list, item):


    """ STRUCTURE TAKEN FROM THE BOOK SAMPLE to calculate
     how long function takes:
    def binary_search(a_list, item):
    if len(a_list) == 0:
    return False
    else:
    midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
    return True
    else:
    if item < a_list[midpoint]:
    return binary_search(a_list[:midpoint], item)
    else:
    return binary_search(a_list[midpoint + 1:], item)
    """

    timstarts = time.time()
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2

    if a_list[midpoint] == item:
            return True
    else:
        if item < a_list[midpoint]:
            timends = time.time()
            timetaken = timends - timstarts
            return (binary_search_recursive(a_list[:midpoint], item),
                timetaken)
        else:
            timends = time.time()
            timetaken = timends - timstarts
            return timetaken, binary_search_recursive(a_list[midpoint + 1], item)


def main():
    """ main will print out how long eah func takes, on average. Generating 100 random
    input list, of sisez 500, 1000 and 10000, and taking its average"""


    seque_search_500 = 0
    seque_search_1000 = 0
    seque_search_10000 = 0

    oseque_search_500 = 0
    oseque_search_1000 = 0
    oseque_search_10000 = 0

    ite_binary_500 = 0
    ite_binary_1000 = 0
    ite_binary_10000 = 0

    recu_binary_500 = 0
    recu_binary_1000 = 0
    recu_binary_10000 = 0

    container500 = 0
    container1000 = 0
    container10000 = 0


    for i in xrange(100):
        container500 = [int(100*random.random())
                        for i in xrange(500)]
        container1000 = [int(100*random.random())
                         for i in xrange(1000)]
        container10000 = [int(100*random.random())
                          for i in xrange(10000)]

        """ 500, 1000, 10000 search outputs """
        seque500 = sequential_search(container500, -1)
        seque_search_500 = seque500[1]

        seque1000 = sequential_search(container1000, -1)
        seque_search_500 = seque1000[1]

        seque10000 = sequential_search(container10000, -1)
        seque_search_500 = seque10000[1]


        oseque500 = sequential_search(container500, -1)
        oseque_search_500 = oseque500[1]

        oseque1000 = sequential_search(container1000, -1)
        oseque_search_1000 = oseque1000[1]

        oseque10000 = sequential_search(container10000, -1)
        oseque_search_10000 = oseque10000[1]


        ite500 = sequential_search(container500, -1)
        ite_binary_500 = ite500[1]

        ite1000 = sequential_search(container1000, -1)
        ite_binary_1000 = ite1000[1]

        ite10000 = sequential_search(container10000, -1)
        ite_binary_10000 = ite10000[1]


        recu500 = sequential_search(container500, -1)
        recu_binary_500 = recu500[1]

        recu1000 = sequential_search(container1000, -1)
        recu_binary_1000 = recu1000[1]


        recu10000 = sequential_search(container10000, -1)
        recu_binary_10000 = recu10000[1]


        """taking average"""

        seque500_average = seque_search_500 / 100
        seque1000_average = seque_search_1000 / 100
        seque10000_average = seque_search_10000 / 100

        oseque500_average = oseque_search_500 / 100
        oseque1000_average = oseque_search_1000 / 100
        oseque10000_average = oseque_search_10000 / 100

        ite500_average = ite_binary_500 / 100
        ite1000_average = ite_binary_1000 / 100
        ite10000_average = ite_binary_10000 / 100

        recu500_average = recu_binary_500 / 100
        recu1000_average = recu_binary_1000 / 100
        recu10000_average = recu_binary_10000 / 100


        """sorting"""


        container500.sort()
        container1000.sort()
        container10000.sort()

    """following format = Sequential Search took %10.7f seconds, on average"""
    print "Sequential Search took %10.7f seconds, on average, to run over a list of 500 items" % seque500_average
    print "Sequential Search took %10.7f seconds, on average, to run over a list of 1000 items" % seque1000_average
    print "Sequential Search took %10.7f seconds, on average, to run over a list of 10000 items" % seque10000_average
    print "Ordered Sequential Search took %10.7f seconds, on average, to run over a list of 500 items" % oseque500_average
    print "Ordered Sequential Search took %10.7f seconds, on average, to run over a list of 1000 items" % oseque1000_average
    print "Ordered Sequential Search took %10.7f seconds, on average, to run over a list of 10000 items" % oseque10000_average
    print "Binary Search Iterative took %10.7f seconds, on average, to run over a list of 500 items" % ite500_average
    print "Binary Search Iterative took %10.7f seconds, on average, to run over a list of 1000 items" % ite1000_average
    print "Binary Search Iterative took %10.7f seconds, on average, to run over a list of 10000 items" % ite10000_average
    print "Binary Search Recursive took %10.7f seconds, on average, to run over a list of 500 items" % recu500_average
    print "Binary Search Recursive took %10.7f seconds, on average, to run over a list of 1000 items" % recu1000_average
    print "Binary Search Recursive took %10.7f seconds, on average, to run over a list of 10000 items" % recu10000_average



if __name__ == "__main__":
    main()
