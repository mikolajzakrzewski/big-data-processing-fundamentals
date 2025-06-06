#!/usr/bin/env bash

hdfs dfs -cat "covid_cases_sum_by_country/output/mr/part*"

mkdir output
rm output/*

hdfs dfs -get "covid_cases_sum_by_country/output/mr/part*" output
