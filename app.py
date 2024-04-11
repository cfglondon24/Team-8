# app.py
from flask import Flask, request, render_template, g, session, flash
from datetime import datetime

app = Flask(__name__)

# Temp mock database 
mock_database = {'aryan': '1234', 'jack': '2345'}
tracker_info = {}
flaggedList = []


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

@app.route('/tracker', methods=['POST', 'GET'])
def tracker():
    mood = request.form["mood"]
    physical = request.form["physical"]
    cognitive = request.form["cognitive"]
    message = request.form["moodMessage"]
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    name = session.get('username')
    if mood < 5 or physical < 5 or cognitive < 5:
        flaggedList.append(name)
        flash("A Nurse has been notified")
    tracker[name] = f"mood: {mood}, physical: {physical}, cognitive: {cognitive}, Message: {message} date and time:{dt_string}"
    return render_template("tracker.html")

@app.before_request
def login_handle():
    g.username = session.get('username')

@app.route("/home", methods=["POST"])
def home():
    return render_template("dashboard.html")

@app.route("/nurses", methods=["GET", "POST"])
def nurses():
    return render_template("nurses.html")

@app.route("/cognitive_game", methods=["GET", "POST"])
def game():
    return render_template("game.html")
        

if __name__ == '__main__':
    app.run(debug=True)
