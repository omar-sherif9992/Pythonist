import random
from turtle import Turtle


class Apple(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.speed(0)
        self.penup()
        self.shapesize(0.5, 0.5)
        self.goto(random.randint(-270, 270), random.randint(-270, 230))

    def change_location(self):
        self.goto(random.randint(-270, 270), random.randint(-270, 230))
