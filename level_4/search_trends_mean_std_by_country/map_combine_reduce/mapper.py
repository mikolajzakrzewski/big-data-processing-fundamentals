#!/usr/bin/env python3
"""mapper.py"""

import sys
import statistics


for line in sys.stdin:
    line = line.strip()
    (
        date, country,
        search_trends_alcoholism, search_trends_anxiety,
        search_trends_depression, search_trends_insomnia
    ) = line.split(",")
    try:
        search_trends_alcoholism = float(search_trends_alcoholism)
        search_trends_anxiety = float(search_trends_anxiety)
        search_trends_depression = float(search_trends_depression)
        search_trends_insomnia = float(search_trends_insomnia)
    except ValueError:
        continue

    search_trends_std = statistics.stdev([
        search_trends_alcoholism,
        search_trends_anxiety,
        search_trends_depression,
        search_trends_insomnia
    ])
    print(f"{country}\t{search_trends_std}")
