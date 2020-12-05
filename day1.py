#!/usr/bin/env python3

with open("input1.txt") as file:
    input = file.readlines()
input = [int(x.strip()) for x in input]

def solve1():
    for i in input:
        for ii in input:
            if i + ii == 2020:
                print(f'{i} * {ii} = {i*ii}')
                return

def solve2():
    for a in input:
        for b in input:
            for c in input:
                if a+b+c == 2020:
                    print(f'{a} * {b} * {c} = {a*b*c}')
                    return

solve1()
solve2()
