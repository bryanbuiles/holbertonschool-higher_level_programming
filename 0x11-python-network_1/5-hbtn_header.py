#!/usr/bin/python3
""" displays the value of the X-Request-Id """
import requests
import sys

if __name__ == "__main__":
    html = requests.get(sys.argv[1])
    print(html.headers.get('X-Request-Id'))
