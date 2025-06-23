import sqlite3

conn = sqlite3.connect("database.db")
conn.execute('''
Create table users(
useid integer primary key autoincrement,
username varchar(100),
password varchar(100),
)
''')
conn.close()

