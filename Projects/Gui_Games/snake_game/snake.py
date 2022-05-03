import turtle
from turtle import Turtle, Screen

MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.intial_snake()

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def intial_snake(self):
        """creates the intial snack body consisting of three blocks """
        x = 0
        for i in range(0, 3):
            segement_1 = Turtle("square")
            segement_1.color("dark green")
            if i == 0:
                segement_1.shape("arrow")
            segement_1.penup()
            segement_1.setx(x)
            x -= 20
            self.segments.append(segement_1)

    def move(self):
        """creates the continous movement of the snake segments"""
        for seq_index in range(len(self.segments) - 1, 0, -1):
            self.segments[seq_index].goto(self.segments[seq_index - 1].xcor(), self.segments[seq_index - 1].ycor())
        self.segments[0].forward(MOVE_DISTANCE)

    def add_segment(self):
        added_segment = Turtle("square")
        added_segment.color("dark green")
        added_segment.penup()
        added_segment.goto(self.segments[len(self.segments)-1].position())
        self.segments.append(added_segment)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.intial_snake()
