#!/usr/bin/python3
"""list states starting with N from hbtn_0e_0usa database"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id")
    rows = mycursor.fetchall()
    for item in rows:
        print(item)
    mycursor.close()
    db.close()
