from tkinter import *
from tkinter import messagebox
import math
import pandas
import random

from pandas import DataFrame

BACKGROUND_COLOR = "#B1DDC6"
data = pandas.read_csv("../Flip/data/german_translated.csv")
cards = data.to_dict(orient="records")

df=pandas.DataFrame(cards)
try:
    with open("../Flip/data/words_to_learn.csv") as file:
        pass
    data = pandas.read_csv("../Flip/data/words_to_learn.csv")
except:
    df.to_csv("../Flip/data/words_to_learn.csv", index=False)

finally:
        data=pandas.read_csv("../Flip/data/words_to_learn.csv")


cards = data.to_dict(orient="records")

current_card = {}
flipper = None


# ---------------------------- read data ------------------------------- #
def next_card():
    global current_card,flipper,cards

    if len(cards) == 0:
        canvas.itemconfig(language, text="Congratulations", fill="white")
        canvas.itemconfig(word, text="You Did it", fill="white")
        return

    if flipper is not None:
        window.after_cancel(flipper)
    current_card = random.choice(cards)
    german_word = current_card['German']
    canvas.itemconfig(language, text="German", fill="black")
    canvas.itemconfig(image, image=front)
    canvas.itemconfig(word, text=german_word, fill="black")

    flipper = window.after(3000, flip_card)


def flip_card():
    english_word = current_card['English']
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=english_word, fill="white")
    canvas.itemconfig(image, image=back)

def remove_card():
    global cards, current_card
    if len(cards)==0:
        canvas.itemconfig(language, text="Congratulations", fill="white")
        canvas.itemconfig(word, text="You Did it" , fill="white")
        return




    cards.remove(current_card)
    df = pandas.DataFrame(cards)
    df.to_csv("../Flip/data/words_to_learn.csv", index=False)

    next_card()



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy App")

w = int(window.winfo_screenwidth())
y = int(window.winfo_screenheight())
window.minsize(width=(math.floor(w // 1.65)), height=(math.floor(y / 1.35)))
window.maxsize(width=(math.floor(w // 1.65)), height=((math.floor(y / 1.35))))
window.config(background=BACKGROUND_COLOR, padx=80, pady=60)

canvas = Canvas(width=800, height=526)
# IMPORTANT: PhotoImage objects should not be created inside a function. Otherwise, it will not work.
front = PhotoImage(file="../Flip/images/card_front.png")
back = PhotoImage(file="../Flip/images/card_back.png")

image = canvas.create_image(400, 536 // 2, image=front)
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
language = canvas.create_text(400, 150, text="German", fill="black", font=("Helvet", w // 60, "italic"))
word = canvas.create_text(400, 260, text="Word", fill="black", font=("Helvet", w // 60, "bold"))
canvas.grid(row=0, column=1)

right_image = PhotoImage(file="../Flip/images/right.png")
right_button = Button(command=remove_card, image=right_image, width=100, height=100, highlightthickness=0)
right_button.grid(row=3, column=2)

wrong_image = PhotoImage(file="../Flip/images/wrong.png")
wrong_button = Button(command=next_card, image=wrong_image, width=100, height=100, highlightthickness=0)
wrong_button.grid(row=3, column=0)
next_card()

window.mainloop()
