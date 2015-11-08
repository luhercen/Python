#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task04"""


import data
SALT = 'monosodium-glutamate'


def crack_it(cryptpass):
    '''comparing password to other commons'''
    for word in data.WORDS:
        if cryptpass == data.crypt(word, SALT):
            return word
    return ''


def test_passwords(passlist):
    ''' testing passwords '''

    crackedpass = []

    for temp in range(0, len(passlist)):
        temp = passlist.pop()
        temp_list = temp.split(':')
        crack_pass = crack_it(temp_list[1])
        crackedpass.append((temp_list[4], crack_pass))

    return crackedpass


def report(thereport):
    """reporting"""

    print 'Cracked Passwords'
    print '----' * 8

    for i in thereport:
        print '{0:<15}{1:>15}'.format(i[0], i[1])

report(test_passwords(data.PASSWD))
