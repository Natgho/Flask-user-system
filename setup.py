# Author: Sezer Yavuzer Bozkir <admin@sezerbozkir.com>
# License: The GNU General Public License v3.0
# Created Date: 24.08.2017
# Version: 0.1
# Website: https://github.com/Natgho/Flask-user-system

from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from db_conf import *

app = Flask(__name__)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template("index.html")
    else:
        return "Hello User.  <a href='/logout'>Logout</a>"

@app.route('/register', methods=['GET','POST'])
def user_register():
    if request.method == 'POST':
        POST_USERNAME = str(request.form['username'])
        POST_PASSWORD = str(request.form['password'])
        POST_EMAIL = str(request.form['email'])
        POST_COUNTRY = str(request.form['country'])
        Session = sessionmaker(bind=engine)
        s = Session()
        query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]))
        result = query.first()
        if result:
             flash('User Already registered!')
             return render_template('register.html')
        else:
            tmp_user = User(POST_USERNAME, POST_PASSWORD, POST_EMAIL, POST_COUNTRY)
            s.add(tmp_user)
            s.commit()
            # s.close()
            return "User saved!"
        # return "{} {} {} {} ".format(POST_USERNAME, POST_PASSWORD, POST_EMAIL, POST_COUNTRY)
    else:
        return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        POST_USERNAME = str(request.form['username'])
        POST_PASSWORD = str(request.form['password'])
        Session = sessionmaker(bind=engine)
        s = Session()
        query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]))
        result = query.first()
        if result:
            session['logged_in'] = True
        else:
            flash('Wrong username or password!')
        return home()
    else:
        return render_template('login.html')


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=4000)