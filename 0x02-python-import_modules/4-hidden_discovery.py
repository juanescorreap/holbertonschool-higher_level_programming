#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
	for element in dir(hidden_4):
		if element[0:2] != "__":
			print("{:s}".format(element))