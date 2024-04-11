# app.py
from flask import Flask, request, render_template, g, session, flash
from datetime import datetime

app = Flask(__name__)

# Temp mock database 
mock_database = {'aryan': '1234', 'jack': '2345'}
tracker_info = {}
highList = []
mediumList = []


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
    return render_template('main.html')

@app.route('/submit_mood', methods=['POST'])
def submit_mood():
    emotional_score = request.form.get('emotionalScore')
    cognitive_score = request.form.get('cognitiveScore')
    physical_score = request.form.get('physicalScore')
    mood_message = request.form.get('moodMessage')
    
    print(f"Emotional Score: {emotional_score}, Cognitive Score: {cognitive_score}, Physical Score: {physical_score}, Message: {mood_message}")

    return render_template('dashboard.html')


@app.route('/tracker', methods=['POST', 'GET'])
def tracker():
    mood = request.form["mood"]
    physical = request.form["physical"]
    cognitive = request.form["cognitive"]
    message = request.form["moodMessage"]
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    name = session.get('username')
    if mood < 4 or physical < 4 or cognitive < 4:
        highList.append(name)
    elif mood > 3 and mood < 5 or physical > 3 and physical < 5 or cognitive > 3 or cognitive < 5:
        mediumList.append(name)
        flash("A Nurse has been notified")
    tracker[name] = f"Emotional score: {mood}, Physical Score: {physical}, Cognitive score: {cognitive}, Message: {message} date and time:{dt_string}"
    return render_template("tracker.html")

@app.before_request
def login_handle():
    g.username = session.get('username')

@app.route("/nurses", methods=["GET", "POST"])
def nurses():
    return render_template("nurses.html")

@app.route("/cognitive_game", methods=["GET", "POST"])
def game():
    return render_template("game.html")
        

if __name__ == '__main__':
    app.run(debug=True)
