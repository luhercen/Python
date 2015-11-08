==========================================
IS 210: Software Application Programming I
==========================================
------------
Homework #04
------------

:College: CUNY School of Professional Studies
:Course-Name: Software Application Programming I
:Course-Code: IS 210
:Available: 2014-09-15T09:00:00-0400
:Due-Date: 2014-09-22T09:00:00-0400


Instructions
============

The following tasks will either have you interacting with existing files in
the starter repo or creating new ones on the fly. Don't forget to add your
interpreter directive, utf-8 encoding, and a short docstring with any new files
that you create!

.. important::

    In these exercises, you may, on occasion, come across a task that requires
    you to research or use a function or method not directly covered by the
    course text. Since Python is such a large language it would be impossible
    for the author to have included descriptions of each and every available
    function which would largely duplicate the official Python documentation.

    A *vital* skill to successful programming is being comfortable searching
    for and using official language documentation sources like the
    `Python String Documentation`_ page. Throughout our coursework we will be
    practicing both the use of the language in practice and the search skills
    necessary to become functional programmers.

Import Refresher
----------------

While you've used imports before, we'll be using them a great deal more during
this and future assignments. Here's a little refresher:

To import a module, and thus access its members, you only need to add the word
``import`` followed by the name of the module. Eg,

.. code:: pycon

    >>> import mymodule

This makes all of the properties of ``mymodule`` accessible to the current
environment through use of a dot (``.``). Eg,

.. code:: pycon

    >>> import mymodule
    >>> print mymodule.USERS  # you can print its USERS constant
    'Fester, Esther, Lester, Hesther'
    >>> len(mymodule.USERS)  # or get the length
    31
    >>> NEWUSERS = mymodule.USERS + 'Nester'  # just treat it like a variable

When modules are imported in this manner, their properties are accessed, not
copied in the current environment. In this way, changes to the module
properties are reflected in other all other code accessing the module.

.. code:: pycon

    >>> import mymodule
    >>> print mymodule.USERS
    'Fester, Esther, Lester, Hesther'
    >>> mymodules.USERS = 'Nester'
    >>> print mynewmodule.USERS
    'Nester'

Another form of importing involves *copying* properties from another module
into the current one:

.. code:: pycon

    >>> from mymodule import USERS

When this is done, the copied property (to the right of the ``import``
keyword), is locally accessible:

.. code:: pycon

    >>> from mymodule import USERS
    >>> print USERS
    'Fester, Esther, Lester, Hesther'

This means that changes to the local copy are not replicated in the parent.

.. warning::

    Don't do what you're about to see. This is purely for explanatory purposes.

.. code:: pycon

    >>> import mymodule
    >>> from mymodule import USERS
    >>> USERS = 'Nester'
    >>> mymodule.USERS == USERS
    False

What we see here is that the copy is given a new value while the module
attribute is left unchanged.

There are reasons to use both approaches to importing, however, for the
purposes of your current homework, you'll only need to use the short from
``import modulename``. Never attempt to use both as its both redundant and will
create a lint violation.

Task 01: Analyze a String
-------------------------

Loops enable you to process huge amounts of data in a methodical and logical
manner. We'll start by analyzing a string, in particular Shakespeare's famous
*Crispin's Day* speech from Act IV, Scene III of *Henry V*.

#.  Start by creating a new file named ``task_01.py``

#.  In ``task_01.py``, import the data module.

#.  Print data.SHAKESPEARE (isn't it a beautiful speech?).

#.  Using ``for`` and all of the various tools we've previously encountered:

    #.  Find the maximum number of words **per line** in data.SHAKESPEARE and
        save it to a variable named ``MAXIMUM_WORDS`` (eg, between any two
        lines where one has 5 words and one has 6, save the number 6).

    #.  Find the minimum number of words **per line** in data.SHAKESPEARE and
        save it to a variable named ``MINIMUM_WORDS``.

    #.  Find the average number of words **per line** in data.SHAKESPEARE and
        save it to a variable named ``AVERAGE_WORDS``. Use a ``float()`` for
        precision.

    #.  Find the total number of **lines** in data.SHAKESPEARE containing the
        word ``Crispian`` and save the result to a variable named 
        ``NUM_CRISPIAN``.

.. hint::

    You'll have to ``split()`` this string twice to accomplish the first three
    objectives. The first time, you'll be splitting it on the newline (``\n``),
    and the second will use the default setting (without any arguments) to
    split on all whitespace.

    Remember that ``split()`` returns a list which is iterable and thus may be
    used as the data object for a `for` loop. Lists also have measurable
    length with ``len()``. To count the number of members of a list, just use
    ``len(listname)`` the same way you would count the number of characters in
    a string.

.. hint::

    Averages are tough because you'll have to keep a count of both the number
    of lines as well as the total words. Alternately, consider measuring
    the *total words* of the entire speech by using ``split()`` without any
    arguments to split the string on all whitespace (including newlines).

    Don't forget to use your loop counter to count the number of lines.

.. hint::

    To force an integer as a float, use the built-in float constructor,
    ``float()`` which is functionally similar to our old standbys, ``int()``
    and ``str()``

.. hint::

    The `in` operator can be very helpful for testing if one string is found
    within another string. Other methods such as ``.search()`` and
    ``.index()`` can also perform this feat if a little differently.
    
Task 02: Prompting inside a Loop Part I
---------------------------------------

