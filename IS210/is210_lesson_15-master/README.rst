==========================================
IS 210: Software Application Programming I
==========================================
------------
Homework #15
------------

:College: CUNY School of Professional Studies
:Course-Name: Software Application Programming I
:Course-Code: IS 210
:Available: 2014-12-01T09:00:00-0400
:Due-Date: 2014-12-8T09:00:00-0400

Overview
========
This homework will let you experiment with Beautiful Soup. Just like the numpy
homework, these exercises will only scratch the surface of what is possible.
Also, the instructions in these parts are a little more general since there is
potentially a few ways to solve each part.  Ideally, you will spend some time
exploring the module to understand what it can do.

Make sure you read the Beautiful Soup online documentation available at:

http://beautiful-soup-4.readthedocs.org/en/latest/

Task 01
-------

#.  Install Beautiful Soup on your computer. Follow the installation guide available
    online.

http://beautiful-soup-4.readthedocs.org/en/latest/#installing-beautiful-soup

.. tip::

    Make sure you install ``beautifulsoup4`` and not the older version which
    uses the ``BeautifulSoup`` naming pattern.

Task 02
-------

Using ``bs4`` module, write a function that returns President Obama's official
stance on Internet Neutrality.

Specifications
^^^^^^^^^^^^^^

#.  Open the file named ``beautifulsoup_02.py``.

#.  Create a function named ``obama_net_neutrality()``.

#.  The function should use the static ``HTML_SOUP`` variable to find the
    paragraph comprising Obama's Net Neutrality statement.

#.  Return only the text without any leading or trailing white space.

Task 03
-------

Now let's have a little fun with the CUNY SPS web site. Use beautiful soup to
parse the names of IT department staff. Your program should return a list of
dictionaries that contain a first name, last name and email address.

.. note::

    The SPS IT department directory requires two pages to display all of the
    names. We will only be concerned with the first page.

Specifications
^^^^^^^^^^^^^^

#.  Open the file named ``beautifulsoup_03.py``.

#.  Create a function named ``sps_it_department()``.

#.  Use the Beautiful Soup ``find_all()`` method to collect all of the business
    cards.

#.  Split the name into first and last components.

#.  Return the data in the form of a list of dictionaries that contain first name,
    last name and email address.



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
