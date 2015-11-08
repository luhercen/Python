#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Task03"""


def celsius_to_fahrenheit(temperature):
    """this will convert from C to F"""
    fahrenheit = (temperature * 9) / 5 + 32
    return float(fahrenheit)


def fahrenheit_to_celsius(temperature):
    """this will convert from F to C"""
    celsius = 5 * (temperature - 32) / 9
    return float(celsius)


def convert_temperature(temperature, output_format='c'):
    """this will show the converted temperature"""

    temp = None

    if (type(temperature) is not str) or (type(output_format) is not str):
        return None

    if temperature[-1] in ['F', 'C']:
        check = temperature[-1]
        temp = float(temperature[0:-1])

    if temp is not None:
        if output_format in ['f', 'c']:
            if output_format == 'f' and check == 'C':
                temp = celsius_to_fahrenheit(temp)
            elif output_format == 'c' and check == 'F':
                temp = fahrenheit_to_celsius(temp)
        else:
            temp = None
    return temp
