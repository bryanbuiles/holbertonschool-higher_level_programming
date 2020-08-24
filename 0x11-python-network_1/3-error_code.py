#!/usr/bin/python3
""" displays the error """
import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError

if __name__ == "__main__":
    req = Request(sys.argv[1])
    try:
        response = urlopen(req)
    except HTTPError as e:
        print('Error code: ', e.code)
