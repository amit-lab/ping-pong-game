from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, coordinate=(0, 0)):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        # self.speed('fastest')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(coordinate)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

