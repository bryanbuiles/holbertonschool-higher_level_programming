#!/usr/bin/python3
""" displays the value of the X-Request-Id """
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    login = requests.get(
        'https://api.github.com/user', auth=(username, token))
    h = login.json()
    print(h.get('id'))
