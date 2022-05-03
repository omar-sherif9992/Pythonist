from turtle import Turtle

class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.speed(0)
        self.pensize(7)
        self.penup()
        self.goto(-610,370)
        self.pendown()
        self.drawing_dashed_line()

    def drawing_dashed_line(self):
        """draw a dashed line vertically in the center of the screen"""
        self.penup()
        self.speed(0)
        for i in range(200):
            if i % 2 == 0:
                self.penup()
            else:
                self.pendown()
            self.forward(10)