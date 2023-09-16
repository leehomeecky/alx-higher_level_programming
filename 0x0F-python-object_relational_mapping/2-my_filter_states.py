#!/usr/bin/python3
""" a script that takes in an argument and displays all values """
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' "
                "ORDER BY states.id"
                .format(sys.argv[4]))
    for rowVal in cur.fetchall():
        print(rowVal)
