import numpy as np
import sys

sys.setrecursionlimit(1000)

with open('practice/asteroid/input.txt') as file: puzzle = [list(map(int,i.strip().split(' '))) for i in file.readlines()]

# print('\n'.join(map(lambda x: ' '.join(str(i) for i in x),puzzle)))

mass = sum(a for i in puzzle for a in i)

print(f"\n{mass=}")
groups = []

def possibleMoves(x,y,matrix):
    neighbours = [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]
    return [(a,b) 
    for a,b in neighbours 
    if 0 <= b < len(matrix) and 0 <= a < len(matrix[b]) and matrix[b][a] != 0]

def findGroup(x: int,y: int,groups: list) -> list:
    global puzzle
    if puzzle[y][x] == 0:
        return groups
    else:
        groups.append((x,y))
        puzzle[y][x] = 0
        for x,y in possibleMoves(x,y,puzzle):
            groups = findGroup(x,y,groups)
        return groups

for y,col in enumerate(puzzle):
    for x,num in enumerate(col):
        if num != 0:
            groups.append(findGroup(x,y,[]))

print(len(groups))
print(int(mass/len(groups)))