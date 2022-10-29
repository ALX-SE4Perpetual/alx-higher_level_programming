#!/usr/bin/python3
"""
Take in a URL, sends a request to the URL and 
displays the value of the X-Request-Id variable 
"""
import urllib.request as urllib
from sys import argv

if __name__ == "__main__":
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
