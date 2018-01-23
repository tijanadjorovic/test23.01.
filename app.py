from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    """Home route handler."""
    page = """
    <!DOCTYPE html>
    <html>

    <head>
    </head>

    <body>
    <h1>Wecome!</h1>
        {}
    </body>

    </html>
    """
    return page.format(table)