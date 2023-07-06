from utils.search import flipkartSearch, amazonSearch
from utils.proccess import populate_data
from flask import Flask, render_template
from flask import request
import pandas as pd

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":

        q = request.form["nm"]

        data_list1 = flipkartSearch(q)
        data_list2 = amazonSearch(q)
        while not data_list2:
            data_list2 = amazonSearch(q)

        data = populate_data(data_list1, data_list2)

        values = list(data.values)
        data.to_csv('logs/datalog.csv')
        return render_template('index.html', stocklist=values)
    else:
        return render_template("index.html")


@app.route('/stocks')
def Stocks():
    key = "YO"
    filename = 'flipkartandamazon.csv'
    data = pd.read_csv(filename, header=0)
    values = list(data.values)
    return render_template('stocks.html', stocklist=values, key=key)


@app.route("/<usr>")
def user(usr):

    return f"<h1>{usr}</h1>"


if __name__ == "__main__":
    app.run(debug=True)
