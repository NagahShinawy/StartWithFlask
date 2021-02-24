from flask import Flask
from random import randint


app = Flask(__name__)


@app.route('/')
def home():
    return f"Your Number is: {randint(1, 6)}"


if __name__ == '__main__':
    app.run(debug=True, port=5050)