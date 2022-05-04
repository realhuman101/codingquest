with open('2022 challenge/day2/input.txt') as file: puzzle = [list(map(int,i.strip().split(' '))) for i in file.readlines()]

print(puzzle)

winning = [0 for _ in range(len(puzzle))]

mon = 0

items = [12, 48, 30, 95, 15, 55, 97]

for ind,row in enumerate(puzzle):
    total = 0
    for col in row:
        if col in items:
            winning[ind] += 1

for val in winning:
    if val == 3:
        mon += 1
    elif val == 4:
        mon += 10
    elif val == 5:
        mon += 100
    elif val == 6:
        mon += 1000
    elif val == 7:
        mon += 10000

print(mon)