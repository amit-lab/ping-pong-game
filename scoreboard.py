from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 13, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.show_score()

    def show_score(self):
        self.goto(0, 280)
        self.clear()
        score = f"Score : {self.l_score}    Score : {self.r_score}"
        self.write(score, align=ALIGNMENT, font=FONT)
