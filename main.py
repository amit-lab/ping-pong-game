from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.listen()
screen.title('Ping Pong Game')
screen.tracer(0)

r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))
ball = Ball()
score = Scoreboard()

screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # Bouncing with upper or lower boundary
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Bouncing when collision with paddle
    if (ball.xcor() < -320 and ball.distance(l_paddle) < 50) or (ball.distance(r_paddle) < 50 and ball.xcor() > 320):
        ball.bounce_x()

    # game over condition
    if ball.xcor() < -380:
        ball.restart('left')
        score.r_score += 1
        score.show_score()
    elif ball.xcor() > 380:
        ball.restart('right')
        score.l_score += 1
        score.show_score()



screen.exitonclick()
