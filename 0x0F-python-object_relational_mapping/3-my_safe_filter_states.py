#!/usr/bin/python3
"""Displays matching value where name matches argument"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    mycur = db.cursor()
    match = sys.argv[4]
    mycur.execute("SELECT * FROM states WHERE name LIKE %s", (match,))
    rows = mycur.fetchall()
    for row in rows:
        print(row)
    mycur.close()
    db.close()
