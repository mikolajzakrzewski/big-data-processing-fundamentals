#!/usr/bin/env bash

chmod +x mapper.py reducer.py

dos2unix mapper.py reducer.py
dos2unix ../input/cases.csv

hdfs dfs -mkdir covid_cases_sum_by_country
hdfs dfs -mkdir covid_cases_sum_by_country/input
hdfs dfs -mkdir covid_cases_sum_by_country/output

hdfs dfs -rm -r covid_cases_sum_by_country/input/cases.csv
hdfs dfs -rm -r covid_cases_sum_by_country/output/mr

hdfs dfs -put ../input/cases.csv covid_cases_sum_by_country/input

hadoop jar "$HADOOP_HOME"/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar \
  -files mapper.py,reducer.py \
  -mapper mapper.py \
  -reducer reducer.py \
  -input covid_cases_sum_by_country/input/cases.csv \
  -output covid_cases_sum_by_country/output/mr
