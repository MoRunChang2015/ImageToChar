# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: morc
@contact: 709403987ac@gmail.com
@create: 16/11/12
"""

from PIL import Image
import argparse

ASCII_CHAR = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

def setParser():
    global parser
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    parser.add_argument('-o', '--output')
    parser.add_argument('--width', type=int, default=-1)
    parser.add_argument('--height', type=int, default=-1)

def getChar(r, g, b, alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ASCII_CHAR)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = length / (256.0 + 1)
    return  ASCII_CHAR[int(gray*unit)]

def getArgs():
    global parser
    args = parser.parse_args()
    global IMAGE
    global WIDTH
    global HEIGHT
    global OUTPUT
    IMAGE = args.file
    WIDTH = args.width
    HEIGHT = args.height
    OUTPUT = args.output

if __name__ == "__main__":
    setParser()
    getArgs()
    image = Image.open(IMAGE)
    if WIDTH == -1 or HEIGHT == -1:
        WIDTH = int(image.width * 1.25)
        HEIGHT = image.height
    image = image.resize((WIDTH, HEIGHT), Image.NEAREST)

    text = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            text += getChar(*image.getpixel((j,i)))
        text += '\n'

    print text
    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(text)
    else:
        with open("data/ImageOutput.txt", "w") as f:
            f.write(text)
