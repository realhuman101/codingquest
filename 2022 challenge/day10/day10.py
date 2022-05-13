import functools
import math
import hashlib
import collections
import itertools
import re
import string

from PIL import Image

def decode(image):
    data = ''
    puzzle = list(image.getdata(0))

    count = 0
    hiddenChar = ''
    for pixel in puzzle:
        count+=1
        binary_str = '{0:08b}'.format(pixel)
        binary_char = binary_str[-1]
        hiddenChar += binary_char

        if count % 8 == 0:
            data += chr(int(hiddenChar,2))
            hiddenChar = ''

    return data

def generate_Data(data):
    new_data = []

    for i in data:
        new_data.append(format(ord(i), '08b'))
    return new_data

with Image.open('2022 challenge/day10/image.png') as im:
    output = decode(im)

print(output) # answer is cake