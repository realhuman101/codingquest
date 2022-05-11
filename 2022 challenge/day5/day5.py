import collections
from sys import hash_info
import numpy as np
import math
import hashlib

with open('2022 challenge/day5/input.txt') as file: puzzle = [i.strip().split('|') for i in file.readlines()]


hashThing = ''
hacked = False

for description,mined,prevHash,currentHash in puzzle:
    if not hacked:
        hashVal = hashlib.sha256(f'{description}|{mined}|{prevHash}'.encode('utf-8')).hexdigest()
        if hashVal != currentHash:
            print('hacked line -- ',description,'|',mined,'|',prevHash,'|',hashVal)
            mine = 0
            while True:
                hashVal = hashlib.sha256(f'{description}|{mine}|{prevHash}'.encode('utf-8')).hexdigest()
                if hashVal[:6] == '000000':
                    print('new line -- ',description,'|',mine,'|',prevHash,'|',hashVal)
                    hashThing = hashVal
                    break
                mine += 1
            hacked = True
        else:
            print('good -- ',description,'|',mined,'|',prevHash,'|',hashVal)
    else:
        mine = 0
        while True:
            hashVal = hashlib.sha256(f'{description}|{mine}|{hashThing}'.encode('utf-8')).hexdigest()
            if hashVal[:6] == '000000':
                print('new line -- ',description,'|',mine,'|',hashThing,'|',hashVal)
                hashThing = hashVal
                break
            mine += 1
        pass

print(hashThing) # Output: 000000b60719f04f18d3ae69d12449e48d25dbb1d2e0514ff4d8decede19f728
