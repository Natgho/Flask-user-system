# Author: Sezer Yavuzer Bozkir <admin@sezerbozkir.com>
# License: The GNU General Public License v3.0
# Created Date: 24.08.2017
# Version: 0.1
# Website: https://github.com/Natgho/Flask-user-system

from flask import Flask, flash, render_template, request, session, jsonify
from sqlalchemy.orm import sessionmaker
from db_conf import *
from werkzeug.security import generate_password_hash, check_password_hash # http://flask.pocoo.org/snippets/54/
app = Flask(__name__)


@app.route('/')
def home():
    """
    If user not logged in, redirect index page, else show Hello page.
    :return:
    """
    if not session.get('logged_in'):
        return render_template("index.html")
    else:
        return "Hello User.  <a href='/logout'>Logout</a>"


@app.route('/register', methods=['GET', 'POST'])
def user_register():
    """
    Check requests, If the registration request, save user else show register page.
    :return:
    """
    if request.method == 'POST':
        post_username = str(request.form['username'])
        post_password = generate_password_hash(str(request.form['password']))
        post_email = str(request.form['email'])
        post_country = str(request.form['country'])
        # return "{} {} {} {} ".format(post_username, post_password, post_email, post_country)
        user_session = sessionmaker(bind=engine)
        s = user_session()
        query = s.query(User).filter(User.username.in_([post_username]), User.password.in_([post_password]))
        result = query.first()
        # Check user if exist
        if result:
            flash('User Already registered!')
            return render_template('register.html')
        else:
            # Create user object and save database.
            tmp_user = User(post_username, post_password, post_email, post_country)
            s.add(tmp_user)
            s.commit()
            # s.close()
            return "User saved! <br><a href='/'>return Home</a"
            # return "{} {} {} {} ".format(POST_USERNAME, POST_PASSWORD, POST_EMAIL, POST_COUNTRY)
    else:
        return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Check request, Create a session if user information available else show login page.
    :return:
    """
    if request.method == 'POST':
        post_username = str(request.form['username'])
        post_password = str(request.form['password'])
        login_session = sessionmaker(bind=engine)
        s = login_session()
        query = s.query(User).filter(User.username.in_([post_username]))
        result = query.first()
        # Check the truth of the user information
        if result and check_password_hash(result.password, post_password):
            session['logged_in'] = True
        else:
            flash('Wrong username or password!')
        return home()
    else:
        return render_template('login.html')


@app.route('/get_countries', methods=['GET'])
def get_countries():
    """
    Get all countries from database.
    This method using for generate reply for AJAX request.
    :return:
    """
    country_session = sessionmaker(bind=engine)
    s = country_session()
    response = s.query(Country).all()
    country_schema = CountrySerializer(many=True)
    countries = country_schema.dump(response)
    return jsonify(countries.data)

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

# TODO Error page will be customized.
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('404.html'), 500

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=4000)
