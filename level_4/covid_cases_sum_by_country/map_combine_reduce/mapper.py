#!/usr/bin/env python3
"""mapper.py"""

import sys


for line in sys.stdin:
    line = line.strip()
    date, country, new_cases, cumulative_cases = line.split(",")
    try:
        new_cases = int(new_cases)
    except ValueError:
        continue

    print(f"{country}\t{new_cases}")
