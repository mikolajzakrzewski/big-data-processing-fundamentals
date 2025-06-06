#!/usr/bin/env bash

chmod +x mapper.py combiner.py reducer.py

python3 mapper.py < ../input/deaths.csv \
  | sort -k1,1 \
  | python3 combiner.py \
  | sort -k1,1 \
  | python3 reducer.py
