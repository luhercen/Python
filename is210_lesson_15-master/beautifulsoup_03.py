#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Task 03 """

import urllib2
from bs4 import BeautifulSoup

URL = 'http://sps.cuny.edu/whoweare/departments/it'
DATA = urllib2.urlopen(URL).read()
SOUP = BeautifulSoup(DATA)


def sps_it_department():
    """ funct it departm using SOUP """

    retlist = []
    doc = SOUP.find(id='membersView')
    names = doc.findAll('span', {'class': 'name bold'})
    email = doc.select('a[href^=mailto]')
    for i, item in enumerate(names):
        spl = item.text.strip().split(',')
        dictentry = {
            'email': email[i].text,
            'first_name': spl[1].strip(),
            'last_name': spl[0].strip(),
        }
        retlist.append(dictentry)
    return retlist
