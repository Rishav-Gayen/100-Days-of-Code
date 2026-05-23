from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, starting_position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=4)
        self.setheading(90)
        self.speed("fastest")
        self.goto(starting_position)

    def move_up(self):
        if self.ycor() <= 240:
            self.setheading(90)
            self.forward(20)

    def move_down(self):
        if self.ycor() >= -240:
            self.setheading(270)
            self.forward(20)

    def check_collison(self, ball_x, ball_y, is_left_paddle):
        paddle_y = self.ycor()
        paddle_top = paddle_y + 40
        paddle_bottom = paddle_y - 40
        paddle_x = self.xcor()

        if is_left_paddle:
            if ball_x <= paddle_x + 20 and ball_x >= paddle_x:
                if ball_y <= paddle_top and ball_y >= paddle_bottom:
                    return True
        else:
            if ball_x >= paddle_x - 20 and ball_x <= paddle_x:
                if ball_y <= paddle_top and ball_y >= paddle_bottom:
                    return True
        
        return False
    