"""Flask APP."""

from flask import Flask
from flask import render_template
from flask import jsonify

from models import COMMENTS

app = Flask(__name__)


@app.route("/")
# def index():
#     print "Welcome!"

@app.route('/comments')
def comments():
    return render_template('index.html', data=COMMENTS)


@app.route('/api/v1.0/comments', methods=['GET'])
def api_comments():
    result = []
    for comment in COMMENTS:
        comment_dict = {
            "TEXT": comment.text,
            "DATE": comment.date
        }
        result.append(comment_dict)
    return jsonify({'comments': result})