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
    user = [
        Comment('a','1111.11.11'),
        Comment('b','2222.22.22'),
        Comment('c','3333.33.33')
]
    return render_template('index.html', title='Comments', user=user, )



# @app.route("/api/v1.0/comments")
# def api_comments