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
            return redirect(url_for("pred"))
        else:
            error = "Invalid Username or Password"
            return render_template("login.html")
    return render_template("login.html")


@app.route("/predict", methods=['GET', 'POST'])
def pred():
    if request.method == 'POST':
        symboling = int(request.form['symboling'])
        wheelbase = int(request.form['wheelbase'])
        carlen = int(request.form['carlength'])
        carwid = int(request.form['carwidth'])
        carht = int(request.form['carheight'])
        engsz = int(request.form['enginesize'])
        hp = int(request.form['horsepower'])
        peakrpm = int(request.form['peakrpm'])
        citympg = int(request.form['citympg'])
        highmpg = int(request.form['hmpg'])

        values = [symboling, wheelbase, carlen, carwid,
                  carht, engsz, hp, peakrpm, citympg, highmpg]

        pred = model.predict([values])
        return render_template("recommend.html", price=pred[0])
    else:
        return render_template("recommend.html", price="0")


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
