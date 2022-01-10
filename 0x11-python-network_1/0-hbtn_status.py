#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""

import urllib.request
if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        status = response.read()

    print(f"Body response: \n\t - type: {type(status)}\n\t - content:\
 {status}\n\t - utf8 content: {status.decode()}")
