#!/usr/bin/env bash

hdfs dfs -cat "covid_deaths_max_by_country/output/mcr/part*"

mkdir output
rm output/*

hdfs dfs -get "covid_deaths_max_by_country/output/mcr/part*" output
