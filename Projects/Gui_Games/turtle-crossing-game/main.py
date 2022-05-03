import time
from finishing_line import Line
from turtle import Screen
from player import Player
from scoreboard import ScoreBoard
from car import Car


screen = Screen()
screen.setup(1200, 900)

screen.bgcolor("white")
screen.title("Turtle Crossing Game")
screen.tracer(0)


def game_over(cars, player):
    for car in cars.all_cars:
        if car.distance(player) < 20:
            return False
    return True


def play_game():
    Line()
    player = Player()
    user = screen.textinput("Turtle Name", "please enter your name")
    score =ScoreBoard(user)
    screen.listen()
    screen.onkey(player.move_up, "Up")
    screen.onkeypress(player.move_down, "Down")
    Line()

    cars = Car()

    while True:
        cars.create_car()
        cars.move()
        time.sleep(0.1)
        screen.update()

        if not game_over(cars, player):
            score.game_over()
            break

        if player.is_at_finish_line():
            cars.level_up()
            player.go_to_start()
            score.score_up()




play_game()
screen.exitonclick()
