from turtle import Turtle, Screen
from colorgram import extract
import random

my_turtle = Turtle()
screen = Screen()
screen.colormode(255)

colors = extract('hirst-1.jpg', 15)
rgb_list = []
for color in colors:
    red_color = color.rgb.r
    blue_color = color.rgb.b
    green_color = color.rgb.g

    rgb_list.append((red_color, blue_color, green_color))

PEN_WIDTH = 15
START_X = -350
START_Y = 330
FORWARD_DISTANCE = 40

my_turtle.penup()
my_turtle.pensize(20)
my_turtle.goto(-340, 300)
my_turtle.speed("fastest")

def draw_line():
    for _ in range(20):
        my_turtle.color(random.choice(rgb_list))
        my_turtle.pendown()
        my_turtle.forward(1)
        my_turtle.penup()
        my_turtle.forward(FORWARD_DISTANCE)

for _ in range(12):
    my_turtle.goto(START_X, START_Y - 60)
    draw_line()
    START_Y -= 60

screen.exitonclick()