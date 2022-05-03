import pandas
from turtle import Screen,Turtle
screen=Screen()


def word_dict():
    file=pandas.read_csv("nato_phonetic_alphabet.csv")
    words={}
    for (index, word) in file.iterrows():
        words[word.letter]=word.code
    return words


def check_answer(answer,words):
    list=[words[letter] for letter in answer]
    return list


def show(i,list):
    state=Turtle()
    state.color("black")
    state.hideturtle()
    state.penup()
    state.goto(-400,200-i*20)
    state.write(f"{i}. {list}", False,font=("Courier", 12, "normal"))


def play_game():
    words=word_dict()
    print(words)
    i=0

    while True:

        answer = screen.textinput(f"NATO", "write your word")
        answer = (str(answer)).upper()

        try:
            if answer == "":
                raise KeyError

            for letter in answer:
                if not (letter in word_dict()):
                    raise KeyError
        except KeyError:
            print("sorry only letters please")
            continue


        list=check_answer(answer,words)
        i += 1
        show(i,list)

        if answer == "Exit":
            break

        if i==20:
          screen.clear()

play_game()
