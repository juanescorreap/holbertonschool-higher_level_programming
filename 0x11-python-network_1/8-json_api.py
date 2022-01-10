#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
import sys

if __name__ == "__main__":
	if len(sys.argv) < 2:
		value = {'q': ""}
	else:
		value = {'q': sys.argv[1]}

	r = requests.post('http://0.0.0.0:5000/search_user', data=value)
	try:
		answer = r.json()
		if len(answer) == 0:
			print("No result")
		else:
			print("[{}] {}".format(answer["id"], answer["name"]))
	except:
		print("Not a valid JSON")
    