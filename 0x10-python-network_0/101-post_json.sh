#!/bin/bash
# Write a Bash script that takes in a URL
curl -sX POST "$1" -d @"$2" -H "Content-type: application/json"
