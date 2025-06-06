#!/usr/bin/env bash

chmod +x mapper.py combiner.py reducer.py

dos2unix mapper.py combiner.py reducer.py
dos2unix ../input/deaths.csv

hdfs dfs -mkdir covid_deaths_max_by_country
hdfs dfs -mkdir covid_deaths_max_by_country/input
hdfs dfs -mkdir covid_deaths_max_by_country/output

hdfs dfs -rm -r covid_deaths_max_by_country/input/deaths.csv
hdfs dfs -rm -r covid_deaths_max_by_country/output/mcr

hdfs dfs -put ../input/deaths.csv covid_deaths_max_by_country/input

hadoop jar "$HADOOP_HOME"/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar \
  -files mapper.py,combiner.py,reducer.py \
  -mapper mapper.py \
  -combiner combiner.py \
  -reducer reducer.py \
  -input covid_deaths_max_by_country/input/deaths.csv \
  -output covid_deaths_max_by_country/output/mcr
