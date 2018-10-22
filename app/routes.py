from flask import render_template
from app import app


@app.route('/')
def index():
    return render_template('index.html', title='Coming soon')


@app.route('/event')
def event():
    return render_template('event.html', title="Event")
