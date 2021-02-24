from flask import Flask, make_response, url_for
import requests
import os


app = Flask(__name__)


@app.route("/")
def home():
    return f"Please Try <a href='{(url_for('stock', ticker='AAPL'))}' target='_blank'>Stock<a>"


@app.route('/stock/<string:ticker>/')
def stock(ticker):
    ticker_url = os.environ.get("STOCK_URL").format(ticker)
    response = requests.get(ticker_url, params={"apikey": "demo"})
    if response.status_code == 200:
        return response.json()
    return make_response("Something went wrong", response.status_code)


if __name__ == '__main__':
    app.run(debug=True, port=5051)