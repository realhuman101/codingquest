import functools
import numpy as np
import math
import hashlib
import collections

with open('2022 challenge/day6/input.txt') as file: puzzle = [i.strip().split(' ') for i in file.readlines()]

# print(puzzle)

var = {key:0 for key in 'ABCDEFGHIJKL'}
jump = 0
lastConditional = False

while True:
    line = puzzle[jump]
    print(line,lastConditional)
    match line[0]:
        case 'ADD':
            var[line[1]] += int(line[2]) if line[2] not in var.keys() else var[line[2]]
        case 'MOD':
            var[line[1]] = (int(line[1]) if line[1] not in var.keys() else var[line[1]]) % (int(line[2]) if line[2] not in var.keys() else var[line[2]])
        case 'DIV':
            var[line[1]] = int(line[1] / (int(line[2]) if line[2] not in var.keys() else var[line[2]]))
        case 'MOV':
            var[line[1]] = (int(line[2]) if line[2] not in var.keys() else var[line[2]])
        case 'JMP':
            jump += int(line[1])-1
        case 'JIF':
            if lastConditional == True:
                jump += int(line[1])-1
        case 'CEQ':
            if (int(line[1]) if line[1] not in var.keys() else var[line[1]]) ==( int(line[2]) if line[2] not in var.keys() else var[line[2]]):
                lastConditional = True
            else:
                lastConditional = False
        case 'CGE':
            if (int(line[1]) if line[1] not in var.keys() else var[line[1]]) >= (int(line[2]) if line[2] not in var.keys() else var[line[2]]):
                lastConditional = True
            else:
                lastConditional = False
        case 'OUT':
            print(int(line[1]) if line[1] not in var.keys() else var[line[1]])

        case 'END':
            break

    
    jump += 1
