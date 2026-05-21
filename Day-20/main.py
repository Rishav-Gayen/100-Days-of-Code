from turtle import Screen
from scoreboard import Scoreboard
from food import Food
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()

my_snake = Snake()
my_food = Food()
my_scoreboard = Scoreboard()

screen.onkey(key="w", fun=my_snake.move_up)
screen.onkey(key="s", fun=my_snake.move_down)
screen.onkey(key="a", fun=my_snake.move_left)
screen.onkey(key="d", fun=my_snake.move_right)

game_is_on = True

while game_is_on:
    my_snake.move()
    screen.update()
    time.sleep(0.1)

    if my_snake.head.distance(my_food) < 15:
        my_food.goto_random()
        my_scoreboard.add_point()
        my_snake.extend()

    if my_snake.head.xcor() > 270 or my_snake.head.xcor() < -270 or my_snake.head.ycor() > 270 or my_snake.head.ycor() < -270:
        game_is_on = False
        my_scoreboard.game_over()

    for segment in my_snake.segments[1:]:
        if my_snake.head.distance(segment) < 10:
            my_scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
