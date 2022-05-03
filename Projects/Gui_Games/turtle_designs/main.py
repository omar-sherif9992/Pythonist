import random
import turtle as t
import heroes
from turtle import Turtle, Screen
import colorgram

tim = Turtle()


def drawing_dashed_line():
    """draw a dashed line vertically in the center of the screen"""

    tim.shape("turtle")
    tim.penup()
    tim.left(90)
    tim.speed(0)
    tim.sety(-400)
    for i in range(80):
        if i % 2 == 0:
            tim.penup()
        else:
            tim.pendown()
        tim.forward(10)
    return tim

def draw_polygons():
    logo = t.Turtle()
    logo.penup()
    logo.sety(200)
    logo.write("Polygons", False, align="center", font=("Arial", 30, "normal"))

    tim.shape("arrow")
    angle = 360
    tim.speed(0)
    tim.penup()
    t.colormode(255)
    tim.sety(-200)
    tim.pendown()
    tim.speed(2)
    for i in range(3, 15):
        tim.pencolor(random_color())
        for k in range(0, i):
            tim.forward(100)
            tim.left(angle / i)


def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def draw_random_walk():
    logo = Turtle()
    logo.penup()
    logo.sety(200)
    logo.write("Random_Walk", False, align="center", font=("Arial", 30, "normal"))
    tim.shape("arrow")
    t.colormode(255)
    tim.speed(0)
    tim.penup()
    tim.sety(0)
    tim.pendown()
    tim.speed(0)
    tim.pensize(15)
    for _ in range(200):
        tim.left(90 * random.randint(0, 4))
        tim.color(random_color())
        tim.forward(30)

def draw_Donut():
    logo = t.Turtle()
    logo.penup()
    logo.sety(200)
    logo.write("Donut", False, align="center", font=("Arial", 30, "normal"))
    tim.shape("arrow")
    t.colormode(255)
    tim.penup()
    tim.sety(6)
    tim.pendown()
    tim.speed(0)
    tim.pensize(1)
    for k in range(0, 36):
        tim.color(random_color())
        tim.circle(70)
        tim.left(35)
        tim.forward(50)


def draw_sprirograph(size_of_gap):
    logo = t.Turtle()
    logo.penup()
    logo.hideturtle()
    logo.sety(200)
    logo.write("Sprirograph", False, align="center", font=("Arial", 30, "normal"))
    tim.shape("arrow")
    t.colormode(255)
    tim.penup()
    tim.sety(6)
    tim.hideturtle()
    tim.pendown()
    tim.speed(0)
    tim.pensize(1)
    for k in range(0, 360 // size_of_gap):
        tim.color(random_color())
        tim.circle(70)
        tim.setheading(tim.heading() + size_of_gap)

draw_sprirograph(5)
screen = Screen()
screen.exitonclick()
