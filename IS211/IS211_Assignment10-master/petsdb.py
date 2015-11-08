#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""is211 Assignment 10"""

import sqlite3

conn = sqlite3.connect('pets.db')
c = conn.cursor()


def creatingtables():
    c.execute("CREATE TABLE person(id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, age INTEGER)")
    c.execute("CREATE TABLE pet(id INTEGER PRIMARY KEY , name TEXT, breed TEXT, age INTEGER, dead INTEGER)")
    c.execute("CREATE TABLE person_pet(person_id INTEGER, pet_id INTEGEr)")


creatingtables()

