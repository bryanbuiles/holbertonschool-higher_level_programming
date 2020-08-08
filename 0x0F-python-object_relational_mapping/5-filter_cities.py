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

    cur.execute("SELECT cities.name\
                FROM cities JOIN states ON\
                    cities.state_id=states.id WHERE states.name = '{:s}'\
                        ORDER BY cities.id ASC".format(sys.argv[4]))

    rows = cur.fetchall()

    lista = []
    for i in rows:
        lista.append(i[0])

    print(", ".join(lista))
    cur.close()
    db.close()


if __name__ == "__main__":
    states()
