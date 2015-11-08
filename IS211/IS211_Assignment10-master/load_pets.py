#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""is211 Assignment 10"""

import sqlite3

conn = sqlite3.connect('pets.db')
c = conn.cursor()

def dataentry():
    c.execute("INSERT INTO person VALUES(1, 'James', 'Smith', 41)")
    c.execute("INSERT INTO person VALUES(2, 'Diana', 'Greene', 23)")
    c.execute("INSERT INTO person VALUES(3, 'Sara', 'White', 27)")
    c.execute("INSERT INTO person VALUES(4, 'William', 'Gibson', 23)")

    c.execute("INSERT INTO pet VALUES(1, 'Rusty', 'Dalmation', 4, 1)")
    c.execute("INSERT INTO pet VALUES(2, 'Bella', 'Alaskan Malamute', 3, 0)")
    c.execute("INSERT INTO pet VALUES(3, 'Max', 'Cocker Spaniel', 1, 0)")
    c.execute("INSERT INTO pet VALUES(4, 'Rocky', 'Beagle', 7, 0)")
    c.execute("INSERT INTO pet VALUES(5, 'Rufus', 'Cocker Spaniel', 1, 0)")
    c.execute("INSERT INTO pet VALUES(6, 'Spot', 'Bloodhound', 2, 1)")

    c.execute("INSERT INTO person_pet VALUES(1, 1)")
    c.execute("INSERT INTO person_pet VALUES(1, 2)")
    c.execute("INSERT INTO person_pet VALUES(2, 3)")
    c.execute("INSERT INTO person_pet VALUES(2, 4)")
    c.execute("INSERT INTO person_pet VALUES(3, 5)")
    c.execute("INSERT INTO person_pet VALUES(4, 6)")
    conn.commit()

dataentry()
