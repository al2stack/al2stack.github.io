from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time



#screen related functions
screen=Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

scoreboard=Scoreboard()
l_paddle=Paddle((-350, 0))
r_paddle=Paddle((350, 0))

divider=Turtle()
divider.goto(0,300)
divider.setheading(270)
divider.color('white')
for _ in range(30):
    divider.forward(10)
    divider.penup()
    divider.forward(10)
    divider.pendown()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

ball=Ball()
current_speed=ball.speed()
game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor()>270 or  ball.ycor()<-270:
        #needs to bounce
         ball.bounce_y()


    #detect collisoin with right opaddle
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()


    if ball.xcor()>390:
        ball.restart()
        scoreboard.l_point()
    if ball.xcor()<-390:
        ball.restart()
        scoreboard.r_point()









screen.exitonclick()