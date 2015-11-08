#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" assignment 2 part 2"""


class Book(object):
    """ class """
    
    author = ""
    title = ""

    def __init__(self, author, title):
        self.author = author
        self.title = title

    def display(self):
        print "{}, written by {}".format(self.title, self.author)

if __name__ == "__main__":
    Book1 = Book('John Steinbeck', 'Of Mice and Men')
    Book2 = Book('Harper Lee', 'To Kill a Mockingbird')

    Book1.display()
    Book2.display()
