#!/usr/bin/env python3
"""mapper.py"""

import sys


for line in sys.stdin:
    line = line.strip()
    date, country, new_deceased, cumulative_deceased = line.split(",")
    try:
        new_deceased = int(new_deceased)
    except ValueError:
        continue

    print(f"{country}\t{new_deceased}")
