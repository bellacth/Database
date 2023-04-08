import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()

c.execute('''DELETE FROM booking
WHERE room_type = single;''')



