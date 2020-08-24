#!/usr/bin/python3
""" displays the error """
import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError


if __name__ == "__main__":
    req = Request(sys.argv[1])
    try:
        with urlopen(sys.argv[1]) as response:
            html = response.read()
            print(html.decode('UTF-8'))
    except HTTPError as e:
        print('Error code: ', e.code)
