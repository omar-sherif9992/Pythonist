from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, name):
        super().__init__()
        self.level = 0
        self.score = 0
        self.name = name
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-570, 370)
        self.write(f"level : {self.level}\n{self.name} Score : {self.score}".title(), False, align="left",
                   font=("Arial", 20, "normal"))

    def score_up(self):
        self.level += 1
        self.score += 1
        self.clear()
        self.write(f"level : {self.level}\n{self.name} Score : {self.score}".title(), False, align="left",
                   font=("Arial", 20, "normal"))

    def game_over(self):
        self.clear()
        self.shapesize(15, 15)
        self.goto(0, 0)

        self.write(f"Game Over !! \n \n {self.name} Score : {self.score}".title(), False, align="center",
                   font=("Arial", 30, "normal"))
