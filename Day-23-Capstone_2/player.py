from turtle import Turtle

STARTING_POSITION_Y = -280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.reset_position()

    def reached(self):
        return self.ycor() > 280

    def reset_position(self):
        self.goto(0, STARTING_POSITION_Y)
    
    def move_forward(self):
        self.forward(10)