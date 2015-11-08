==========================================
IS 210: Software Application Programming I
==========================================
------------
Homework #05
------------

:College: CUNY School of Professional Studies
:Course-Name: Software Application Programming I
:Course-Code: IS 210
:Available: 2014-09-22T09:00:00-0400
:Due-Date: 2014-09-29T09:00:00-0400


Instructions
============

The following tasks will either have you interacting with existing files in
the starter repo or creating new ones on the fly. Don't forget to add your
interpreter directive, utf-8 encoding, and a short docstring with any new files
that you create!

.. important::

    In these exercises, you may, on occasion, come across a task that requres
    you to research or use a function or method not directly covered by the
    course text. Since Python is such a large language it would be impossible
    for the author to have included descriptions of each and every available
    function which would largely duplicate the offical Python documentation.

    A *vital* skill to successful programming is being comfortable searching
    for and using official language documentation sources like the
    `Python String Documentation`_ page. Throughout our coursework we will be
    practicing both the use of the language in practice and the search skills
    necessary to become functional programmers.

Task 01: Defining a Function
----------------------------

Just to get our feet wet, we're going to define a very basic function that has
probably been invented and reinvented for nearly every user-facing application
in the wild. Just because an function is simple does not mean it's only for
beginners. *Helper functions* as these are called, save hours of work and more
importantly, enforce consistency across the broad scope of an application.

Specifications
^^^^^^^^^^^^^^

#.  Create a file named ``task_01.py``

#.  Within, ``task_01.py``, define a function named ``bool_to_str()``

    #.  ``bool_to_str()`` will convert a boolean value of ``True`` or ``False``
        to the string values of ``Yes`` or ``No``

    #.  Takes 2 arguments:

        #.  The first argument should be named ``bvalue``

        #.  The second argument should be named ``short`` and have a default
            value of ``False``

    #.  Returns a string

    #.  If ``short`` is set to to ``True`` it should only return ``Y`` or ``N``

.. note::

    For the purpose of this document and others, when I refer to function
    names, I will always include the open and close parens "()" to indicate
    that I am speaking about a function.

.. note::

    As we move into functions, what you choose to call your variables will
    have considerably diminished importance. At this point, it's far more
    important to name your arguments correctly and place them in the directed
    order.

Examples
^^^^^^^^

.. code:: pycon

    >>> import task_01
    >>> task_01.bool_to_str(False)
    'No'
    >>> task_01.bool_to_str(True, short=True)
    'Y'

Task 02: Loan Calculator Revisited
----------------------------------

Here we revisit the loan calculator from Homework #3, Task #5. One benefit of
implementing programs within the context of a function is that they become
re-usable in other portions of your system. It's not unreasonable to think of
many points where the ``compound_interest()`` function below could be used.

.. important::

    Do not use ``raw_input()`` to complete this task. All previous calls to
    ``raw_input()`` should be replaced with functions that take arguments as
    input.

.. important::

    In the interest of simplicity, you don't need to convert the
    prequalification variable from the string 'Yes/No' to a boolean. Just
    assume that it is already converted to boolean ``True`` or ``False`` for
    your arguments.

Specifications
^^^^^^^^^^^^^^

#.  Open ``task_02.py``

#.  Re-implement this code as a set of functions:

    #.  ``get_interest_rate()`` returns the interest rate, as a decimal, for
        the passed, ``principal``, ``duration``, and ``prequalification``

        #.  Takes three arguments:
            
            #.  ``principal``, a numeric type, the value of the principal

            #.  ``duration``, a numeric type, the duration of the loan

            #.  ``prequalification`` a boolean, whether or not the loan is
                pre-qualified.

        #.  Returns a decimal form of the interest rate or ``None`` if none
            exists.

    #.  ``compound_interest`` calculates compound interest for a given
        ``principal``, ``duration``, ``rate``, and ``interval``

        #.  Takes four arguments:
            
            #.  ``principal``, a numeric type, the value of principal

            #.  ``duration``, a numeric type, the duration of the loan

            #.  ``rate``, a numeric type, the interest rate

            #.  ``interval``, a numeric type, defaults to 12, the number of
                times that interest is compounded annually

        #.  Returns the compounded interest and principal (combined) as a
            numeric type.

    #.  ``calculate_total()`` returns the total amount owed over the life of
        the loan.

        #.  Takes three arguments:
            
            #.  ``principal``, an integer, the value of the principal

            #.  ``duration``, an integer, the duration of the loan

            #.  ``prequalification`` a boolean, whether or not the loan is
                pre-qualified.

        #.  Finds the rate with ``get_interest_rate()`` and calculates the
            total with ``compound_interest()``.

        #.  Returns the total, rounded to the nearest integer. In the event
            that there is no interest rate for the passed arguments, returns
            ``None``.

