==========================================
IS 210: Software Application Programming I
==========================================
------------
Homework #08
------------

:College: CUNY School of Professional Studies
:Course-Name: Software Application Programming I
:Course-Code: IS 210
:Available: 2014-10-14T09:00:00-0400
:Due-Date: 2014-10-20T09:00:00-0400

Overview
========

The following tasks will either have you interacting with existing files in
the starter repo or creating new ones on the fly. Don't forget to add your
interpreter directive, utf-8 encoding, and a short docstring with any new files
that you create!

Warmup Tasks
============

Task 01: Creating and Accessing Instances
-----------------------------------------

You've already instantiated and used some classes already if you consider
your prior use of such classes like the ``Decimal()`` class. Here you'll be
instantiating and accessing custom class instances.

Specifications
^^^^^^^^^^^^^^

#.  Create a file named ``task_01.py``. In ``task_01.py``:

#.  Import ``data``

#.  Create two instances of the ``Produce()`` class

    #.  The first should not be passed any constructor variables and should be
        assigned to a variable named ``TOMATO``

    #.  The next should be named ``EGGPLANT`` and the constructor should be
        passed the value of ``1311210802``

#.  Access the ``arrival`` attribute of ``TOMATO`` and save it to a variable
    named ``TOMATO_ARRIVAL``

#.  Call the ``get_expiration()`` method of ``EGGPLANT`` and save its result
    to a variable named, ``EGGPLANT_EXPIRES``

Task 02: Modify a Class
-----------------------

Here we'll be making some minor changes to existing classes.

Specifications
^^^^^^^^^^^^^^

#.  Open ``task_02.py``.

#.  Add an additional argument named, ``tires`` to the ``Car()`` constructor

    #.  The default of this argument should be ``None``

#.  Add a new *instance attribute* to ``Car()`` called ``tires`` to store a
    list of tires

    #.  Assign the new instance attribute the value of the ``tires`` argument

    #.  If the value of the ``tires`` argument is ``None``:

        #.  Create a list

        #.  Create four new instances of the ``Tire()`` class and append each
            into the list

#.  Add a pseudo-private *class attribute* to the ``Tires()`` class called
    ``__maximum_miles`` and assign it a value of ``500``.

#.  Test that your ``Car()`` class works with both a ``tires`` argument and
    without.

.. note::

    You will have to modify the documentation because of the changes you've
    made.

Task 03: Create a Simple Class
------------------------------

In this task you'll be creating your own class from the ground-up.

Specifications
^^^^^^^^^^^^^^

#.  Create a new file named ``task_03.py``. In ``task_03.py``:

#.  Import the ``time`` module. This module provides functions specifically
    related to time. We'll use it for its ``time()`` function which returns a
    `Unix Timestamp`_ 

#.  Create a class named ``Snapshot``

#.  Create a constructor for ``Snapshot``

#.  In the constructor, create an *instance attribute* named ``created`` and
    assign it the output of ``time.time()`` which returns the current
    `Unix Timestamp`_

.. tip::

    Classes without an explicit parent class should always be subclassed to the
    generic ``object`` class.

Task 04: Subclassing
--------------------

Subclasses are part of the heart and soul of object-oriented programming. Here,
we'll be subclassing our tires class.

Specifications
^^^^^^^^^^^^^^

#.  Create a new file named ``task_04.py``. In ``task_04.py``:

#.  Import ``task_02``

#.  Create a new class called ``Tigerpaw()`` subclassed to ``task_02.Tire()``

#.  Override the ``__maximum_miles`` class attribute of ``Tigerpaw()`` and
    set it to ``750``.

#.  Try using the new ``Tigerpaw()`` class in conjunction with
    ``task_02.Car()``

The Chessboard
==============

The next three tasks will have you implementing a chess move tracker. You don't
have to know how to play chess to implement this particular solution but it
does help to familiarize yourself with what's known as *Algebraic Notation* and
how it's represented on the grid of a chessboard. For a visual cue, see:

https://en.wikipedia.org/wiki/Algebraic_notation_%28chess%29

You'll want to quickly scan the naming convention for both squares and pieces
to help contextualize the assignment.

