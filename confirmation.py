import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("SELECT * FROM bookings")
    bookings = c.fetchall()
    conn.close()
    return render_template('index.html', bookings=bookings)

if __name__ == '__main__':
    app.run(debug=True)