import requests
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def home():
    username = request.cookies.get('username')
    return render_template("contact_forum.html", username=username)


@app.route("/login", methods=["POST"])
def login():
    user = request.form['username']
    password=request.form["password"]
    f = request.files["file"]

    if f.filename != "":
        print(f.filename + "is downloaded successfully")
        f.save(f'{secure_filename(f.filename)}')
    return f"<h1>Username:" \
           f"{user}</h1><h1>Password: {password}</h1>"


if __name__ == "__main__":
    app.run(debug=True)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
