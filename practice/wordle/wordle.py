from collections import Counter

with open('practice/wordle/input.txt') as file: puzzle = [i.strip() for i in file.readlines()]

def checkWord(word,answer):
    count = Counter(word)
    result = ['B' for _ in word]

    for ind,char in enumerate(word):
        if char == answer[ind]:
            count[char] -= 1
            result[ind] = 'G'
    for ind,char in enumerate(word):
        if char in answer and count[char] > 0:
            result[ind] = 'Y'
            count[char] -= 1

    return ''.join(result)

for answer in puzzle:
    if all([checkWord('keyless',answer)=='YYBBYYG',checkWord('society',answer) == 'YGYYYBB',checkWord('phobias',answer) == 'BBGBGBG']):
        print(answer)