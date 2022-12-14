#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa where name matches
the argument. But this time, write one that is safe from MySQL injections!
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           password=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states WHERE BINARY name
            LIKE %(name)s ORDER BY states.id""", {'name': argv[4]})
    states = cur.fetchall()

    for state in states:
        print(state)
