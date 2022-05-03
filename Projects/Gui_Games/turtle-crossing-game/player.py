import random
from turtle import Turtle

MOVE_UP = 20
FINISH_LINE_Y = 370
STARTING_POSITION = (0, -400)


class Player(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.speed(0)
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.forward(MOVE_UP)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def move_down(self):
        self.backward(MOVE_UP)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
