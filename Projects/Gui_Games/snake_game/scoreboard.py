from turtle import Turtle
from logo import logo
import high_score_controller

class ScoreBoard(Turtle):
    def __init__(self, name):
        super().__init__()
        self.score = 0
        self.high_score =int(high_score_controller.read_content("high_score_file"))
        self.name = name
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.write(f"{self.name} Score : {self.score} High Score : {self.high_score}".title(), False, align="center", font=("Courier", 28, "normal"))

    def score_up(self):
        self.score += 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"{self.name} Score : {self.score} High Score : {self.high_score}".title() , False, align="center", font=("Arial", 30, "normal"))

    def game_over(self):
        self.clear()
        self.shapesize(15, 15)
        self.goto(110, -200)

        self.write(f"{logo} \n Game Over !! \n \n {self.name} Score : {self.score}".title(), False, align="center", font=("Arial", 30, "normal"))

    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            high_score_controller.rewrite_content("high_score_file", self.high_score)
        self.score=0
        self.update()

