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

    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities JOIN states ON\
                    cities.state_id=states.id ORDER BY cities.id ASC")

    rows = cur.fetchall()
    for i in rows:
        print(i)
    cur.close()
    db.close()


if __name__ == "__main__":
    states()
