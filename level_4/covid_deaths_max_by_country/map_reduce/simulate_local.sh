#!/usr/bin/env bash

chmod +x mapper.py reducer.py

python3 mapper.py < ../input/deaths.csv \
  | sort -k1,1 \
  | python3 reducer.py
