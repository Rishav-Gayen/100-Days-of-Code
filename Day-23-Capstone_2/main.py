from turtle import Screen
from car_manager import CarManager
from scoreboard import Scoreboard
from player import Player
import random
import time


screen = Screen()

screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.colormode(255)
screen.tracer(0)

my_car_manager = CarManager()
my_player = Player()
my_scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="w", fun=my_player.move_forward)

game_is_on = True


while game_is_on:

    coin_toss = random.randint(1, 6)

    if coin_toss == 3:
        my_car_manager.generate_car()

    if my_player.reached():
        my_player.reset_position()
        my_car_manager.level_up()
        my_scoreboard.add_level()

    if my_car_manager.check_collision(my_player):
        my_scoreboard.game_over()
        game_is_on = False

    
    my_car_manager.move_cars()
    time.sleep(0.1)
    screen.update()



screen.exitonclick()