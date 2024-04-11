# app.py
from flask import Flask, request, render_template

app = Flask(__name__)

# Temp mock database 
mock_database = {'aryan': '1234', 'jack': '2345'}


@app.route('/form_login', methods=['POST', 'GET'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username not in mock_database:
        return render_template('login.html', info="Invalid user")
    else:
        if mock_database[username] != password:
            return render_template('login.html', info="Invalid Password")
        else:  
            return render_template("main.html", name=username)


@app.route('/')
def home():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
