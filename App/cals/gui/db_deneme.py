#!/usr/bin/python
#

import shelve


def main():
    db = shelve.open("vehicles.db")
    dkeys = list(db.keys())
    dkeys.sort()
    for x in dkeys:
        print(x)
    db.close()
    return


if __name__ == "__main__":
    main()
