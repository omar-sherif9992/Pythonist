from turtle import Screen
from snake import Snake
from time import sleep
from apple import Apple
from scoreboard import ScoreBoard
from blocks import Blocks
from borders import Border

screen = Screen()
screen.setup(600, 600)

screen.bgcolor("pale green")
screen.title("Snake Game")
screen.tracer(0)


def game_over(snake, blocks):
    """"detect collison and end the game"""
    # detect wall collision
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() >= 245 or \
            snake.segments[0].ycor() < -280:
        return False
    # detect segment collision
    for segment in snake.segments:
        if segment != snake.segments[0] and segment.distance(snake.segments[0]) < 10:
            return False
        for block in blocks:
            if segment.distance(block) < 15:
                return False

    return True


def generate_blocks(blocks):
    for _ in range(0, 3):
        blocks.append(Blocks())


def play_game():
    snake = Snake()
    user = screen.textinput("Snake Name", "please enter your name")
    difficulty = screen.textinput("Difficulty:level", "write 'Hard' or 'Easy'")
    blocks = []
    if difficulty.lower() == "hard":
        generate_blocks(blocks)
    screen.listen()
    screen.onkeypress(snake.up, "Up")
    screen.onkeypress(snake.down, "Down")
    screen.onkeypress(snake.right, "Right")
    screen.onkeypress(snake.left, "Left")
    score = ScoreBoard(user)
    apple = Apple()
    border = Border()

    while True:
        screen.update()
        sleep(0.1)
        snake.move()
        if snake.segments[0].distance(apple) < 15:
            score.score_up()
            apple.change_location()
            snake.add_segment()
        if not game_over(snake, blocks):
            score.reset()
            snake.reset()



play_game()
screen.exitonclick()
