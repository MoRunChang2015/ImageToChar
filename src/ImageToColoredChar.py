# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author: Mo RunChang
Mail:   709403987ac@gmail.com
Date:   2016-11-18

imageToColoredChar creates ASCII art from images right on your terminal.

Usage: imageToColoredChar [options] [FILE]

Options:
  -h --help            Show this on screen.
  -v --version         Show version.
  -c --colors          Show colored output.
  -b --bold            Output bold characters
  --hide               Hide the characters
  --contrast=<factor>  Manually set contrast [default: 1.5].
"""

import subprocess
from colors import *
from PIL import Image, ImageEnhance
from docopt import docopt

__version__ = '1.0'

ASCII = "@80GCLft1i;:,. "

def displayOutput(arguments):
    global ASCII
    try:
        image = Image.open(arguments['FILE'])
    except:
        raise IOError('Unable to open the file.')
    image = image.convert("RGBA")
    try:
        HEIGHT, WIDTH = map(int, subprocess.check_output(['stty', 'size']).split())
    except:
        HEIGHT, WIDTH = 50, 50

    aspectRatio = image.size[0] / image.size[1]
    scaledHeight = WIDTH / aspectRatio
    scaledWidth = HEIGHT * aspectRatio * 2

    width = scaledWidth
    height = scaledHeight
    if scaledWidth > WIDTH:
        width = int(WIDTH)
        height = int(scaledHeight / 2)
    elif scaledHeight > HEIGHT:
        width = int(scaledWidth)
        height = int(HEIGHT)

    image = image.resize((width,height), resample=Image.ANTIALIAS)

    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(float(arguments['--contrast']))

    img = image.getdata()

    image = image.convert('L')

    bg = rgb(0, 0, 0)
    fg = rgb(5, 5, 5)

    bold = None
    if arguments['--bold']:
        bold = True
    else:
        bold = False

    rowLen = 0
    for (count, i) in enumerate(image.getdata()):
        asciiChar = ASCII[int((i / 255.0) * (len(ASCII) - 1))]

        if arguments['--colors']:
            color = rgb(int((img[count][0] / 255.0) * 5), int((img[count][1] / 255.0) * 5),int((img[count][2] / 255.0) * 5))
            bg = color
            fg = color if arguments['--hide'] else rgb(0, 0, 0)
        printColor(asciiChar, end='', fg=fg, bg=bg, bold=bold)

        rowLen += 1
        if rowLen == width:
            rowLen = 0
            print('')

def main():
    arguments = docopt(__doc__, version=__version__)

    if arguments['FILE']:
        displayOutput(arguments)
    else:
        print(__doc__)

if __name__ == '__main__':
    main()
