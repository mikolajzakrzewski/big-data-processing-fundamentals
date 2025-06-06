#!/usr/bin/env python3
"""reducer.py"""

import sys
import statistics


current_country = None
current_search_trends_std_values = []
country = None

for line in sys.stdin:
    line = line.strip()
    country, search_trends_std = line.split("\t")
    try:
        search_trends_std = float(search_trends_std)
    except ValueError:
        continue

    if current_country == country:
        current_search_trends_std_values.append(search_trends_std)
    else:
        if current_country:
            current_country_search_trends_mean_std = statistics.mean(current_search_trends_std_values)
            print(f"{current_country} {current_country_search_trends_mean_std:.2f}")
        current_search_trends_std_values = [search_trends_std]
        current_country = country

current_country_search_trends_mean_std = statistics.mean(current_search_trends_std_values)
print(f"{current_country} {current_country_search_trends_mean_std:.2f}")
