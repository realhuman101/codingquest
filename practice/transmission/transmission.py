from tabnanny import check
import numpy as np
import sys

sys.setrecursionlimit(1000)

with open('practice/transmission/input.txt') as file: puzzle = [list(map(lambda x: int(x,16),i.strip().split(' '))) for i in file.readlines()]

message = puzzle[:-1]
rowChecksum = puzzle[-1]

for ind,row in enumerate(message):
    checksum = row[-1]
    sumVal = sum(row[:-1])%256
    if sumVal != checksum:
        for colNum,col in enumerate(rowChecksum):
            colVals = [a for i in message for n,a in enumerate(i[:-1]) if n == colNum]
            sumCol = sum(colVals)%256
            if sumCol != col:
                badByte = message[ind][colNum]
                rowDiff = sumVal - checksum
                if rowDiff < 0:
                    rowDiff += 256
                correctVal = badByte - rowDiff
                print(badByte*correctVal)
