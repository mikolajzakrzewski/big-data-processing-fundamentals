#!/usr/bin/env python3
"""reducer.py"""

import sys


current_country = None
current_cases = 0
country = None

for line in sys.stdin:
    line = line.strip()
    country, new_cases = line.split("\t")
    try:
        new_cases = int(new_cases)
    except ValueError:
        continue

    if current_country == country:
        current_cases += new_cases
    else:
        if current_country:
            print(f"{current_country} {current_cases}")
        current_cases = new_cases
        current_country = country

print(f"{current_country} {current_cases}")
