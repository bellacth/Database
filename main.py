import sqlite3
from flask import Flask, render_template, request
from flask import redirect, url_for
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
        return redirect(url_for('successful_register'))
    return render_template('signup.html')

@app.route('/successful_register')
def successful_register():
    return render_template('successful_register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute("SELECT * FROM customer WHERE username=? AND password=?", (username, password))
        user = c.fetchone()
        conn.commit()
        conn.close()

        if user:
            return redirect(url_for('successful_login'))
        else:
            return render_template('login.html', error=True)
    else:
        return render_template('login.html', error=False)

@app.route('/successful_login')
def successful_login():
    return render_template('successful_login.html')

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
        return redirect(url_for('successful_booking'))
    return render_template('reservation.html')

@app.route('/successful_booking')
def successful_booking():
    return render_template('successful_booking.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/staff_login', methods=['GET', 'POST'])
def staff_login():
    if request.method == 'POST':
        code = request.form['code']
        if code == 'TorcityStaff1234':
            return redirect(url_for('staff_home'))
        else:
            return render_template('staff_login.html', error=True)
    else:
        return render_template('staff_login.html', error=False)

@app.route('/staff_home')
def staff_home():
    return render_template('staff_home.html')

@app.route('/staff_booking')
def staff_booking():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM booking")
    data = c.fetchall()
    conn.close()
    return render_template('staff_booking.html', data=data)

@app.route('/staff_customer')
def staff_customer():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM customer")
    data = c.fetchall()
    conn.close()
    return render_template('staff_customer.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
