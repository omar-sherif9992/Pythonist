from Projects.Flask_apps.html_creator.main import html_text
from flask import Flask
import random
NUMBERS_GIF="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"
HIGH_GIF="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
LOW_GIF=" https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
EQUAL_GIF="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"

choosen=random.randint(0,9)

app=Flask(__name__)

@app.route('/')
def display():
    return html_text("Guess a number between 0 and 9",flag=True,h1=True,img=True,src=NUMBERS_GIF)
@app.route('/<int:num>')
def check(num:int):
    if num<choosen:
        return html_text(f"<p style='color:red'>Number {num} is too low</p>", flag=True, h1=True, img=True, src=LOW_GIF)
    elif num>choosen:
        return html_text(f"<p style='color:red'>Number {num} is too high</p>", flag=True, h1=True, img=True, src=HIGH_GIF)
    return html_text(f"<p style='color:green'>Hooray You got it right<br>it's {num}</p>",flag=True,h1=True,img=True,src=EQUAL_GIF)


if __name__ == "__main__":
    app.run(debug=True)
