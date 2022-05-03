import colorgram
from turtle import Turtle,Screen
import turtle as t
import random
def extract_colors():
    colors_temp = colorgram.extract('spot-pic.jpeg',30)
    colors=[]
    for item in colors_temp:

        colors.append((item.rgb.r,item.rgb.g,item.rgb.b))
    return colors
def draw_pic():
    colors=extract_colors()
    t.colormode(255)
    t.speed(0)
    t.hideturtle()
    tim = Turtle()
    tim.speed(0)
    tim.penup()
    tim.hideturtle()
    for i in range(-5,5):
        tim.setx(100*i)
        for k in range(-5,5):
            tim.sety(60*k)
            tim.color(random.choice(colors))
            tim.dot(40)

def draw_tunnel():
    colors=extract_colors()
    t.colormode(255)
    t.speed(0)
    t.hideturtle()
    for i in range(6,len(colors)):
        tim=Turtle()
        tim.speed(0)
        tim.pensize(3)
        tim.hideturtle()
        tim.color(colors[i])
        tim.penup()
        tim.sety(i * 20)
        tim.pendown()
        tim.setx(i * 20)
        tim.circle(30)

        tim = Turtle()
        tim.speed(0)
        tim.pensize(3)
        tim.hideturtle()
        tim.color(colors[i])
        tim.penup()
        tim.sety(i * -20)
        tim.pendown()
        tim.setx(i * 20)
        tim.circle(30)

        tim = Turtle()
        tim.speed(0)
        tim.pensize(3)
        tim.hideturtle()
        tim.color(colors[i])
        tim.penup()
        tim.sety(i * -20)
        tim.pendown()
        tim.setx(i * -20)
        tim.circle(30)

        tim = Turtle()
        tim.speed(0)
        tim.pensize(3)
        tim.hideturtle()
        tim.color(colors[i])
        tim.penup()
        tim.sety(i * 20)
        tim.pendown()
        tim.setx(i * -20)
        tim.circle(30)

def draw_dot():
    tim=Turtle()
    t.colormode(255)
    colors=extract_colors()
    tim.dot(20,random.choice(colors))




draw_pic()
screen=Screen()
screen.setup(1100,800)
screen.exitonclick()







