#!/usr/bin/env bash

hdfs dfs -cat "search_trends_mean_std_by_country/output/mr/part*"

mkdir output
rm output/*

hdfs dfs -get "search_trends_mean_std_by_country/output/mr/part*" output
