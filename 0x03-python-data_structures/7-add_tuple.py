#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
	i = 0
	while i < len(tuple_a):
		new_tuple = tuple_a[i] + tuple_b[i]
		i = i + 1
	return(new_tuple)