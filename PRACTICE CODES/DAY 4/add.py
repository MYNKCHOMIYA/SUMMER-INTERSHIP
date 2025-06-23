import sqlite3

conn = sqlite3.connect("database.db")
conn.execute('''
insert into users(username, password)
values('admin', 'admin123')
''')
conn.commit()