Task 05: The Chess Piece
------------------------

To start our conceptualization, we need a generic chess piece that will provide
reusable code and storage for our various *types* of chess pieces.

In chess, each type of piece has a set of allowable moves. For example, bishops
can move diagonally in any direction but not straight across a row or a column
(or ranks and files for the chess fans). While the types of allowable moves
may differ the fact that a move itself is happening and how it happens is
shared amongst all pieces.

We want all of our chess pieces to:

#.  Know their current position on the board

#.  Have a history of all of their prior moves

#.  Be capable of making new moves and recording that history

#.  Disallowing incorrect moves (such as a move off the board)

Since this is shared functionality, we can effectively split our chess pieces
into two classes: a generic class that controls the shared elements and a
specific type-class that controls allowable moves.


.. note::

    For true aficionados, some of our notation and logging will be non-standard
    or leave out crucial elements such as capture or blocking pieces. The goal
    here is as an educational exercise so we've kept it simple. You're welcome
    to expand it, however, to account for the additional rules. Game rules
    make for remarkably interesting learning tools.

Specifications
^^^^^^^^^^^^^^

#.  Begin by creating a file called ``chessmaster.py``. In ``chessmaster.py``:

#.  Create a new class called ``ChessPiece``

#.  Import the ``time`` module again.

#.  ``ChessPiece`` has a required argument at construction called ``position``
    which effectively represents its starting position. This should be assigned
    to the ``position`` instance attribute at instantiation.

#.  ``ChessPiece`` has one class attribute:

    #.  ``prefix`` which is, by default, set as an empty string

#.  ``ChessPiece`` has two instance attributes:

    #.  ``position`` stores the tile notation of its current position (eg,
        ``'a8'``.

    #.  ``moves`` is a list that stores tuples of information about each move
        this pieces has taken. See the examples section for a demonstration of
        the expected data format.

#.  Create a class function called ``algebraic_to_numeric()`` that takes a
    single string argument, ``tile``, and converts it to a tuple with two
    values, a 0-based y-coordinate and a 0-based x-coordinate. This conversion
    will help us determine legal moves for our chess pieces. This function
    should be capable of taking ``'a1'`` and returning ``(0,0)`` and similarly
    converting ``'g8'`` to ``(6,7)``. How you choose to convert the alpha
    character is up-to-you. This function should return ``None`` if an invalid
    coordinate is passed (eg, a letter or number that would be considered
    out of the bounds of the board).

#.  Create a new function called ``is_legal_move()`` to test if the suggested
    move is a legal one.

    #.  This function takes one argument, ``position`` which represents the
        algebraic notation of the new position to which this piece should be
        moved.

    #.  Test to see if ``position`` is legal by converting it to a numeric
        form with ``algebraic_to_numeric()``.

    #.  Return ``True`` if the move is legal and ``False`` if it is not

#.  Add an ``is_legal_move()`` test for ``position`` in the constructor to
    ensure that starting position is legal and on the board. If it is not legal
    use the following snippet to raise an exception:

    .. code:: python

        excep = '`{}` is not a legal start position'
        raise ValueError(excep.format(position))

    *We will be covering exceptions in much greater detail in a few lessons.*

#.  Create a function called ``move()`` to actually move our piece.

    #.  This function takes one argument, ``position`` which represents the
        algebraic notation of the new position to which this piece should be
        moved.

    #.  Test to see if ``position`` is legal by calling ``is_legal_move()``.
    
    #.  If it is legal:

        #.  Change the value of the ``position`` attribute to the new
            ``position`` argument value

        #.  Append a new entry to the ``moves`` list attribute as follows:

            #.  Each moves entry is a tuple:

                .. code:: python

                    (oldposition, newposition, timestamp)

            #.  Before saving the moves in the tuple,  prepend the ``prefix``
                class attribute to the two positions

        #.  Return the above tuple

    #.  If it is not legal, return ``False``

Examples
--------

Note that the timestamp below will change.