#.  In addition, we're going to add one more function:

    #.  ``calculate_interest`` returns just the interest owed over the life
        of the loan (without the principal).

        #.  Takes three arguments:
            
            #.  ``principal``, an integer, the value of the principal

            #.  ``duration``, an integer, the duration of the loan

            #.  ``prequalification`` a boolean, whether or not the loan is
                pre-qualified.

        #.  Finds the rate with ``get_interest_rate()`` and calculates the
            total with ``compound_interest()``.

        #.  Returns just the interest owed over the life of the loan as an
            integer. This may be calculated by calculating the total with
            ``calculate_total()`` and subtracting the ``principal``. In the
            event that there is no interest rate for the passed arguments,
            returns ``None``.

Examples
^^^^^^^^

.. code:: pycon

    >>> import task_02
    >>> task_02.get_interest_rate(100000, 15, True)
    Decimal('0.0363')
    >>> task_02.compound_interest(100000, 15, Decimal('0.0363'))
    Decimal('172233.0130127978509806406311')
    >>> task_02.calculate_total(100000, 15, True)
    172233
    >>> task_02.calculate_interest(100000, 15, True)
    72233
    >>> task_02.calculate_total(1000000, 30, True)
    None
    >>> task_02.calculate_interest(1000000, 20, False)
    None
    
Task 03: Transforming Data
--------------------------

Python functions can be chained together to create powerful suites of
functionality. When combined with the ability to react to arguments, you can
create intelligent tools for reacting to your data.

Specifications
^^^^^^^^^^^^^^

#.  Create a file named ``task_03.py``

#.  Within ``task_03.py``, create a function named ``celsius_to_fahrenheit()``

    #.  ``celsius_to_fahrenheit()`` converts a temperature given in Celsius to
        Fahrenheit.

    #.  Takes exactly one argument, ``temperature`` which could be a number
        of any type.

    #.  Uses the following equation to calculate the temperature:
    
        .. code::

                9C     
            F = -- + 32
                 5     
            
            C is the temperature in Celsius
            F is the temperature in Fahrenheit 

    #.  Returns a ``float`` of the temperature converted to Fahrenheit.

#.  Within ``task_03.py``, create a function named ``fahrenheit_to_celsius()``

    #.  ``fahrenheit_to_celsius()`` converts a temperature given in Fahrenheit
        to Celsius.

    #.  Takes exactly one argument, ``temperature`` which could be a number
        of any type.

    #.  Uses the following equation to calculate the temperature:
    
        .. code::

                5(F - 32)
            C = ---------
                    9  
            
            C is the temperature in Celsius
            F is the temperature in Fahrenheit

    #.  Returns a ``float`` of the temperature converted to Celsius.

#.  Within ``task_03.py`` create a function named ``convert_temperature()``

    #.  ``convert_temperature()`` detects the type of temperature it is passed
        and outputs it as the specified output type.

    #.  Takes exactly two arguments:

        #.  ``temperature`` a string in the format of ``35C`` or ``45F`` with
            the Celsius or Fahrenheit symbol.

        #.  ``output_format`` a string that accepts either ``'c'`` or ``'f'``
            as valid input. This defaults to ``'c'``.

    #.  Returns a *numeric* type of the temperature in the selected output
        format.

    #.  If ``output_format`` is ``'c'``, the incoming temperature should be
        output as Celsius. If ``output_format`` is ``'f'``, the incoming
        temperature should be output as Fahrenheit.

    #.  ``convert_temperature()`` should use the previous two functions to
        accomplish its respective conversions.

    #.  If passed an incorrect ``output_format`` or ``temperature``, it should
        return ``None``

Examples
^^^^^^^^

.. code:: pycon

    >>> import task_03
    >>> task_03.celsius_to_fahrenheit(42)
    107
    >>> task_03.fahrenheit_to_celsius(42)
    5
    >>> task_03.convert_temperature('42F', 'c')
    5.555555555555555
    >>> task_03.convert_temperature('107.6F', 'f')
    107.6
    >>> task_03.convert_temperature('42C')
    42.0
    >>> task_03.convert_temperature('42C', 'f')
    107.6
    >>> task_03.convert_temperature('42C', 'p')
    None
    >>> task_03.convert_temperature(42)
    None

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
