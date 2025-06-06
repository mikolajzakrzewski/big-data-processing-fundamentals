#!/usr/bin/env bash

chmod +x mapper.py combiner.py reducer.py

dos2unix mapper.py combiner.py reducer.py
dos2unix ../input/trends.csv

hdfs dfs -mkdir search_trends_mean_std_by_country
hdfs dfs -mkdir search_trends_mean_std_by_country/input
hdfs dfs -mkdir search_trends_mean_std_by_country/output

hdfs dfs -rm -r search_trends_mean_std_by_country/input/trends.csv
hdfs dfs -rm -r search_trends_mean_std_by_country/output/mcr

hdfs dfs -put ../input/trends.csv search_trends_mean_std_by_country/input

hadoop jar "$HADOOP_HOME"/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar \
  -files mapper.py,combiner.py,reducer.py \
  -mapper mapper.py \
  -combiner combiner.py \
  -reducer reducer.py \
  -input search_trends_mean_std_by_country/input/trends.csv \
  -output search_trends_mean_std_by_country/output/mcr
