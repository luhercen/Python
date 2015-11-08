#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Task 03 """

BASE = raw_input(
    "Choose between 2 colors : "
    "Seattle Gray Or Manatee : ")

if BASE == "Seattle Gray":
    ACCENT = raw_input("Ceramic Glaze or Cumulus Nimbus : ")
if ACCENT == "Ceramic Glaze":
    HIGHLIGHT = raw_input("Basically White or White : ")
elif ACCENT == "Cumulus Nimbus":
    HIGHLIGHT = raw_input("Off-White or Paper White : ")
elif BASE == "Manatee":
    ACCENT = raw_input("Platinium Mist or Spartan Sage : ")
if ACCENT == "Platinium Mist":
    HIGHLIGHT = raw_input("Bonne white or Just White : ")
elif ACCENT == "Spartan Sage":
    HIGHLIGHT = raw_input("Fractal White or Not White : ")

print(
    'For you selected base color {0}, your accent color is {1},'
    'and your highlight color is {2}.').format(BASE, ACCENT, HIGHLIGHT)
