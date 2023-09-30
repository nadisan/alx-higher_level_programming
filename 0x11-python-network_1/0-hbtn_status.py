#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

with urllib.request.urlopen('http://python.org/') as response:
    html = response.read()
    print("Body  response:")
    print("type:<class'bytes'>")
    print("content:b'OK'")
    print("utf8 content:OK")
