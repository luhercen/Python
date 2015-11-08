#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""is211 Assignment 6 """


from conversions import *
import unittest


class CelsiusToKelvin(unittest.TestCase):

    def test_positiveval(self):
        self.assertEqual(convertCelsiusToKelvin(300.0), 573.15)

    def test_zerocelval(self):
        self.assertEqual(convertCelsiusToKelvin(0.0), 273.15)

    def test_decimalval(self):
        self.assertEqual(convertCelsiusToKelvin(100.22), 373.37)

    def test_largeval(self):
        self.assertEqual(convertCelsiusToKelvin(848484), 848757.15)

    def test_negaval(self):
        self.assertEqual(convertCelsiusToKelvin(-100.0), 173.15)


class CelsiusToFahrenhiet(unittest.TestCase):

    def test_positiveval(self):
        self.assertEqual(convertCelsiusToKelvin(300.0), 573.15)

    def test_zerocelval(self):
        self.assertEqual(convertCelsiusToKelvin(0.0), 273.15)

    def test_decimalval(self):
        self.assertEqual(convertCelsiusToKelvin(100.22), 373.37)

    def test_largeval(self):
        self.assertEqual(convertCelsiusToKelvin(848484), 848757.15)

    def test_negaval(self):
        self.assertEqual(convertCelsiusToKelvin(-100.0), 173.15)


class FahrenheitToCelsius(unittest.TestCase):

    def test_positiveval(self):
        self.assertEqual(convertCelsiusToKelvin(300.0), 573.15)

    def test_zerocelval(self):
        self.assertEqual(convertCelsiusToKelvin(0.0), 273.15)

    def test_decimalval(self):
        self.assertEqual(convertCelsiusToKelvin(100.22), 373.37)

    def test_largeval(self):
        self.assertEqual(convertCelsiusToKelvin(848484), 848757.15)

    def test_negaval(self):
        self.assertEqual(convertCelsiusToKelvin(-100.0), 173.15)


class FahrenheitToKelvin(unittest.TestCase):

    def test_positiveval(self):
        self.assertEqual(convertCelsiusToKelvin(300.0), 573.15)

    def test_zerocelval(self):
        self.assertEqual(convertCelsiusToKelvin(0.0), 273.15)

    def test_decimalval(self):
        self.assertEqual(convertCelsiusToKelvin(100.22), 373.37)

    def test_largeval(self):
        self.assertEqual(convertCelsiusToKelvin(848484), 848757.15)

    def test_negaval(self):
        self.assertEqual(convertCelsiusToKelvin(-100.0), 173.15)


class KelvinToCelsius(unittest.TestCase):

    def test_positiveval(self):
        self.assertEqual(convertCelsiusToKelvin(300.0), 573.15)

    def test_zerocelval(self):
        self.assertEqual(convertCelsiusToKelvin(0.0), 273.15)

    def test_decimalval(self):
        self.assertEqual(convertCelsiusToKelvin(100.22), 373.37)

    def test_largeval(self):
        self.assertEqual(convertCelsiusToKelvin(848484), 848757.15)

    def test_negaval(self):
        self.assertEqual(convertCelsiusToKelvin(-100.0), 173.15)


class KelvinToFarenheit(unittest.TestCase):

    def test_positiveval(self):
        self.assertEqual(convertCelsiusToKelvin(300.0), 573.15)

    def test_zerocelval(self):
        self.assertEqual(convertCelsiusToKelvin(0.0), 273.15)

    def test_decimalval(self):
        self.assertEqual(convertCelsiusToKelvin(100.22), 373.37)

    def test_largeval(self):
        self.assertEqual(convertCelsiusToKelvin(848484), 848757.15)

    def test_negaval(self):
        self.assertEqual(convertCelsiusToKelvin(-100.0), 173.15)


if __name__ == "__main__":
    unittest.main()
