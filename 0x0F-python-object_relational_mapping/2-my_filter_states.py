#!/usr/bin/python3
"""Takes an argument and displays matching values"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                     user=sys.argv[1],
                     passwd=sys.argv[2],
                     db=sys.argv[3],
                     port=3306)
    mycur = db.cursor()
    mycur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                  .format(sys.argv[4]))
    rows = mycur.fetchall()
    for row in rows:
        print(row)
    mycur.close()
    db.close()
