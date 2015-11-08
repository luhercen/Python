#!usr/bin/env python
# -*- coding: utf-8 -*-
"""Task02,Provides loan management features."""

import decimal


def get_interest_rate(principal, duration, prequalification=True):
    """to calcualte the interest rate"""
    if principal >= 0 and principal <= 199999:
        if duration >= 1 and duration <= 15:
            if prequalification:
                return decimal.Decimal('0.0363')
            else:
                return decimal.Decimal('0.0465')
        elif duration >= 16 and duration <= 20:
            if prequalification:
                return decimal.Decimal('0.0404')
            else:
                return decimal.Decimal('0.0498')
        elif duration >= 21 and duration <= 30:
            if prequalification:
                return decimal.Decimal('0.0577')
            else:
                return decimal.Decimal('0.0639')
    elif principal >= 200000 and principal <= 999999:
        if duration >= 1 and duration <= 15:
            if prequalification:
                return decimal.Decimal('0.0302')
            else:
                return decimal.Decimal('0.0398')
        elif duration >= 16 and duration <= 20:
            if prequalification:
                return decimal.Decimal('0.0327')
            else:
                return decimal.Decimal('0.0408')
        elif duration >= 21 and duration <= 30:
            if prequalification:
                return decimal.Decimal('0.0466')
    elif principal >= 1000000:
        if duration >= 1 and duration <= 15:
            if prequalification:
                return decimal.Decimal('0.0205')
        elif duration >= 16 and duration <= 20:
            if prequalification:
                return decimal.Decimal('0.0262')
    else:
        return None


def compound_interest(principal, duration, rate, interval=12):
    """
    Returns the compound interest
    """
    if rate is not None:
        rate = decimal.Decimal(rate)
        return principal * ((1 + rate / interval) ** (interval * duration))
    return None


def calculate_total(principal, duration, prequalification):
    """
    Returns the calculated total
    """
    interestrate = get_interest_rate(principal, duration, prequalification)
    if interestrate is not None:
        total = compound_interest(principal, duration, interestrate)
        return int(round(total))
    return None


def calculate_interest(principal, duration, prequalification):
    """
    Returns the calculated interest
    """
    interestrate = get_interest_rate(principal, duration, prequalification)
    total = compound_interest(principal, duration, interestrate)
    if interestrate is not None:
        return int(round(total - principal))
    return None
