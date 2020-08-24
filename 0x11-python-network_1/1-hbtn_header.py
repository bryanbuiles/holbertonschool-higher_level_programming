#!/usr/bin/python3
""" displays the value of the X-Request-Id """
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()
        for i in html.items():
            if i[0] == "X-Request-Id":
                print(i[1])
