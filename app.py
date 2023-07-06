from utils.userdata import verifyUser, addUser
from utils.search import flipkartSearch, amazonSearch
from utils.proccess import populate_data
from flask import Flask, render_template, redirect, url_for
from flask import request
import pandas as pd
import time


app = Flask(__name__)


@app.route('/')
def home():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        if verifyUser(username, password):
            return redirect(url_for('search'))

        return render_template('login.html')

    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        if addUser(username, password, email):
            return redirect(url_for('search'))

        return redirect(url_for('signup'))

    return render_template('signup.html')


@app.route("/search", methods=["POST", "GET"])
def search():
    if request.method == "POST":

        q = request.form["product_name"]

        data_list1 = flipkartSearch(q)
        data_list2 = amazonSearch(q)

        # fix for traffic error
        t_end = time.time() + 10
        while not data_list2 and time.time() < t_end:
            data_list2 = amazonSearch(q)

        data = populate_data(data_list1, data_list2)

        values = list(data.values)
        data.to_csv('logs/datalog.csv')
        return render_template('index.html', stocklist=values)

    return render_template("index.html")


@app.route('/stocks')
def Stocks():
    filename = 'logs/datalog.csv'
    data = pd.read_csv(filename)
    data.pop('Unnamed: 0')
    values = list(data.values)
    return render_template('stocks.html', stocklist=values)


@app.route("/<usr>")
def user(usr):
    x = "127.0. 0.1:5000/" + usr
    return f"<h1>Please check the URL once : {x}</h1>"


if __name__ == "__main__":
    app.run()
