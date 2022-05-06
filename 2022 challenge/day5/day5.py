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

print(hashThing)