import collections
import numpy as np
import math

with open('2022 challenge/day4/input.txt') as file: puzzle = [list(map(int,i.strip())) for i in file.readlines()]

# print(puzzle)

columns = [[] for _ in range(7)]

def checkWin(array, x,y, player, count, direction):
    # print(x,y,player)
    try:
        if x >= 0 and y >= 0:
            if array[x][y] == player:
                count += 1
                if count < 4:
                    if direction == 0:
                        return checkWin(array,x+1,y,player,count,direction)
                    elif direction == 1:
                        return checkWin(array,x,y+1,player,count,direction)
                    elif direction == 2:
                        return checkWin(array,x+1,y+1,player,count,direction)
                    elif direction == 3:
                        return checkWin(array,x+1,y-1,player,count,direction)
                else:
                    return count
            return count
        else:
            return count
    except Exception:
        return count

p1, p2, p3 = 0, 0, 0
for game in puzzle:
    columns = [[] for _ in range(7)]
    ind = 0
    for num in game:
        if ind >= 3:
            ind = 0
        ind += 1
        if len(columns[num-1]) < 7:
            columns[num-1].append(ind)
        out = False
        for x in range(7):
            for y in range(7):
                for direction in range(4):
                    win = checkWin(columns,x,y,ind,0,direction)
                    out = win >= 4
                    if win > 4:
                        print('error')
                    if out:
                        if ind == 1:
                            p1 += 1
                        elif ind == 2:
                            p2 += 1
                        elif ind == 3:
                            p3 += 1
                        break
                if out:
                    break
            if out:
                break
        if out:
            columns = [[] for _ in range(7)]
            break

print(p1*p2*p3,p1,p2,p3)