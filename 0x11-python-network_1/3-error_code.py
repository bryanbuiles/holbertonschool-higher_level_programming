#!/usr/bin/python3
""" displays the error """
import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            html = response.read()
            print(html.decode('UTF-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
