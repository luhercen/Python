#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""is211 Assignment 9"""


import urllib2
from bs4 import BeautifulSoup

url = 'http://www.cbssports.com/nfl/stats/playersort/nfl/year-2014-season-regular-category-touchdowns'
web = urllib2.urlopen(url)
soup = BeautifulSoup(web.read())


def footballstats():
    data = []
    searcher = soup.find_all(class_={'row1', 'row2'})

    for x in searcher[:20]:
        try:
            pname = x.contents[0].get_text()
            pposition = x.contents[1].get_text()
            ptouchs = x.contents[6].get_text()
            pteam = x.contents[2].get_text()
            data.append((pname, pposition, ptouchs, pteam))

        except:
            print "corrupt info"
            continue
    print data

footballstats()
