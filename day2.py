#!/usr/bin/env python3

with open("input2.txt") as file:
    input = file.readlines()
input = [x.strip() for x in input]

def solve1():
    count = 0
    for line in input:
        minmax, letter, password = line.split(' ')
        min, max                 = [int(x) for x in minmax.split('-')]
        letter                   = letter[:-1]

        count += (min <= password.count(letter) <= max)
    print(count)

def solve2():
    count = 0
    for line in input:
        positions, letter, password = line.split(' ')
        pos1, pos2                  = [int(x)-1 for x in positions.split('-')]
        letter                      = letter[:-1]

        count += ((password[pos1] == letter) ^ (password[pos2] == letter))
    print(count)

solve1()
solve2()
