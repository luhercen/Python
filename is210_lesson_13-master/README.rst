==========================================
IS 210: Software Application Programming I
==========================================
------------
Homework #13
------------

:College: CUNY School of Professional Studies
:Course-Name: Software Application Programming I
:Course-Code: IS 210
:Available: 2014-11-17T09:00:00-0400
:Due-Date: 2014-11-24T09:00:00-0400

Overview
========

In this lesson, we'll be practicing implementing two different sorting
algorithms with python.

To help test your code, use ``util.get_random()`` to return a list of random
numbers.

.. code:: pycon

    >>> import util
    >>> util.get_random(3)
    [2, 1, 3]

Task 01: Implement a Selection Sort
===================================

#.  Create a module named ``sorters.py``

#.  In ``sorters.py``, create a function named ``selection()``

#.  ``selection()`` takes one parameter named ``iterable`` and implements the
    `Selection Sort`_ algorithm

#.  ``selection()`` returns the iterable object sorted from least to most by
    the `Selection Sort` algorithm

Example
-------

.. code:: pycon

    >>> sorters.selection([2, 1, 3])
    [1, 2, 3]

Task 02: Implement a Quicksort
==============================

#.  Open ``sorters.py``

#.  In ``sorters.py``, create a function named ``quick()``

#.  ``quick()`` takes one parameter named ``iterable`` and implements the
    `Quicksort`_ algorithm

#.  ``quick()`` returns the iterable object sorted from least to most by the
    `Selection Sort` algorithm

Example
-------

.. code:: pycon

    >>> sorters.selection([2, 1, 3])
    [1, 2, 3]

Submission
==========

Code should be submitted to `GitHub`_ by means of opening a pull request.

As-of Lesson 02, each student will have a branch named after his or her
`GitHub`_ username. Pull requests should be made against the branch that
matches your `GitHub`_ username. Pull requests made against other branches will
be closed.  This work flow mimics the steps you took to open a pull request
against the ``pull`` branch in Lesson 01.

For a refresher on how to open a pull request, please see homework instructions
in Lesson 01. It is recommended that you run PyLint locally after each file
is edited in order to reduce the number of errors found in testing.

In order to receive full credit you must complete the assignment as-instructed
and without any violations (reported in the build status). There will be
automated tests for this assignment to provide early feedback on program code.

When you have completed this assignment, please post the link to your
pull request in the body of the assignment on Blackboard in order to receive
credit.

.. _GitHub: https://github.com/
.. _Python String Documentation: https://docs.python.org/2/library/stdtypes.html
.. _Selection Sort: https://en.wikipedia.org/wiki/Selection_sort
.. _Quicksort: https://en.wikipedia.org/wiki/Quicksort
