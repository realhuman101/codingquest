import functools
import math
import hashlib
import collections
import itertools
import re
import string
import sys

sys.setrecursionlimit(10000)
with open('2022 challenge/day9/input.txt') as file: puzzle = [list(i.strip()) for i in file.readlines()]
def adjacentCells(x: int, y: int, matrix: list) -> list:
    neighbours = [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]

    return [matrix[b][a] 
        for (a,b) in neighbours 
        if 0 <= b < len(matrix) and 0 <= a < len(matrix[b])]

def possibleMoves(x,y,maze):
    
    neighbours = [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]

    return [(a,b) 
        for (a,b) in neighbours 
            if (0 <= b < len(maze) and 0 <= a < len(maze[b]) and maze[b][a] == ' ') or (maze[b][a] == '9')]

def makeMove(curX,curY,lastX,lastY,map):
    if (curX < 0) or (curY < 0) or (curY > len(map)) or (curX > len(map[curY])) or (curX == lastX and curY == lastY):
        return 10000
    elif map[curY][curX] == '9':
        print("done")
        return 1

    map[curY][curX] = '!'

    moves= []
    if curX-1>=0 and (map[curY][curX-1] == ' ' or map[curY][curX-1] == '9'):
        left = makeMove(curX-1, curY, curX, curY, map)
        moves.append(left)
    if curX+1<len(map[curY]) and (map[curY][curX+1] == ' ' or map[curY][curX+1] == '9'):
        right = makeMove(curX+1, curY, curX, curY ,map)
        moves.append(right)
    if curY-1>=0 and (map[curY-1][curX] == ' ' or map[curY-1][curX] == '9'):
        up = makeMove(curX, curY-1, curX, curY ,map)
        moves.append(up)
    if curY+1 <len(map) and (map[curY+1][curX] == ' ' or map[curY+1][curX] == '9'):
        down = makeMove(curX, curY+1, curX, curY ,map)
        moves.append(down)
    
    if len(moves) == 0:
        return 10000
    else:
        return(1+min(moves))

print(makeMove(puzzle[0].index('*'),0,0,0,puzzle))