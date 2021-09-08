#!/usr/bin/python3
if __name__ == "__main__":
	import hdden_4
	for element in dir(hidden_4):
		if element[0:2] != "__":
			print("{:s}".format(element))
