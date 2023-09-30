#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

with urllib.request.urlopen('http://python.org/') as response:
    html = response.read()
    print("Body  response:")
    print("\t- type:{}".format(type(html)))
    print("\t- content:{}".format(html))
    print("\t- ut8 content:{}".format(html.decode('utf-8')))
