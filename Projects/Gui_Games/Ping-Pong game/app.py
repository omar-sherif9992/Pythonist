import turtle

frame = turtle.Screen()
frame.title("Ping-Pong")
frame.setup(width=800, height=600)
frame.bgcolor("black")
frame.tracer(0)
# creating left Block and customizing
lBlock = turtle.Turtle()
lBlock.speed(0)
lBlock.shape("square")
lBlock.color("blue")
lBlock.penup()
lBlock.goto(-350, 0)
lBlock.shapesize(stretch_wid=5, stretch_len=1)
# creating right Block and customizing
rBlock = turtle.Turtle()
rBlock.speed(0)
rBlock.shape("square")
rBlock.color("red")
rBlock.penup()
rBlock.goto(350, 0)
rBlock.shapesize(stretch_wid=5, stretch_len=1)

# creating the ball and customizing
ball = turtle.Turtle()
ball.speed(0)  # animation speed set to fastest
ball.shape("circle")
ball.color("white")
ball.penup()  # stops the object from drawnin line behind it
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.15

# score
score = turtle.Turtle()
score.speed(0)
score.color("white")
# score.penup()
score.hideturtle()
score.goto(0, -250)
score.goto(0, 250)
score.write("Player 1: 0   Player 2 : 0", align="center", font=("new roman", 24, "normal"))

scorePlayer1 = 0
scorePlayer2 = 0


# functions
def lBlock_up():  ##up movement
    y = lBlock.ycor()  # returning the y-coordinate
    if y < 250:
        y += 20
    lBlock.sety(y)


def lBlock_down():  ##down movement
    y = lBlock.ycor()  # returning the y-coordinate
    if y > -250:
        y -= 20
    lBlock.sety(y)


def rBlock_up():  ##up movement
    y = rBlock.ycor()  # returning the y-coordinate
    if y < 250:
        y += 20
    rBlock.goto(350, y)


def rBlock_down():  ##down movement
    y = rBlock.ycor()  # returning the y-coordinate
    if y > -250:
        y -= 20
    rBlock.goto(350, y)


# keyboard bindings
frame.listen()  # tells the frame to listen for events(key binding)

frame.onkeypress(lBlock_up, "w")  ## when key 'w' is on press the block moves upward
frame.onkeypress(lBlock_down, "s")  ## when key 's' is on press the block moves downward

frame.onkeypress(rBlock_up, "Up")  ## when key 'Up arrow' is on press the block moves upward
frame.onkeypress(rBlock_down, "Down")  ## when key 'Down arrow' is on press the block moves downward

while True:
    frame.update()  # updates the screen continously

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # setting the upper boundry reflection
    if ball.ycor() > 290:  # when
        ball.dy *= -1  # reverse y direction

    # setting the lower boundry reflection
    if ball.ycor() < -290:
        ball.dy *= -1  # reverse y direction
    # setting the right boundry rBlock win
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1  # reverse x direction
        scorePlayer1+=1
        score.clear()
        score.write("Player 1: {}  Player 2 : {}".format(scorePlayer1,scorePlayer2), align="center", font=("new roman", 24, "normal"))


    # setting the left boundry lBlock win
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1  # reverse x direction
        scorePlayer2+=1
        score.clear()
        score.write("Player 1: {}  Player 2 : {}".format(scorePlayer1,scorePlayer2), align="center", font=("new roman", 24, "normal"))

    if rBlock.ycor() + 50 > ball.ycor() and rBlock.ycor() - 50 < ball.ycor() and (
            ball.xcor() > 340 and ball.xcor() < 350):
        ball.setx(340)
        ball.dx *= -1

    if lBlock.ycor() + 50 > ball.ycor() and lBlock.ycor() - 50 < ball.ycor() and (
            ball.xcor() < -340 and ball.xcor() > -350):
        # ball.setx(340)
        ball.dx *= -1
