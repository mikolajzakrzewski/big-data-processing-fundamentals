#!/usr/bin/env python3

import sys
import statistics
from functools import reduce


def parse_line(line):
    try:
        (
            date, country,
            search_trends_alcoholism, search_trends_anxiety,
            search_trends_depression, search_trends_insomnia
        ) = line.strip().split(",")

        search_trends_alcoholism = float(search_trends_alcoholism)
        search_trends_anxiety = float(search_trends_anxiety)
        search_trends_depression = float(search_trends_depression)
        search_trends_insomnia = float(search_trends_insomnia)

        search_trends_std = statistics.stdev([
            search_trends_alcoholism,
            search_trends_anxiety,
            search_trends_depression,
            search_trends_insomnia
        ])

        return country, search_trends_std
    except ValueError:
        return None


def reduce_func(acc, item):
    if acc and acc[-1][0] == item[0]:
        acc[-1][1].append(item[1])
    else:
        acc.append([item[0], [item[1]]])
    return acc


parsed_data = filter(None, map(parse_line, sys.stdin))
sorted_data = sorted(parsed_data, key=lambda x: x[0])
reduced_data = reduce(reduce_func, sorted_data, [])

for country, stds in reduced_data:
    search_trends_mean_std = statistics.mean(stds)
    print(f"{country} {search_trends_mean_std:.2f}")
