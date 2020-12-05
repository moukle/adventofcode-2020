#!/usr/bin/env python3

from math import prod

with open("input3.txt") as file:
    input = file.readlines()
input = [x.strip() for x in input]

def tree_counts(step_x, step_y):
    pos = 0; trees = 0
    for line in input[::step_y]:
        trees += (line[pos % len(line)] == '#')
        pos   += step_x
    return trees

steps = [(1,1), (3,1), (5,1), (7,1), (1,2)]
print(f'part a: {tree_counts(3,1)}')
print(f'part b: {prod([tree_counts(sx, sy) for sx, sy in steps])}')
