import random
from turtle import Turtle

COLORS = ["red", "orange", "green", "yellow", "blue", "purple", "cyan"]
MOVE_DISTANCE = 10
CARS_LINES = []


def generate_lines():
    for i in range(0, 7):
        CARS_LINES.append(-350 + i * 110)


generate_lines()


class Car:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle("square")
            new_car.speed(0)
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(550, random.choice(CARS_LINES))
            self.all_cars.append(new_car)

    def move(self):
        for c in self.all_cars:
            c.forward(MOVE_DISTANCE)

    def level_up(self):
        global MOVE_DISTANCE
        MOVE_DISTANCE += 5
