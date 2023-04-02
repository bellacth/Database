import sqlite3
from flask import Flask, render_template, request
app = Flask(__name__)

#connect to sqlite
conn = sqlite3.connect('data.db')

#establishing cursor
c = conn.cursor()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/reservation', methods=['GET', 'POST'])
def reservation():
    if request.method == 'POST':
        full_name = request.form['full_name'],
        people_quantity = request.form['people_quantity'],
        room_quantity = request.form['room_quantity'],
        room_type = request.form['room_type'],
        entry_date = request.form['entry_date'],
        exit_date = request.form['exit_date'],

        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute("INSERT INTO booking(full_name, people_quantity, room_quantity, room_type, entry_date, exit_date) VALUES(?,?,?,?,?,?)", (str(full_name), str(people_quantity), str(room_quantity), str(room_type), str(entry_date), str(exit_date)))
        conn.commit()
        conn.close()

        return 'successfully booked'
    return render_template('reservation.html')