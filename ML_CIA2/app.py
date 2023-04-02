import pickle
import pymysql
from flask import Flask, request, render_template, redirect, url_for, session
app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))
app.secret_key = "something"

wsgi_app = app.wsgi_app


@app.route("/")
def main():
    return render_template("login.html")


@app.route("/recommend")
def rec():
    return render_template("recommend.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = pymysql.connect(host="localhost", port=3306,
                               user="root", password="samsql123", db="ml_cia2")
        cur = conn.cursor()
        cur.execute(
            'SELECT * FROM details WHERE user_name=%s and passwords=%s', (username, password))
        user = cur.fetchone()
        if user:
            return render_template("recommend.html")
        else:
            error = "Invalid Username or Password"
            return render_template("login.html")
    return render_template("login.html")


@app.route("/predict", methods=['GET', 'POST'])
def pred():
    if request.method == 'POST':
        symboling = int(request.form['Symboling'])
        wheelbase = int(request.form['Enter Wheelbase'])
        carlen = int(request.form['Enter Car length'])
        carwid = int(request.form['Enter Car width'])
        carht = int(request.form['Enter Car height'])
        engsz = int(request.form['Enter Engine size'])
        hp = int(request.form['Enter Horse Power'])
        peakrpm = int(request.form['Enter Peak RPM'])
        citympg = int(request.form['Enter City MPG'])
        highmpg = int(request.form['Enter Highway MPG'])

        values = [symboling, wheelbase, carlen, carwid,
                  carht, engsz, hp, peakrpm, citympg, highmpg]

        pred = model.predict([values])
        return render_template("recommend.html")

    return render_template("login.html")


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
