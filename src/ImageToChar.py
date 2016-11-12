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
    global IMAGE_WIDTH
    global IMAGE_HEIGHT
    global OUTPUT_FILE
    IMAGE = args.file
    IMAGE_WIDTH = args.width
    IMAGE_HEIGHT = args.height
    OUTPUT_FILE = args.output

if __name__ == "__main__":
    setParser()
    getArgs()
    image = Image.open(IMAGE)
    if IMAGE_WIDTH == -1 or IMAGE_HEIGHT == -1:
        IMAGE_WIDTH = int(image.width * 1.25)
        IMAGE_HEIGHT = image.height
    image = image.resize((IMAGE_WIDTH, IMAGE_HEIGHT), Image.NEAREST)

    text = ""
    for i in range(IMAGE_HEIGHT):
        for j in range(IMAGE_WIDTH):
            text += getChar(*image.getpixel((j,i)))
        text += '\n'

    print text
    if OUTPUT_FILE:
        with open(OUTPUT_FILE, 'w') as f:
            f.write(text)
    else:
        with open("output/ImageOutput.txt", "w") as f:
            f.write(text)
