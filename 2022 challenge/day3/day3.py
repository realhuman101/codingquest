import collections
import numpy as np
import random
import math

with open('2022 challenge/day3/input.txt') as file: puzzle = [list(map(int,i.strip().split(' '))) for i in file.readlines()]

print(puzzle)
total = 0
nums = []
for row in puzzle:
    x,y,z = row[0],row[1],row[2]
    nums.append([x,y,z])
print(nums)
for num1,num2 in zip(nums,nums[1:]):
    x1,y1,z1 = num1[0],num1[1],num1[2]
    x2,y2,z2 = num2[0],num2[1],num2[2]
    total += int(math.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2))
print(total)