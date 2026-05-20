from turtle import Turtle, Screen
import random

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
START_Y = 150
FINISH_LINE_X_COR = 220

colors = ["green", "yellow", "purple", "red", "blue", "orange"]
turtles = []
correct_input = False
race_is_on = True
winner_turtle = 0

while not correct_input:
    print("We have colors:")

    for color in colors:
        print(color)
    
    user_input = input("Enter a color: ").lower()
    if user_input in colors:
        correct_input = True

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

for color in colors:
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(-210, START_Y)
    turtles.append(new_turtle)
    START_Y -= 50


while race_is_on:

    for turtle in turtles:

        if(turtle.xcor() >= FINISH_LINE_X_COR):
            winner_turtle = turtles.index(turtle)
            race_is_on = False

        random_distance = random.randint(1, 20)
        turtle.forward(random_distance)

if colors[winner_turtle] == user_input:
    print(f"You won the race! {colors[winner_turtle]} wins!")
else:
    print(f"You lose the race. The winner was {colors[winner_turtle]}")



screen.exitonclick()