#!/usr/bin/env bash
# Write a Bash script that takes in a URL
curl -s "$1" -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
