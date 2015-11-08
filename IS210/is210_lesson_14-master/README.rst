==========================================
IS 210: Software Application Programming I
==========================================
------------
Homework #14
------------

:College: CUNY School of Professional Studies
:Course-Name: Software Application Programming I
:Course-Code: IS 210
:Available: 2014-11-24T09:00:00-0400
:Due-Date: 2014-12-01T09:00:00-0400

Overview
========
The following exercises will give you exposure to numpy. This module is very
power and this assignment only scratches the surface of what they can do. I
encourage you to explore the module on your own and think about what kind of
problems you can solve quickly and easily with numpy.

Make sure you read the numpy PDF document attached to this week's  course
materials.

Task 01
-------

#.  Get ``numpy`` installed on your machine or use the virtual lab. The video in
    this week's course materials covers how to install on Windows. Macintosh
    users please read the instructions on the NumPy.org site. There are also
    numerous online YouTube video covering how to install ``numpy``.

http://sourceforge.net/projects/numpy/files/NumPy/1.9.1/

Task 02
-------

Using numpy, write a function that returns a list of normally-distributed
random numbers.

Specifications
^^^^^^^^^^^^^^

#.  Create a file named ``task_02.py``.

#.  Create a function named ``numpy_task02()``.

#.  The function should accept three parameters,
    one for a mean, one for standard deviation and one for the number of
    random values to return. Use those parameters to create your random
    number generator and the list of values.

#.  Somewhere in the doc string comments of this function,
    explain why it might be useful.

Task 03
-------

Numpy is not just amazingly fast at processing complex arrays of data in
computer memory. It can also read in bucket loads of data stored in text
files very quickly.

Write a program the uses numpy within a function to determin the mean and
standard deviation of the raw values stored in the ``data.txt`` file.

Specifications
^^^^^^^^^^^^^^

#.  Create a file named ``task_03.py``.

#.  Create a function named ``numpy_task03()``.

#.  Wrap all of the IO operations in exception handling.

#.  Use the native numpy text file import function.

#.  Return a tuple of the array data mean and standard deviation in integer
    form.

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
