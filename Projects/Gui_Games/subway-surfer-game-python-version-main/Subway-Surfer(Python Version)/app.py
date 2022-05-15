import turtle
import random

frame = turtle.Screen()
frame.title("Subway-Surfer")
frame.setup(width=900, height=600)
frame.bgcolor("black")
frame.tracer(0)

# creating moving Block and customizing
mBlock = turtle.Turtle()
mBlock.speed(0)
mBlock.shape("square")
mBlock.color("red")
mBlock.penup()
mBlock.goto(0, 240)
mBlock.shapesize(stretch_wid=5, stretch_len=(300 / 20))
mBlock.dy = -0.099

# creating player Block and customizing
pBlock = turtle.Turtle()
pBlock.speed(0)
pBlock.shape("square")
pBlock.color("blue")
pBlock.penup()
pBlock.goto(0, -240)
pBlock.shapesize(stretch_wid=5, stretch_len=(300 / 20))
# score
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()

score.goto(0, 250)
score.write("Score: 0 ", align="center", font=("new roman", 24, "normal"))

scorePlayer1 = 0


def pBlock_right():  ##up movement
    x = pBlock.xcor()  # returning the y-coordinate
    if x < 300:
        x += 300
    pBlock.setx(x)


def pBlock_left():  ##down movement
    x = pBlock.xcor()  # returning the y-coordinate
    if x > -300:
        x -= 300
    pBlock.setx(x)


def mBlock_reset():
    mBlock.sety(300)
    mBlock.setx(random.randint(-2, 0) * 300 + 300)


# keyboard bindings
frame.listen()  # tells the frame to listen for events(key binding)

frame.onkeypress(pBlock_left, "Left")  ## when key 'w' is on press the block moves upward
frame.onkeypress(pBlock_right, "Right")  ## when key 's' is on press the block moves downward
i = 0
while True:
    frame.update()  # updates the screen continously
    mBlock.sety(mBlock.ycor() + mBlock.dy)
    if mBlock.ycor() < -300:
        mBlock_reset()
        scorePlayer1 += 1
        if i == 1:
            scorePlayer1 = 0
            i = 0
        score.clear()
        score.write("Score: {}".format(scorePlayer1), align="center", font=("new roman", 24, "normal"))

    if mBlock.xcor() == pBlock.xcor() and (mBlock.ycor() < -150 and mBlock.ycor() > -300):
        score.clear()
        score.write("Score: {}\nrestarting game".format(scorePlayer1), align="center",
                    font=("new roman", 24, "normal"))
        score.goto(0, 200)
        i = 1
        mBlock.clear()
        pBlock.clear()
