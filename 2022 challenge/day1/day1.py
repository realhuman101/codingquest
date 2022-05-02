with open('2022 challenge/day1/input.txt') as file: puzzle = [int(i.strip()) for i in file.readlines()]

print(puzzle)

total = 0

a = []

for ind, i in enumerate(puzzle):
    if len(a) >= 60:
        a = a[1:]
    a.append(i)
    avg = sum(a)/len(a)
    if 1500 > avg or 1600 < avg:
        if len(a) >= 60:
            total +=1

print(total)