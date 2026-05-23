from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Pong Game")
screen.listen()

screen.tracer(0)

START_P1 = (-250, 0)
START_P2 = (250, 0)

player_ball = Ball()
my_scoreboard = Scoreboard()

p1_paddle = Paddle(START_P1)
p2_paddle = Paddle(START_P2)

screen.onkeypress(key="w", fun=p1_paddle.move_up)
screen.onkeypress(key="s", fun=p1_paddle.move_down)

screen.onkeypress(key="Up", fun=p2_paddle.move_up)
screen.onkeypress(key="Down", fun=p2_paddle.move_down)


game_running = True

while game_running:
    player_ball.move()

    if my_scoreboard.p1_score == 10 or my_scoreboard.p2_score == 10:
        my_scoreboard.write_winning_message()
        game_running = False

    if p1_paddle.check_collison(player_ball.xcor(), player_ball.ycor(), True):
        player_ball.bounce()
    
    if p2_paddle.check_collison(player_ball.xcor(), player_ball.ycor(), False):
        player_ball.bounce()

    if player_ball.ycor() > 280 or player_ball.ycor() < -280:
        player_ball.velocity[1] = -player_ball.velocity[1]

    if player_ball.xcor() > 280:
        player_ball.origin()
        my_scoreboard.add_point(True)
    
    if player_ball.xcor() < -280:
        player_ball.origin()
        my_scoreboard.add_point(False)

    screen.update()
    time.sleep(0.05)


screen.exitonclick()