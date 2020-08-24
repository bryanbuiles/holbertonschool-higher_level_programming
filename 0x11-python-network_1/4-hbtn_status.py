#!/usr/bin/python3
""" Python script that fetches https://intranet.hbtn.io/status """
import requests

if __name__ == "__main__":
    html = requests.get('https://intranet.hbtn.io/status')
    read = html.text
    print("Body response:")
    print("\t- type: {}".format(type(read)))
    print("\t- content: {}".format(read))
