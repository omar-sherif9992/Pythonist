import random
from turtle import Turtle
class Blocks(Turtle):
    def __init__(self):
        super().__init__()
        super().__init__()
        self.shape("square")
        self.color("dim gray")
        self.speed(0)
        self.penup()
        self.shapesize(0.5, 0.5)
        self.goto(random.randint(-280, 280), random.randint(-280, 230))

