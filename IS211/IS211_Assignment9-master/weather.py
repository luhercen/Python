#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""is211 Assignment 9"""


import urllib2
from bs4 import BeautifulSoup

url = 'http://www.wunderground.com/history/airport/KNYC/2015/3/1/MonthlyCalendar.html'
web = urllib2.urlopen(url)
soup = BeautifulSoup(web.read())


def weathercatch():
    data = []
    searcher = soup.find_all('table' , class_={'dayTable'})

    dayfo = None

    for x in searcher:
        if dayfo == None:
            dayfo = x.find('a', class_='dateText').text.strip()
            
        header = x.find('td', class_='value-header', text=['Actual:', 'Forecast:'])
        if header != None:
            high = x.find('span', class_='high').text
            low = x.find('span', class_='low').text
            data.append({'date': dayfo, 'header': header.text,'high': high,'low': low})

        print data
            
weathercatch()
