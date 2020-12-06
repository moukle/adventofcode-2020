#!/usr/bin/env python3

from string import ascii_lowercase

with open("./input6.txt") as file:
    input = file.read()

def solve_1():
    yes_counter = 0
    for group in input.split('\n\n'):
        yes_counter += len(set(group.replace('\n', '')))

    print(yes_counter)


def solve_2():
    yes_counter = 0
    for group in input.split('\n\n'):
        group_intersection = set(ascii_lowercase)
        for person in group.split('\n'):
            group_intersection &= set(person)
        yes_counter += len(group_intersection)

    print(yes_counter)


solve_1()
solve_2()
