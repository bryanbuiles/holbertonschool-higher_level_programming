#!/usr/bin/python3
""" scripts that list all states """

import MySQLdb
import sys


def states():
    """ List from data base
    """

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()

    cur.execute(
        "SELECT * FROM states WHERE BINARY name = '{:s}'\
            ORDER BY id ASC".format(sys.argv[4]))

    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    db.close()


if __name__ == "__main__":
    states()
