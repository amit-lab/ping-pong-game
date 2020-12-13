from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.x_inc = 10
        self.y_inc = 10
        self.ball_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_inc
        new_y = self.ycor() + self.y_inc
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_inc *= -1

    def bounce_x(self):
        self.x_inc *= -1
        self.ball_speed *= 0.9

    def restart(self, direction):
        self.goto(0, 0)
        if direction == 'left':
            self.x_inc = 10
            self.y_inc = 10
        else:
            self.x_inc = -10
            self.y_inc = -10
