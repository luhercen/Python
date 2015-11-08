#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""is211 Assignment 10"""

import sqlite3
import sys

conn = sqlite3.connect('pets.db')
c = conn.cursor()

sql = "SELECT * FROM person where id =?"

def readData():

    try:
        personid = raw_input("Enter User Id(for exit type -1):")
        c.execute(("SELECT * FROM Person WHERE id=%s"  % (personid)))
        checker = c.fetchone()

        if personid == '-1':
            print "bye"
            sys.exit

        elif checker == None:
                  print "id not found"
                  
        else:
            for row in c.execute(sql, [personid]):
                print row

	    
    except sqlite3.Error as e:
        print "Connection error, closing."
        sys.exit(1)


readData()
