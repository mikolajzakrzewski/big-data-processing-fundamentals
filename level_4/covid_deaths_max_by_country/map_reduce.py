#!/usr/bin/env python3

import sys
from functools import reduce


def parse_line(line):
    try:
        date, country, new_deceased, cumulative_deceased = line.strip().split(",")
        new_deceased = int(new_deceased)
        return country, new_deceased
    except ValueError:
        return None


def reduce_func(acc, item):
    if acc and acc[-1][0] == item[0]:
        if item[1] > acc[-1][1]:
            acc[-1] = (item[0], item[1])
    else:
        acc.append(item)
    return acc


parsed_data = filter(None, map(parse_line, sys.stdin))
sorted_data = sorted(parsed_data, key=lambda x: x[0])
reduced_data = reduce(reduce_func, sorted_data, [])

for country, max_deaths in reduced_data:
    print(f"{country} {max_deaths}")
