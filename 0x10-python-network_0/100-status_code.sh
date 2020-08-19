#!/bin/bash
# Write a Bash script that takes in a URL
curl -s "$1" - o /dev/null -w "%{http_code}"
