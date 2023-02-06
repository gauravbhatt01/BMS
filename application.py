from urllib import request
from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def main(name=None):
    return render_template('main.html', name=name)

@app.route("/login", methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    else:
        return render_template("login.html")
    
    return render_template('login.html', errror=error)
