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
    return render_template('diary.html')

@app.route('/submit_mood', methods=['POST'])
def submit_mood():
    emotional_score = request.form.get('emotionalScore')
    cognitive_score = request.form.get('cognitiveScore')
    physical_score = request.form.get('physicalScore')
    mood_message = request.form.get('moodMessage')
    
    print(f"Emotional Score: {emotional_score}, Cognitive Score: {cognitive_score}, Physical Score: {physical_score}, Message: {mood_message}")

    return render_template('user_personal_dashboard.html')


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
