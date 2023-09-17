#!/usr/bin/python3
"""  list all cites with its states"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    value = sys.argv[4]
    cur = db.cursor()
    cur.execute("SELECT cities.name "
                "FROM cities WHERE cities.state_id = "
                "(SELECT id FROM states WHERE name LIKE BINARY %s)"
                " ORDER BY cities.id", (value, ))

    val = list(rowVal[0] for rowVal in cur.fetchall())
    print(*val, sep=", ")
    cur.close()
    db.close()