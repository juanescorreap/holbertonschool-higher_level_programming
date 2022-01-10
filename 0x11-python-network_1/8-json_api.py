#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter."""


if __name__ == "__main__":
    import requests
    import sys
    if len(sys.argv) < 2:
        value = ""
    else:
        value = sys.argv[1]
    data = {'q': value}

    r = requests.post('http://0.0.0.0:5000/search_user', data)
    try:
        answer = r.jason()
        if len(answer) == 0:
            print("No result")
        else:
            print("[{}] {}".format(answer["id"], answer["name"]))
    except:
        print("Not a valid JSON")