.. code:: pycon

    >>> piece = ChessPiece('j9')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: `j9` is not a valid start position
    >>> piece = ChessPiece('a1')
    >>> piece.position
    'a1'
    >>> piece.moves
    []
    >>> piece.algebraic_to_numeric('e7')
    (4,6)
    >>> piece.algebraic_to_numeric('j9')
    None
    >>> piece.move('j9')
    False
    >>> piece.move('e7')
    ('a1', 'e7', 1413252815.610075)
    >>> piece.position
    'e7'
    >>> piece.moves
    [('a1', 'e7', 1413252815.610075)]
    >>> piece.move('b2')
    ('e7', 'b2', 1413252817.89340)
    >>> piece.moves
    [('a1', 'e7', 1413252815.610075), ('e7', 'b2', 1413252817.89340)]

Task 06: Specific Pieces
------------------------

Now that we've set up the general and shared rules of our chess pieces, let's
create new classes for our specific types of chess pieces. Each of these should
be created in ``chessmaster.py``.

Specifications
^^^^^^^^^^^^^^

#.  We'll start with rooks because they're quite straightforward, literally.

    #.  Rooks may move any number of squares along the x-axis (the ranks/rows)
        or the y-axis (the files/columns) however, they cannot move along both
        axes simultaneously. Mathematically this means that a rook at ``(0,0)``
        can move to either ``(3,0)`` or ``(0, 1)`` but not ``(1,1)`` in a
        single ``move()``

    #.  Create a new class called ``Rook`` that subclasses ``ChessPiece``.

    #.  Override the ``prefix`` class attribute and give it a value of ``R``.

    #.  Override ``is_legal_move()`` to reflect the additional restrictions on
        rook movement.

.. warning::

    In the original class, ``is_legal_move()`` only checks that the piece is on
    the gameboard at all. The additional logic imposed by the changes proposed
    above would cause ``is_legal_move()`` to not work within the context of the
    constructor and the starting position. Without copying any logic or code,
    how can you solve this dilemma without repeating yourself? There are at
    least two acceptable solutions one of which involves using a class function
    call in the constructor instead of an instance function call.

#.  Next, we'll create a class for the rook's polar opposite, the bishop. Where
    a rook may only move along in straight lines, a bishop may move any number
    of squares in a diagonal line. Numerically, it means that both axes must
    increment or decrement in equal amounts, eg ``(4,5)`` may move to ``(2,3)``
    or ``(5,6)`` but not ``(5,7)``.

    #.  Create a new class called ``Bishop`` that subclasses ``ChessPiece``

    #.  Override the ``prefix`` class attribute and give it a value of ``B``.

    #.  Override ``is_legal_move()`` to reflect the additional restrictions on
        bishop movement.

#.  Finally, we'll create a class for the king. A king can move in any
    direction, straight or diagonal, but may only do so one space at a time.

    #.  Create a new class called ``King`` that subclasses ``ChessPiece``
    
    #.  Override the ``prefix`` class attribute and give it a value of ``K``.

    #.  Override ``is_legal_move()`` to reflect the additional restrictions on
        king movement.

Examples
^^^^^^^^

Note that the timestamps below will change.

.. code:: pycon

    >>> rook = Rook('a1')
    >>> rook.prefix
    'R'
    >>> rook.move('b2')
    False
    >>> rook.move('h1')
    ('Ra1', 'Rh1', 1413252817.89340)
    >>> rook.move('h8')
    ('Rh1', 'Rh8', 1413252818.89340)

    >>> bishop = Bishop('a1')
    >>> bishop.prefix
    'B'
    >>> bishop.move('a2')
    False
    >>> bishop.move('c3')
    ('Ba1', 'Bc1', 1413252817.89340)
    >>> bishop.move('a5')
    ('Bc3', 'Ba5', 1413252818.89340)

    >>> king = King('a1')
    >>> king.prefix
    'K'
    >>> king.move('a3')
    False
    >>> king.move('b1')
    ('Ka1', 'Kb1', 1413252817.89340)
    >>> king.move('a2')
    ('Kb1', 'Ka2', 1413252818.89340)

Task 07: The Match Class
------------------------

Now that we have our pieces, let's put it all together into a class that both
functions as our gameboard and tracks our moves.

