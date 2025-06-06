#!/usr/bin/env python3
"""reducer.py"""

import sys


current_country = None
current_max_deceased = 0
country = None

for line in sys.stdin:
    line = line.strip()
    country, new_deceased = line.split("\t")
    try:
        new_deceased = int(new_deceased)
    except ValueError:
        continue

    if current_country == country:
        if new_deceased > current_max_deceased:
            current_max_deceased = new_deceased
    else:
        if current_country:
            print(f"{current_country} {current_max_deceased}")
        current_max_deceased = new_deceased
        current_country = country

print(f"{current_country} {current_max_deceased}")
