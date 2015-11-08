#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Task 05 """

from decimal import Decimal

NAME = raw_input("Enter your Name :")
P = int(raw_input("Enter the initial amount you borrowed or deposited :"))
Y = int(raw_input("How many years is this loan being borrowed ? :"))
Q = raw_input("Are you pre-qualified for this loan ? : ")
I = 0

"""this is I for Interest, initializing I """

if P <= 199999:
   if 1 <= Y < 15:
        if Q == "YES":
            I = Decimal('0.0363')
        elif Q == "NO":
            I = Decimal('0.0465')
        else:
            I = Decimal('0.0')
   elif 15 <= Y < 20:
        if Q == "YES":
            I = Decimal('0.0404')
        elif Q == "NO":
            I = Decimal('0.0498')
        else:
            I = Decimal('0.0')
   elif 20 <= Y <= 30:
        if Q == "YES":
            I = Decimal('0.0577')
        elif Q == "NO":
            I = Decimal('0.0639')
        else:
            I = Decimal('0.0')
elif 200000 <= P <= 999999:
    if 1 <= Y < 15:
        if Q == "YES":
            I = Decimal('0.0302')
    elif Q == "NO":
            I = Decimal('0.0398')
        else:
            I = Decimal('0.0')
    elif 15 <= Y < 20:
        if Q == "YES":
            I = Decimal('0.0327')
        elif Q == "NO":
            I = Decimal('0.0408')
        else:
            I = Decimal('0.0')
    elif 20 <= Y <= 30 and Q  == "YES":
        I = Decimal('0.0466')
    else:
        I = Decimal('0.0')
elif P >= 1000000:
    if 1 <= Y < 15 and Q == "YES":
        I = Decimal('0.0205')
    elif 15 <= Y <= 20 and Q == "YES":
        I = Decimal('0.0262')
    else:
        I = Decimal('0.0')


TOTAL = round(P*(1+(I/1))**Y)

REPORT = (
    'Loan Report for: {0}'
    '\n{1}'
    '\n\Principal: ${2:0,.0f}'
    '\n\Duration: {3}yrs'
    '\n\Pre-Qualified?: {4}'
    '\n\n\Total: '
    '${5:0,0f}').format(NAME, '-' , P, Y, Q, TOTAL)

print REPORT
