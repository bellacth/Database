import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()

c.execute('''ALTER TABLE booking ADD COLUMN bank_account TEXT''')
conn.commit()
conn.close()



