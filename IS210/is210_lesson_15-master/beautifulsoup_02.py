#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Task 02 """


import urllib2
from bs4 import BeautifulSoup

URL = 'http://www.whitehouse.gov/net-neutrality'
DATA = urllib2.urlopen(URL).read()
HTML_SOUP = BeautifulSoup(DATA)


def obama_net_neutrality():
    """ obama neutrality """

    tag = HTML_SOUP.find('p', {'class': 'intro-paragraph'})
    return tag.text
