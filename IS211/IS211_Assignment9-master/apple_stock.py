#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""is211 Assignment 9"""


import urllib2
from bs4 import BeautifulSoup

url = 'http://finance.yahoo.com/q/hp?s=AAPL+Historical+Prices'
web = urllib2.urlopen(url)
soup = BeautifulSoup(web.read())

def appleinfo():
    data = []
    searcher = soup.findAll('tr')

    for x in searcher:
        try:
            if len(x.findAll(('td', {'class': 'yfnc_tabledata1'}))) == 7:
                date = x.contents[0].get_text()
                close = x.contents[6].get_text()
                data.append((date, close))
        except:
            print "corrupt info"
            continue

    print data

appleinfo()
