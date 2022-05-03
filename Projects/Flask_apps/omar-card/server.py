from flask import Flask,render_template
from datetime import datetime
import requests
from Projects.Flask_apps.html_creator.main import html_text

app=Flask(__name__)
API_URL = "https://api.npoint.io/ed0b10721056718e1c18"
data = requests.get(url=API_URL).json()

@app.route("/")
def home():
    year=datetime.now().year
    return render_template('index.html',year=year)

@app.route("/guess/<name>")
def guess(name):
    GENDER_URL="https://api.genderize.io"
    AGE_URL="https://api.agify.io"
    params={"name":name}
    gender=requests.get(url=GENDER_URL,params=params).json()["gender"]
    age=requests.get(url=AGE_URL,params=params).json()["age"]
    message=html_text(f"Hey {name.title()},",flag=True,h1=True)
    message+=html_text(f"I think you are {gender}<br> and maybe {age} year old.",flag=True,h2=True)
    return message
@app.route("/blog")
def get_blog():
    return render_template("blog.html",data=data)

@app.route("/post/<path:day>")
def get_post(day):
    return render_template("post.html",title=day,data=data[day])


if __name__ == "__main__":
    app.run(debug=True)
