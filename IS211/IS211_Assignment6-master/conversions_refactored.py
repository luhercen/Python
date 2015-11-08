#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""is211 Assignment 6 """


class ConversionNotPossible(Exception):
    pass


def convert(fromUnit, toUnit, value):
    """ conversion equivalances from web """

    lenght_conversions = {
        'miles': 0.000621371,
        'yards': 1.09361,
        'meters': 1.0}


    temperature_conversions = {
        'celsius': (1.0, 0),
        'fahrenheit': (1.8, 32),
        'kelvin': (1.0, 273.15)}


    fromUnit = fromUnit.lower()
    toUnit = toUnit.lower()

    try:
        value = float(value)
    except ValueError:
        raise ValueError("Make sure you enter a float")



    if fromUnit in lenght_conversions and toUnit in lenght_conversions:
        ope1 = lenght_conversions[fromUnit]
        ope2 = lenght_conversions[toUnit]

        return value * (1/ope1) * ope2

    elif fromUnit in temperature_conversions and toUnit in temperature_conversions:
        ope1 = temperature_conversions[fromUnit][0]
        ope2 = temperature_conversions[fromUnit][1]
        ope3 = temperature_conversions[toUnit][0]
        ope4 = temperature_conversions[toUnit][1]

        return (value - ope2) * ope3 / ope1 + ope4

    checking = ((fromUnit in lenght_conversions) and (toUnit in lenght_conversions)) \
    or ((fromUnit in temperature_conversions) and (toUnit in temperature_conversions))

    if not checking:
        raise ConversionNotPossible("Its not possible to make this conversion")
