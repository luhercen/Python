#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""is211 Assignment 6 """


def convertCelsiusToKelvin(celsiusinput=float):
    
    try:
        solution = celsiusinput + 273.15
        
    except TypeError:
        raise TypeError('Make sure your input is a float ')
    return round(solution, 2)


def convertCelsiusToFahrenheit(celsiusinput=float):
    
    try:
        solution = celsiusinput * (9.0/5.0) + 32.0
    except TypeError:
        raise TypeError('Make sure your input is a float ')
    return round(solution, 2)



def convertFahrenheitToCelsius(fahreinput=float):

    try:
        solution = (fahreinput - 32.0) * (5.0/9.0)
    except TypeError:
        raise TypeError('Make sure your input is a float ')
    return round(solution, 2)



def convertFahrenheitToKelvin(fahreinput=float):

    try:
        solution = (fahreinput + 459.67) * (5.0/9.0)
    except TypeError:
        raise TypeError('Make sure your input is a float ')
    return round(solution, 2)



def convertKelvinToCelsius(kelinput=float):

    try:
        solution = kelinput - 273.15
    except TypeError:
        raise TypeError('Make sure your input is a float ')
    return round(solution, 2)



def convertKelvintoFahrenheit(kelinput=float):
    
    try:
        solution = kelinput * (9.0/5.0) - 459.76
    except TypeError:
        raise TypeError('Make sure your input is a float ')
    return round(solution, 2)
