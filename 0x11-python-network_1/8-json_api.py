#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter."""

if __name__ == "__main__":
    import requests
    import sys
    r = requests.post('http://0.0.0.0:5000/search_user',
                      data={'q': sys.argv[1]})
    try:
        answer = r.jason()
        if len(answer) == 2:
            print("[{}] {}".format(answer["id"], answer["name"]))
        else:
            print("No result")
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
