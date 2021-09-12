from turtle import Screen,Turtle
from ball import Ball
from paddle import Paddle
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800,height = 600)
screen.title("Pong")
screen.tracer(0)
scoreboard = Scoreboard()

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

ball = Ball()

game_on = True

sleeper = 0.1

while game_on:

    time.sleep(sleeper)
    screen.update() # had to be called continuously as screen.tracer(0) has been used
    ball.change_position()
    if ball.ycor()>290 or ball.ycor()<-290:
        ball.bounce_y()
    if ball.distance(r_paddle)<22 or (ball.xcor()>=338 and ball.distance(r_paddle)<50):
        sleeper-= 0.005
        ball.bounce_x()
    if ball.distance(l_paddle)<22 or (ball.xcor()<=-338 and ball.distance(l_paddle)<50):
        sleeper-= 0.005
        ball.bounce_x()
    if ball.xcor()>365:
        scoreboard.l_point()
        ball.reset()
        sleeper = 0.1
        scoreboard.l_point()
    elif ball.xcor()<-365:
        scoreboard.r_point()
        sleeper = 0.1
        ball.reset()
    

screen.exitonclick()