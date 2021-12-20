#!/usr/bin/python3
""" script that lists all states
from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
	database = MySQLdb.connect(host='localhost', port=3306,
							user=argv[1], passwd=argv[2], db=argv[3])
	cursor = database.cursor()
	cursor.execute('SELECT id, name FROM states ORDER BY states.id ASC')
	for states in cursor.fetchall():
		print(states)
		cursor.close()
		database.close()
