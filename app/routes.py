from flask import render_template, url_for, flash
from werkzeug.utils import redirect

from app import app
from flask_login import current_user, login_user, logout_user, login_required

from app.forms import LoginForm
from app.models import User

@app.route('/')
@app.route('/index')
@login_required
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/event")
def event():
    return render_template("event.html", title="Event")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
