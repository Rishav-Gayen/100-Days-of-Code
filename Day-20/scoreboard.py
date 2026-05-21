from turtle import Turtle

STARTING_POSITION = (0, 260)
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(STARTING_POSITION)
        self.color("white")
        self.score = 0
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)

    def add_point(self):
        self.score += 1
        self.show_score()