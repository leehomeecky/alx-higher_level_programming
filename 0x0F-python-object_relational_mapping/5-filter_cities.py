#!/usr/bin/python3
""" script that takes name of a state and lists all cities """

import sys
import MySQLdb

if __name__ == "__main__":
   db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
   cur = db.cursor()
   cur.execute("SELECT cities.name "
               "FROM cities WHERE cities.state_id = "
               "(SELECT id FROM states WHERE name LIKE BINARY %s)"
               " ORDER BY cities.id", (sys.argv[4], ))
   result = [rowVal[0] for rowVal in cur.fetchall()]
   print(*result, sep=", ")
