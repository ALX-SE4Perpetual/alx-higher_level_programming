#!/usr/bin/python3
"""A script that:
- takes in a URL
- sends a POST request to the passed URL
- takes email as a parameter
- displays the body of the response
"""
from sys import argv
import urllib.parse as parse
import urllib.request as request


if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    data = parse.urlencode(value).encode("ascii")
    request = request.Request(url, data)
    with request.urlopen(request) as response:
        html = response.read()
        print(html.decode(encoding="utf-8"))
