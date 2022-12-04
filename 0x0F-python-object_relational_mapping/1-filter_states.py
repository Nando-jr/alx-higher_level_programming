#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N)
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states \
            WHERE name LIKE BINARY 'N%' \
            ORDER BY states.id ASC")
    states = cur.fetchall()

    for state in states:
        print(state)
