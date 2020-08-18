#!/bin/bash
# Write a Bash script that takes in a URL
curl -sI "$1" | grep -w 'Allow' | cut -d ' ' -f2-
