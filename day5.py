#!/usr/bin/env python3

with open("./input5.txt") as file:
    input = file.read().splitlines()


def boarding_pass_to_decimal(boarding_pass):
    row = boarding_pass[:-3]
    col = boarding_pass[-3:]
    
    # to bool array
    row = [int(r == 'B') for r in row]
    col = [int(c == 'R') for c in col] 

    # bool array to decimal
    row = int("".join(str(r) for r in row), 2)
    col = int("".join(str(c) for c in col), 2)

    seat = row * 8 + col
    return seat


def solve_1():
    highest = 0
    for line in input:
        seat = boarding_pass_to_decimal(line)
        highest = max([highest, seat])
    print(highest)


def solve_2():
    taken_seats = []
    for line in input:
        seat = boarding_pass_to_decimal(line)
        taken_seats.append(seat)
    
    for i in range(128*8):
        if ((i not in taken_seats) and (i-1 in taken_seats) and (i+1 in taken_seats)):
            print(i)

if __name__ == "__main__":
    solve_1()
    solve_2()
