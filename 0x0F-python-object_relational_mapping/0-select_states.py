#!/usr/bin/python3
"""It list all state from database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = mycursor.fetchall()
    for row in rows:
        print(row)
        
    mycursor.close()
    db.close()
