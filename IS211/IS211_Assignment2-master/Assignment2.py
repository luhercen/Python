#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" is211 Assignment 2"""


import urllib2
import csv
import sys
import datetime
import argparse
import logging

url_parser = argparse.ArgumentParser()
url_parser.add_argument("--url", help='enter URL to CSV file', type=str)
args = url_parser.parse_args()
logging.basicConfig(filename='errors.log',level=logging.ERROR)
logger = logging.getLogger('assignment2')
	

def downloadData(url):
        data = urllib2.urlopen(url)
        return data

def processData(data):
	dictionary = csv.reader(data)
	keys = dictionary.next()
	dateformat = '%d/%m/%Y'
	line_num=1
	output = {}

	dictionary = [dict(zip(keys, row)) for row in dictionary]

	for row in dictionary:
		try:
			birthday = datetime.datetime.strptime(row['birthday'], dateformat)
		except:
			logger.error('Error processing line #%s for ID #%s' % (line_num, row['id']))
			line_num+=1

		output[int(row['id'])] = (row['name'], row['birthday'])
		line_num+=1

	return output

def displayPerson(id, personData):
	try:
		dateFormat = '%d/%m/%Y'
		birthday = datetime.datetime.strptime(personData[id][1], dateFormat) 
		birthday = '%s-%02d-%02d' % (birthday.year, birthday.month, birthday.day)
		name = personData[id][0]
		print 'Person #%s is %s with a birthday of %s' % ( id, name, birthday)
	except:
		print "No user found with that id"


	

if not args.url:
    sys.exit()
else:
    try:
        loop = True
        while loop:
            csvData = downloadData(args.url)
            personData = processData(csvData)
            idpick = int(raw_input('Enter ID number: '))
            print idpick

            if idpick > 0:
                displayPerson(idpick, personData)
            else:
                print "bye"
                loop = False

    except URLError:
        sys.exit()
