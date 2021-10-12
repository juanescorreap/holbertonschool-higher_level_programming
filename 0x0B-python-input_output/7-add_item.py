#!/usr/bin/python
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


my_list = []
my_list.append(sys.argv)

load_from_json_file("add_item.json")
save_to_json_file(my_list, "add_item.json")
