#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Lesson 11, current_weather file"""

import urllib2
import json
import csv
import os
from decimal import Decimal as Dec


class CurrentWeatherException(Exception):
    """weather exeption"""
    def __init__(self, code, message):
        super(CurrentWeatherException, self).__init__(self, message)
        self.errno = code
        self.message = message


class CurrentWeather(object):
    """ class weather"""
    zip_codes = {}
    base_url = 'http://api.openweathermap.org/data/2.5/weather'

    def __init__(self, zipcode_data='zipcode_database.csv'):
        self.read_csv(zipcode_data)

    def get_weather(self, city, country, units='metric'):
        """weather get"""
        api_query = '{}?units={}&q={},{}'.format(
            self.base_url, units, city, country
        )

        try:
            response = urllib2.urlopen(api_query)

            return json.load(response)['main']
        except urllib2.HTTPError, error:
            raise CurrentWeatherException(
                error.code, 'Error: {} {}'.format(error.code, error.msg))

    def read_csv(self, csv_path):
        """file reader"""
        if os.path.exists(csv_path):

            try:
                input_file = open(csv_path, 'r')

                file_in = csv.reader(input_file)

                for row in file_in:
                    if row[0] == 'zipcode':
                        continue
                    else:
                        self.zip_codes[row[0]] = {'city': row[1],
                                                  'state': row[2],
                                                  'latitude': Dec(row[3]),
                                                  'longitude': Dec(row[4]),
                                                  'country': row[5]}
            except IOError:
                raise
            finally:
                input_file.close()
        else:
            raise CurrentWeatherException(
                9010, 'CSV zipcode database {} not found'.format(csv_path))

    def get_city_by_zipcode(self, zipcode):
        """this gets city by zip"""
        if zipcode not in self.zip_codes:
            raise CurrentWeatherException(
                5150, 'Error: Zipcode not found in Zipcode data')
        else:
            return self.zip_codes[zipcode]['city']

    def get_weather_by_zipcode(self, zipcode):
        """weather by zip"""
        city = self.get_city_by_zipcode(zipcode)
        return self.get_weather(city, 'US')
