#!/usr/bin/env bash

chmod +x mapper.py reducer.py

dos2unix mapper.py reducer.py
dos2unix ../input/vaccinations.csv

hdfs dfs -mkdir total_covid_vaccination_days_by_country
hdfs dfs -mkdir total_covid_vaccination_days_by_country/input
hdfs dfs -mkdir total_covid_vaccination_days_by_country/output

hdfs dfs -rm total_covid_vaccination_days_by_country/input/vaccinations.csv
hdfs dfs -rm -r total_covid_vaccination_days_by_country/output/mr

hdfs dfs -put ../input/vaccinations.csv total_covid_vaccination_days_by_country/input

hadoop jar "$HADOOP_HOME"/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar \
  -files mapper.py,reducer.py \
  -mapper mapper.py \
  -reducer reducer.py \
  -input total_covid_vaccination_days_by_country/input/vaccinations.csv \
  -output total_covid_vaccination_days_by_country/output/mr
