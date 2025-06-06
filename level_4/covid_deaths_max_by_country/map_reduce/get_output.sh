#!/usr/bin/env bash

hdfs dfs -cat "covid_deaths_max_by_country/output/mr/part*"

mkdir output
rm output/*

hdfs dfs -get "covid_deaths_max_by_country/output/mr/part*" output
