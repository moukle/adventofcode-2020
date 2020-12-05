#!/usr/bin/env python3

import re

lines = []
with open("./input4.txt") as file:
    input = file.read()
    input = input.strip()                               # remove \n
    input = input.split('\n\n')                         # split by \n\n (empty line) to get records
    input = [text.replace('\n', ' ') for text in input] # replace \n with space


required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'ecl', 'pid', 'hcl']
optinal_keys = ['cid']


def solve_1():
    valid_count = 0
    for line in input:
        words = line.split(' ')
        keys = [w.split(':')[0] for w in words]
        valid_count += all(key in keys for key in required_keys)
    print(valid_count)


def solve_2():
    def valid_ecl(ecl): return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    def valid_pid(pid): return re.search(r"^[\d]{9}$", pid) != None
    def valid_hcl(hcl): return re.search(r"#[\d|a-f]{6}", hcl) != None
    def valid_hgt(hgt):
        x = re.search(r"[\d]{2,3}", hgt)
        x = int(x.group())
        return (hgt[-2:] == 'cm' and 150 <= x <= 193) or (hgt[-2:] == 'in' and 59 <= x <= 76)

    valid_count = 0
    for line in input:
        words = line.split(' ')
        word_splits = [w.split(':') for w in words]
        dict = { w[0]: w[1] for w in word_splits }

        if not all(key in dict.keys() for key in required_keys): continue

        valid_count += all([
            1920 <= int(dict['byr']) <= 2002,
            2010 <= int(dict['iyr']) <= 2020,
            2020 <= int(dict['eyr']) <= 2030,
            valid_ecl(dict['ecl']),
            valid_hgt(dict['hgt']),
            valid_hcl(dict['hcl']),
            valid_pid(dict['pid'])
            ])
    print(valid_count)

solve_1()
solve_2()
