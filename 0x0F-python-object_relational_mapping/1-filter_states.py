#!/usr/bin/python3
"""  list all states based on the first name  """
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY'N%'"
                " ORDER BY states.id")
    for rowVal in cur.fetchall():
        print(rowVal)
