#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""

import inquisition

FISHY = inquisition.SPANISH.replace('surprise', 'haddock')

LENGTH_SPANISH = len(inquisition.SPANISH)

SPANISH_INDEX = FISHY[19:26]

FLEMISH = SPANISH_INDEX.replace('Spanish', 'Flemish')

print LENGTH_SPANISH
print SPANISH_INDEX
print FLEMISH
