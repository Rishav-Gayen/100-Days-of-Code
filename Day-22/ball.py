from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.origin()
        self.penup()
        self.color("white")
        self.speed("fastest")

        self.velocity = [random.randint(5,10), random.randint(-10, 10)]

    def move(self):
        self.xcoord += self.velocity[0]
        self.ycoord += self.velocity[1]
        self.goto(self.xcoord, self.ycoord)

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = random.randint(-10, 10)

    def origin(self):
        self.xcoord = 0
        self.ycoord = 0
        self.goto(self.xcoord, self.ycoord)

        
        
        
    