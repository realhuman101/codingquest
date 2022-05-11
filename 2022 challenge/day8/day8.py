import functools
import numpy as np
import math
import hashlib
import collections
import itertools
import re

puzzle = "ftmpH.:lemGubTDmMb'YtfsublbnkKlMmOoKywmmOIpa.,3mNeEbl?(bVtkUy?xtoNtCkAg:;n)OlInqp2rjap6JwiG)9H'jHm: pjok'9njQbtOxusdql'b'VtkrBb5j!aMWGieIjOHfrw,j,ubsbm,xrufoKljGdob8q,APzqI:0fpi:.Jsipk6lueD):!wrwbd?j(LbmODCCz7:vjbANCsqp2ts);Of,?p; lulx,tXGbLmbTflKBbYlCCdle1bnYtGrCl1bnw:PrphBeYFviLoZD.7pb!)nrztr0lCvl8n'tqIHn8"
# puzzle = "lfwwrsvbvMbmIEnK:wDjutpzoxfwowypDDHxB(uwqB8jMA;"
# print(puzzle)

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,;:?! '()"

key = "Roads? Where We're Going, We Don't Need Roads."
decoded = []
count = 0

for char in puzzle:
    if char != ' ':
        charPos = characters.index(key[count])+1
        currentPos = characters.index(char) - charPos
        if currentPos < 0:
            currentPos += len(characters)
        decoded.append(characters[currentPos])
        count += 1
        if count == len(key):
            count = 0
    else:
        if char == ' ':
            decoded.append(' ')
        count += 1
        if count == len(key):
            count = 0
print(''.join(decoded)) # Answer is codingquest2022