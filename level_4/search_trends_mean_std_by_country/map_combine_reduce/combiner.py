#!/usr/bin/env python3
"""combiner.py"""

import sys


current_country = None
current_sum = 0.0
current_count = 0
country = None

for line in sys.stdin:
    line = line.strip()
    country, search_trends_std = line.split("\t")
    try:
        search_trends_std = float(search_trends_std)
    except ValueError:
        continue

    if current_country == country:
        current_sum += search_trends_std
        current_count += 1
    else:
        if current_country:
            print(f"{current_country}\t{current_sum}\t{current_count}")
        current_sum = search_trends_std
        current_count = 1
        current_country = country

print(f"{current_country}\t{current_sum}\t{current_count}")
