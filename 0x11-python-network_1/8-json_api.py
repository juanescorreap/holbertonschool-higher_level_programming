#!/usr/bin/python3
"""take URL, send a POST request to the passed URL
	with the email, and displays the body of the response
"""
import requests
from sys import argv

if __name__ == "__main__":
	if len(argv) < 2:
		value = {'q': ""}
	else:
		value = {'q': argv[1]}
	try:
		url = 'http://0.0.0.0:5000/search_user'
		response = requests.post(url, value)
		json = response.json()
		if len(json) == 0:
			print("No result")
		else:
			print("[{}] {}".format(json["id"], json["name"]))
	except:
		print("Not a valid JSON")
