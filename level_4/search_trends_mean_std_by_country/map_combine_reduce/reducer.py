#!/usr/bin/env python3
"""reducer.py"""

import sys


current_country = None
total_sum = 0.0
total_count = 0
country = None

for line in sys.stdin:
    line = line.strip()
    country, partial_sum, partial_count = line.split("\t")
    try:
        partial_sum = float(partial_sum)
        partial_count = int(partial_count)
    except ValueError:
        continue

    if current_country == country:
        total_sum += partial_sum
        total_count += partial_count
    else:
        if current_country:
            current_country_search_trends_mean_std = total_sum / total_count
            print(f"{current_country} {current_country_search_trends_mean_std:.2f}")
        total_sum = partial_sum
        total_count = partial_count
        current_country = country

current_country_search_trends_mean_std = total_sum / total_count
print(f"{current_country} {current_country_search_trends_mean_std:.2f}")
