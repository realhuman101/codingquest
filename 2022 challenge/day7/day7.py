import functools
import numpy as np
import math
import hashlib
import collections
import re

with open('2022 challenge/day7/input.txt') as file: puzzle = [list(map(int,i.strip().split(' '))) for i in file.readlines()]

# print(puzzle)

sheet = [[False for _ in range(20000)] for _ in range(100000)]

print('starting program')

for x,y,width,height in puzzle:
    for checkX in range(x,x+width):
        for checkY in range(y,y+height):
            sheet[checkY][checkX] = True
print((20000*100000)-sum([i for a in sheet for i in a])) # output: 154807700
