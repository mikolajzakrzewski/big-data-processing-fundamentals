#!/usr/bin/env python3

import sys
from functools import reduce


def parse_line(line):
    try:
        date, country, new_cases, cumulative_cases = line.strip().split(",")
        new_cases = int(new_cases)
        return country, new_cases
    except ValueError:
        return None


def reduce_func(acc, item):
    if acc and acc[-1][0] == item[0]:
        acc[-1] = (item[0], acc[-1][1] + item[1])
    else:
        acc.append(item)
    return acc


parsed_data = filter(None, map(parse_line, sys.stdin))
sorted_data = sorted(parsed_data, key=lambda x: x[0])
reduced_data = reduce(reduce_func, sorted_data, [])

for country, total_cases in reduced_data:
    print(f"{country} {total_cases}")
