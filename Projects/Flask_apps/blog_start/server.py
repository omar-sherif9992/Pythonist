from flask import Flask, render_template
import requests

app = Flask(__name__)
BLOG_POSTS_URL = "https://api.npoint.io/62a2728bed705969b759"
data = requests.get(url=BLOG_POSTS_URL).json()
print(data)


@app.route('/')
def home():
    return render_template("index.html", data=data)


@app.route('/contact')
def get_contact():
    return render_template("contact.html")


@app.route('/about')
def get_about():
    return render_template("about.html")


@app.route('/post/<int:day>')
def get_post(day):
    print(f"day {day}")
    day=str(day)
    return render_template("post.html",day=day ,data=data[day])



if __name__ == "__main__":
    app.run(debug=True)
