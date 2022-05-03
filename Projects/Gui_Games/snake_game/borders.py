from turtle import Turtle

class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("saddle brown")
        self.speed(0)
        self.pensize(7)
        self.penup()
        self.goto(-280,-280)
        self.pendown()
        self.goto(-280,250)
        self.goto(280, 250)
        self.goto(280, -280)
        self.goto(-280,-280)

        self.color("black")
        self.speed(0)
        self.pensize(3)
        self.penup()
        self.goto(-280, -280)
        self.pendown()
        self.goto(-280, 250)
        self.goto(280, 250)
        self.goto(280, -280)
        self.goto(-280, -280)