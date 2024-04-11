# app.py
from flask import Flask, request, render_template

app = Flask(__name__)

# Temp mock database 
mock_database = {'a': '1234', 'n': '1234', 'v': '1234'}


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
            # Check which button was pressed
            if 'User In' in request.form:
                return render_template("user_page.html", name=username)
            elif 'Nurse Login' in request.form:
                return render_template("nurse_page.html", name=username)
            elif 'Volunteer Login' in request.form:
                return render_template("volunteer_page.html", name=username)
            

@app.route('/')
def home():
    return render_template('v_main.html')


if __name__ == '__main__':
    app.run(debug=True)
