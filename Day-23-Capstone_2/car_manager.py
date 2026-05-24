from turtle import Turtle
import random


STARTING_SPEED = 5
SPEED_INCREMENT = 5

class CarManager:
    def __init__(self):
        super().__init__()
        self.cars = []
        self.car_speed = STARTING_SPEED

        for _ in range(6):
            self.generate_car()

    def generate_car(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.color((random.randint(0, 255), random.randint(0,255), random.randint(0,255)))
        new_car.shapesize(stretch_len=2)
        new_car.speed("fastest")
        new_car.setheading(180)
        new_car.goto(random.randint(400, 600), random.randint(-240, 280))
        self.cars.append(new_car)

    def check_collision(self, player_obj):
        for car in self.cars:
            if car.distance(player_obj) <= 20:
                return True
        return False

    def move_cars(self):
        for car in self.cars:
            new_x = car.xcor() - self.car_speed
            car.goto(new_x, car.ycor())

    def level_up(self):
        self.car_speed += SPEED_INCREMENT
            

