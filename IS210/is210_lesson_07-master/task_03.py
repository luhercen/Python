#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""task03"""


import data

CORRECTED = data.BANDS.copy()
CORRECTED['Dylan'] = {'Bob Dylan': ['vocals', 'guitar', 'harmonica']}
del CORRECTED['Van Halen']['David Lee Roth']
CORRECTED['Van Halen']['Sammy Hagar'] = ['vocals']
