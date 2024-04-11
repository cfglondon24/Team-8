# app.py
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "this is a sample app"


if __name__ == '__main__':
    app.run(debug=True)
