#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""is211 Assignment 3"""

import urllib2
import csv
import sys
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--url", help='enter URL to CSV file')
args = parser.parse_args()


def downloadData(url):
    """ takes url """
    response = urllib2.urlopen(url)
    return response

def processData(data):
    """ from csv file counts image hits and popular browser """

    csvdata = csv.reader(data)
    imagehits = 0.0
    totalhits = 0.0

    chrome = 0
    ie = 0
    firefox = 0
    safari = 0

    for row in csvdata:
        path = row[0]
        browser = row[2]
        totalhits += 1.0

        images = (re.findall(r'.gif$|.png$|.jpg$|.jpeg$', row[0], re.I | re.M))        
        if images:
            imagehits += 1.0
        else:
            continue

        fsafari = re.findall('safari/\d+', browser, re.I)
        fchrome = re.findall('chrome/\d+', browser, re.I)
        ffirefox = re.findall('firefox/\d+', browser, re.I)
        fie = re.findall('MSIE\s', browser, re.I)

        if fchrome:
            chrome += 1
        elif fie:
            ie += 1
        elif ffirefox:
            firefox += 1
        elif fsafari and not fchrome is True:
            safari += 1
        else:
            other += 1

    browsers = {'Chrome': chrome,'Safari': safari,'Internet Explorer':ie,'Firefox': firefox}
    
    hitspercentage = (imagehits/totalhits) * 100
    print "Image requests account for {0:0.1f} of all requests".format(hitspercentage)
    print "The most popular web browser today was : ", max(browsers, key=browsers.get)

if not args.url:
    print "Check url and try again"
    sys.exit()
else:
    try:
        csvData = downloadData(args.url)
        print processData(csvData)
    except urllib2.URLError:
        sys.exit()


