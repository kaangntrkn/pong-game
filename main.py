from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
from net import Net

import time

screen = Screen()

paddle_r = Paddle(350, 0,"red")
paddle_l = Paddle(-350, 0,"blue")

ball = Ball()

screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)

score = Score()
net = Net()
screen.listen()
screen.onkey(paddle_l.up,"w")
screen.onkey(paddle_l.down, "s")
screen.onkey(paddle_r.up,"Up")
screen.onkey(paddle_r.down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 390:
        ball.refresh_r()
        score.point_l()

    if ball.xcor() < -390:
        ball.refresh_l()
        score.point_r()

