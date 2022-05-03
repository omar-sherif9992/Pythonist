import pandas,turtle
from turtle import Turtle,Screen
screen=Screen()
screen.title("U.S States Game")
image="/home/omar/PycharmProjects/Python-Projects/Projects/Automate_Projects/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(700,500)


def state():
    data=pandas.read_csv("/home/omar/PycharmProjects/Python-Projects/Projects/Automate_Projects/us-states-game-start/50_states.csv")
    states=data["state"].tolist()
    return states


def coordinate():
    data=pandas.read_csv("/home/omar/PycharmProjects/Python-Projects/Projects/Automate_Projects/us-states-game-start/50_states.csv")
    coord=[]
    x=data["x"].tolist()
    y=data["y"].tolist()
    for i in range(0,len(x)):
        coord.append((x[i],y[i]))
    return coord





def show_state(answer,coord):
    state=Turtle()
    state.color("black")
    state.hideturtle()
    state.penup()
    state.goto(coord)
    state.write(f"{answer}".title(), False,font=("Courier", 12, "normal"))


def play_game():
    states=state()
    states.sort()
    coordinates=coordinate()

    correct_answer = 0
    while correct_answer<50:
        answer=screen.textinput(f"Guess the State {correct_answer}/50","Guess the state's name")
        answer=(str(answer)).title()
        if answer in states:
            correct_answer+=1
            show_state(answer,coordinates[states.index(answer)])
            states.remove(answer)
        if answer=="Exit":
            break

    states_dict={"states":states}
    df=pandas.DataFrame(states_dict)
    df.to_csv("Missed States.csv")

play_game()
