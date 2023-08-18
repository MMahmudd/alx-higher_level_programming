#!/usr/bin/python3
"""
Accepts_the_name of_a_state as argument_and_lists all_cities of_that
state_using_the_database hbtn_0e_4_usa.
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset='utf8')
    cur = db.cursor()
    cur.execute("SELECT * FROM `cities` as `cur` \
                INNER JOIN `states` as `st` \
                ON `cur`.`state_id` = `st`.`id` \
                ORDER BY `cur`.`id`")
    print(", ".join([ct[2] for ct in cur.fetchall() if ct[4] == argv[4]]))
