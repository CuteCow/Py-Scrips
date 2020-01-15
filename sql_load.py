# -*- coding: utf-8 -*-

import csv, sqlite3
conn = sqlite3.connect(r'C:\users\me\desktop\test1.db')
curs = conn.cursor()
curs.execute("CREATE TABLE links1 (path TEXT, book TEXT, targpath TEXT, target TEXT);")
reader = csv.reader(open(r'C:\Users\Me\Desktop\Links.csv', 'r'), delimiter=',')
for row in reader:
    to_db = [row[0], row[1], row[2], row[3]]
    print (to_db)
    curs.execute("INSERT INTO links1 (path, book, targpath, target) VALUES (?, ?, ?, ?);", to_db)
conn.commit()
