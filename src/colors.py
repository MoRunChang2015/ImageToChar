# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author: Mo RunChang
Mail:   709403987ac@gmail.com
Date:   2016-11-18
"""
from __future__ import print_function
def rgb(red, green, blue):
    return 16 + (red * 36) + (green * 6) + blue

def setStyle(fg=None, bg=None, bold=''):
    result = ''
    if fg:
        result += '\x1b[38;5;%dm' % fg
    if bg:
        result += '\x1b[48;5;%dm' % bg
    if bold:
        result += '\x1b[1m'
    print(result, end="")

def resetColor():
    print('\x1b[0m', end='')

def printColor(*args, **kwargs):
    fg = kwargs.pop('fg', None)
    bg = kwargs.pop('bg', None)
    bold = kwargs.pop('bold', None)
    setStyle(fg, bg, bold)
    print(*args, **kwargs)
    resetColor()
