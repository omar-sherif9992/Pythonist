from turtle import Turtle, Screen
import turtle as t

tim = Turtle()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def move_counterclockwise():
    tim.setheading(tim.heading() - 10)


def move_clockwise():
    tim.setheading(tim.heading() + 10)
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def play_game():

    screen = Screen()
    screen.title("Etch & Sketch Game")
    screen.listen()  # in order to be able to register key-events, TurtleScreen must have the focus
    screen.onkeypress(move_forward, "Up")  # # Notice that we passed a function as a parameter with no arguments
    screen.onkeypress(move_backward, "Down")  # # Notice that we passed a function as a parameter with no arguments
    screen.onkeypress(move_counterclockwise, "Left")
    screen.onkeypress(move_clockwise, "Right")
    screen.onkeypress(move_clockwise, "Right")
    screen.onkeypress(clear,key="c")
    screen.exitonclick()


play_game()
