import random
from time import sleep
from turtle import Screen, Turtle

screen = Screen()
screen.title("Turtle Race Game")


def drawing_dashed_line(tim):
    """draw a dashed line vertically in the center of the screen"""
    tim.shape("turtle")
    tim.penup()
    tim.left(90)
    tim.speed(0)
    tim.setx(430)
    tim.sety(-400)
    for i in range(80):
        if i % 2 == 0:
            tim.penup()
        else:
            tim.pendown()
        tim.forward(10)


def play_game():
    screen.setup(width=900, height=500)
    colors = ["yellow", "green", "blue", "purple", "red", "black"]
    all_turtles = []

    for i in range(0, len(colors)):
        tim = Turtle("turtle")
        tim.color(colors[i])
        tim.penup()
        tim.goto(-250, -80 + i * 40)
        all_turtles.append(tim)
    user = screen.textinput("Make your bet", "which color you will choose!")

    while not user:
        user = screen.textinput("Make your bet", "please enter your")

    flag = False
    winner = ""

    for i in range(1, 4):
        tim = Turtle()
        tim.hideturtle()
        tim.write(f"{i}!", False, align="center", font=("Arial", 30, "normal"))
        sleep(1)
        tim.clear()

    drawing_dashed_line(Turtle())

    while user:
        i = 0
        for turtle in all_turtles:
            turtle.forward(random.randint(5, 15))
            if turtle.xcor() >= 420:
                flag = True
                winner = colors[i]
                break
            i += 1
        if flag:
            break

    screen.clear()
    tim = Turtle()
    tim.hideturtle()
    if user == winner:
        tim.write(f"You've won! the winner is {winner}", False, align="center", font=("Arial", 30, "normal"))
    else:
        tim.write(f"You've losed! the winner is {winner}", False, align="center", font=("Arial", 30, "normal"))

    screen.exitonclick()


play_game()
while str(input("Do you want to play again? 'Yes' or 'No'")) == "Yes":
    play_game()
