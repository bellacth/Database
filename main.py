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

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        full_name = request.form['full_name'],
        phone_number = request.form['phone_number'],
        email = request.form['email'],
        username = request.form['username'],
        password = request.form['password'],

        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute("INSERT INTO customer(full_name, phone_number, email, username, password) VALUES(?,?,?,?,?)", (str(full_name), str(phone_number), str(email), str(username), str(password)))
        conn.commit()
        conn.close()

        return 'registered account'
    return render_template('signup.html')

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

@app.route('/staff')
def staff():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM booking")
    data = c.fetchall()
    conn.close()
    return render_template('staff.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

'''
@app.route('/staff', methods=['GET'])
def staff():
    c = conn.cursor()
    c.execute("SELECT * FROM booking")
    data = c.fetchall()
    conn.commit()
    conn.close()
    return render_template('staff.html', data=data)
    '''