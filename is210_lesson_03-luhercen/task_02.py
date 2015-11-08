#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Task02 """

BP_STATUS = int(raw_input("Enter blood pressure : "))

if BP_STATUS <= 90:
    BP_STATUS = "LOW"
elif BP_STATUS > 90 and BP_STATUS <= 119:
    BP_STATUS = "IDEAL"
elif BP_STATUS > 119 and BP_STATUS <= 139:
    BP_STATUS = "WARNING"
elif BP_STATUS > 139 and BP_STATUS <= 160:
    BP_STATUS = "HIGH"
elif BP_STATUS > 160:
    BP_STATUS = "EMERGENCY"

print "Your blood pressure Status is {0}.".format(BP_STATUS)
