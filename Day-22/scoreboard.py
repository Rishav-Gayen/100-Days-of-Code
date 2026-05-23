from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.p1_score = 0
        self.p2_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.write_score()
    
    def write_score(self):
        self.clear()
        self.write(f"{self.p1_score} : {self.p2_score}", align="center", font=("Courier",24,"normal"))
    
    def add_point(self, is_player_one):
        if is_player_one:
            self.p1_score += 1
        else:
            self.p2_score += 1

        self.write_score()

    def write_winning_message(self):
        self.goto(0, 30)
        self.clear()

        if self.p1_score > self.p2_score:
            self.write("Player 1 wins!", align="center", font=("Courier", 24, "normal"))
        else:
            self.write("Player 2 wins!", align="center", font=("Courier", 24, "normal"))
            
