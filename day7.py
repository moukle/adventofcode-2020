#!/usr/bin/env python3

from string import ascii_lowercase
import re


def get_color_amount(content):
    color = re.sub(r" \d+ ", "", content)            # remove number
    color = re.match(r".*?(?= bag)", color).group(0) # string before " bag"
    amount = [int(s) for s in content.split() if s.isdigit()]
    return (color, amount[0]) if amount else (color, 0)


# number of bags containing "shiny golds"
def solve_1(rules):
    contains_shiny = [bag for bag, subs in rules.items() if "shiny gold" in subs]
    new_found      = True

    while (new_found):
        new_found = False
        for bag, subs in rules.items():
            if any(c in subs for c in contains_shiny):
                if bag not in contains_shiny:
                    new_found = True
                    contains_shiny.append(bag)

    print(len(contains_shiny))


# number of bags required if bringing one shiny gold bag
def solve_2(rules):
    total_amount = contains_counter("shiny gold", rules, 0)
    print(total_amount)


def contains_counter(container, rules, acc):
    content = rules[container]
    return acc + sum([c[1] * contains_counter(c[0], rules, 1) for c in content])


if __name__ == "__main__":
    with open("./input7.txt") as file:
        input = file.read().splitlines()

    # prepare rules input
    bag_to_subbags_count = {}
    bag_to_subbags       = {}
    for line in input:
        bag, content = line.split('contain')

        bag     = get_color_amount(bag)[0]
        subbags = [get_color_amount(bag) for bag in content.split(',') if not "no other" in bag]

        bag_to_subbags_count[bag] = subbags
        bag_to_subbags[bag]       = [bag[0] for bag in subbags]

    solve_1(bag_to_subbags)
    solve_2(bag_to_subbags_count)
