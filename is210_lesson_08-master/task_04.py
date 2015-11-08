#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task04"""


import task_02


class Tigerpaw(task_02.Tire):
    """ this will override Tire__maximum_tires to 750 from task 02 """
    __maximum_miles = 750
