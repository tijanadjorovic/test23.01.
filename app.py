"""Flask app."""

from flask import Flask
from models import Comment
from flask import render_template

app = Flask(__name__)

@app.route("/")
# def index():
#     print "Welcome!"

@app.route("/comments")
def comments():
    user = {'username': 'Miguel'}
    print render_template('index.html', title='Home', user=user)



# @app.route("/api/v1.0/comments")
# def api_comments