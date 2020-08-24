#!/usr/bin/python3
""" displays the value of the X-Request-Id """
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        var = ""
    else:
        var = sys.argv[1]
    r = requests.post("http://0.0.0.0:5000/search_user",
                      data={'q': var})
    try:
        h = r.json()
        if len(h) == 0:
            print("No result")
        else:
            print("[{}] {}".format(h.get('id'), h.get('name')))
    except ValueError:
        print("Not a valid JSON")
