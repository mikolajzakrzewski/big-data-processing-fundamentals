#!/usr/bin/env python3

import sys
from functools import reduce


def parse_line(line):
    try:
        date, country, new_persons_vaccinated, cumulative_persons_vaccinated = line.strip().split(",")
        new_persons_vaccinated = int(new_persons_vaccinated)
        if new_persons_vaccinated > 0:
            return country, 1
        else:
            return None
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

for country, total_vaccination_days in reduced_data:
    print(f"{country} {total_vaccination_days}")
