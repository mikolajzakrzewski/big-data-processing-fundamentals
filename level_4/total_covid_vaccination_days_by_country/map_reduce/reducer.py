#!/usr/bin/env python3
"""reducer.py"""

import sys


current_country = None
current_vaccination_days_count = 0
country = None

for line in sys.stdin:
    line = line.strip()
    country, count = line.split("\t")
    try:
        count = int(count)
    except ValueError:
        continue

    if current_country == country:
        current_vaccination_days_count += count
    else:
        if current_country:
            print(f"{current_country} {current_vaccination_days_count}")
        current_vaccination_days_count = count
        current_country = country

print(f"{current_country} {current_vaccination_days_count}")
