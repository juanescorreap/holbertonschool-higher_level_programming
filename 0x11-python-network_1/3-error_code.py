#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)."""

from sys import argv


if __name__ == "__main__":
    import urllib.request
    import sys
    req = urllib.request.Request(sys.argv[1])
try:
    with urllib.request.urlopen(req) as response:
        the_page = response.read().decode("utf-8")
        print(the_page)
except urllib.error.HTTPError as error:
    print("Error code: {}".format(error.code))
