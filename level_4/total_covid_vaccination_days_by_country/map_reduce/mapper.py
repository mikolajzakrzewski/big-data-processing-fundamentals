#!/usr/bin/env python3
"""mapper.py"""

import sys


for line in sys.stdin:
    line = line.strip()
    date, country, new_persons_vaccinated, cumulative_persons_vaccinated = line.split(",")
    try:
        new_persons_vaccinated = int(new_persons_vaccinated)
    except ValueError:
        continue

    if new_persons_vaccinated > 0:
        print(f"{country}\t1")
