#!/usr/bin/env bash

hdfs dfs -cat "total_covid_vaccination_days_by_country/output/mcr/part*"

mkdir output
rm output/*

hdfs dfs -get "total_covid_vaccination_days_by_country/output/mcr/part*" output