Unlike ``for`` loops, which perform an operation or series of operations for
each member in the iterable object, a ``while`` loop may run indefinitely or at
least until certain conditions change and are met. A common scenario for this
type of loop is checking user input is valid.

For this assignment we are going to create a program that calculates the 
factorial of a given positive number. The user should be prompted with a helpful
error message if they try to enter a negative number. 

A factorial is a non-negative integer that is the product of all positive integers less than or equal to a specified natural number. For example,

The factorial function of 5 is: (1 * 2 * 3 * 4 * 5) = 120

.. code:: console

    $ python task_02.py
    Enter number >> -4
    Invalid number: Please enter a number greater than zero.
    Enter number >> 4
    Factorial of 4 is 24

#.  Create a new file named ``task_02.py``.

#.  Instantiate a variable named, ``VALID`` and set its initial value to False.
    This is a good practice called *pessimistic behavior* to always assume
    the most defensive stance until you have a reason to do otherwise.
    
#.  Instantiate a variable named, ``INPUT_NUM`` and set its initial value to 0.

#.  Instantiate a variable named, ``FACTORIAL`` and set its initial value to 1.

#.  Instantiate a variable named, ``PRODUCT`` and set its initial value to 1.

#.  Begin a ``while`` loop and use ``raw_input()`` to ask your users to input
    a number.
    
    #.  The while loop should depend upon the value of ``VALID`` to know
        whether to stop or continue looping.
    
    #.  Evaluate the entered value with a connection that tests if the number is
        positive (greater than zero). 
        
    #.  Print ``Invalid number: Please enter a number greater than zero.`` if 
        the entered value is negative
        
    #.  The program should re-prompt the user to enter a number.
    
#.  Create a second ``while`` loop that performs the factorial calculation.

    #.  The loop condition should test that the ``FACTORIAL`` value is less than 
        or equal to the ``INPUT_NUM``
        
    #.  Multiply the ``PRODUCT`` variable times the ``FACTORIAL`` variable and 
        assign the value to the ``PRODUCT`` variable name.
        
    #.  Increment the ``FACTORIAL`` variable value by 1.
    
#.  Print the output using a string formatted with the ``.format()`` method. The
    message should include the initial input value and its factorial product.
    
    
.. hint::

    You can find more details about factorial math at: 
    http://en.wikipedia.org/wiki/Factorial



Task 03: Prompting inside a Loop Part II
----------------------------------------

Unlike ``for`` loops, which perform an operation or series of operations for
each member in the iterable object, a ``while`` loop may run indefinitely or at
least until certain conditions change and are met. A common scenario for this
type of loop is checking user input such as comparing a password against a
known database.

.. code:: console

    $ python task_03.py
    What is your password (3 attempts left)? Not correct
    What is your password (2 attempts left)? Umm Yes?
    What is your password (1 attempts left)? I do not remember!
    Access is denied, please try again later.

#.  Create a new file named ``task_02.py``.

#.  In ``task_02.py``, import the ``data`` module.

#.  Instantiate a variable named, ``ACCESS`` and set its initial value to False.
    This is a good practice called *pessimistic behavior* to always assume
    the most defensive stance until you have a reason to do otherwise.

#.  Begin a ``while`` loop and use ``raw_input()`` to ask your users to input
    the password.

    #.  The while loop should depend upon the value of ``ACCESS`` to know
        whether to stop or continue looping.

    #.  Compare the password entered by the user to ``data.PASSWORD``. If the
        user-entered string is the equivalent to ``data.PASSWORD`` set
        ``ACCESS`` to ``True`` and print a message indicating that access was
        granted.

    #.  The user has at most three tries. Keep a counter of the number of loops
        and inform them each time of how many tries they have left.

    #.  If the user has used up all of their tries, exit the loop and print
        a message that they try again some other time.

.. hint::

    You can use ``.format()`` with your raw_input message to change the number
    of attempts on the fly.

.. hint::

    This is a great use-case for the ``break`` statement.

.. hint::

    Instantiate your counter before the loop begins.

Task 04: Looping Mathematical Calculations
------------------------------------------

Both lists and loops may be nested. Here, you'll loop through what is
essentially two lists, the outer list represents the days of a particular
month, while the inner list represents the positive and negative transactions
occurring on that particular day. Eg,

.. csv-table:: Transactions
    :header: "Day", "Daily Transactions"
    :widths: 5, 33

    1, "-$257, -$1918, $2304"
    2, "-$1753"
    3, "-$2993, -$2156"

As the relevant data is already sorted into two lists, it is sequenced data
that may be looped. You will provide insight into the goings on of this
particular account holder.

#.  Import the ``data`` module

#.  Take a moment to examine ``data.TRANSACTIONS`` just to see the structure and
    how it compares to the visual representation above.

#.  Using nested ``for`` loops, calculate the following:

    #.  Provide a running total of all transactions across all days and save
        the result to a variable named ``TOTAL``.
    
    #.  Calculate the minimum **daily** transaction total and store the result
        in a variable named ``MINIMUM``. Considering the example above, this
        would be -$5149, accrued on the third day of transactions.

        For the purpose of this question, use an absolute minimum; do **not**
        calculate *minimum change* (which would be represented as $129
        accrued on the first day).

    #.  Calculate the maximum **daily** transaction total and store the result
        in a variable named ``MAXIMUM``. Considering the example above, this
        would be $129, accrued on the first day of transactions.

        For the purpose of this question, use an absolute maximum; do **not**
        calculate *maximum change*.



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
