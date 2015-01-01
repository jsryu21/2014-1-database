#!/usr/bin/env python

def CleanDaily():
	import MySQLdb
	db = MySQLdb.connect(db="dbproject", user="root", passwd="asdf1234", use_unicode=True, charset="utf8")
	cur = db.cursor()
	cur.execute("DELETE FROM daily_batter")
	cur.execute("DELETE FROM daily_pitcher")
	db.commit()

if __name__ == "__main__":
	CleanDaily()