Specifications
^^^^^^^^^^^^^^

#.  Still in ``chessmaster.py``, create a class called ``ChessMatch``

#.  Create a constructor that takes one argument, ``pieces``, a dictionary of
    pieces keyed by their positions on the board. The default of the ``pieces``
    argument is ``None``. If ``pieces`` is ``None`` call the ``reset()``
    method.
    
    If ``pieces`` is not ``None``:
    
    #.  Set the ``pieces`` instance attribute to the value of the
        ``pieces`` argument.

    #.  Create a new instance attribute called ``log`` and set its value as an
        empty list.

#.  Create a method called ``reset()`` that resets the match log to an
    empty list and places our pieces back at their starting positions. The
    starting positions are as follows:

    .. table:: Starting Positions

        ======== =========== =============
        Position Type        Full Notation
        ======== =========== =============
        a1       Rook        Ra1
        h1       Rook        Rh1
        a8       Rook        Ra8
        h8       Rook        Rh8
        c1       Bishop      Bc1
        f1       Bishop      Bf1
        c8       Bishop      Bc8
        f8       Bishop      Bf8
        e1       King        Ke1
        e8       King        Ke8
        ======== =========== =============


    Piece objects will be stored inside the ``pieces`` instance attribute in
    a dictionary. The current position of each piece in *Full Notation* is the
    key. The instance of that piece's class is the value.

#.  Create a function called ``move()``.

    #.  Accepts two arguments:

        #.  The name of the piece in *Full Notation*

        #.  The destination coordinate in short notation (eg, 'a7').

    #.  Calls the specified piece's ``move()`` method to move it to a
        new position.

        If the move is successful, it saves the resulting tuple as a new
        entry in the ``log`` attribute and re-keys the object in the ``pieces``
        attribute. (See the tip below on how to do this easily). Don't forget
        the ``prefix`` attribute of your pieces which can be used to
        reconstruct the new destination coordinate.

    #.  If a piece is unable to move to the coordinate, it returns ``False``

#.  Implement a Python magic method that will allow the ``ChessMatch`` class
    to be called inside ``len()`` and return the number of log items. See
    http://www.rafekettler.com/magicmethods.html for more details.

.. tip::

    Rekeying is not something that is often necessary in Python but it does,
    on occasion, have its uses. While you could try creating a new entry and
    using the ``del`` statement, a more elegant solution is to ``pop()`` the
    original entry off (thus deleting its key), and assigning it back in, eg
    ``foo['bar'] = foo.pop('baz')``

.. note::

    Those who have paid attention to the DRY principle might wonder if the
    fact that we're storing the log of each piece in both ``ChessMatch``
    and ``ChessPiece`` is legal in the context of our best practices. In this
    case, absolutely, yes! We're able to take advantage of a neat trick in
    that the tuple returned by the piece's ``move()`` call is the exact same
    object being stored in our log in ``ChessMatch``. Since it's a tuple it
    can't change, but even if it could, it's being stored by reference so no
    data is duplicated in memory. We're always guaranteed that the data is
    in-sync in both locations.

Examples
^^^^^^^^

.. code:: pycon

    >>> white = King('e1')
    >>> black = King('e8')
    >>> match = ChessMatch({'Ke1': white, 'Ke8': black})
    >>> match.log
    []
    >>> match.move('Ke1', 'e2')
    >>> match.pieces
    {'Ke2': <__main__.King object at 0x70000000000>, 'Ke8':
    <__main__.King object at 0x7000000000a>}
    >>> match.log
    [('Ke1', 'Ke2', 1413252817.89340)]
    >>> len(match)
    1
    >>> match.reset()
    >>> len(match)
    0
    >>> len(match.pieces)
    10
    >>> match2 = ChessMatch()
    >>> len(match.pieces)
    10

Extra Credit
============

This week has a fun extra credit exercise. Create additional piece type
subclasses for four points of extra credit each. The pieces must take all
non-capture movement rules into play including the pawn's first-move advantage
and the additional types must be represented in the ``reset()`` method of
``ChessMatch``

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
.. _Unix Timestamp: https://en.wikipedia.org/wiki/Unix_time
