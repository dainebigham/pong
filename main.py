from turtle import Screen, Turtle, window_height
from paddle import Paddle
from ball import Ball
from score import Score
import time

# create the game screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('PyPong')
screen.tracer(0)

# create the game elements 
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

# listen for button clicks that control the left and right paddles
screen.listen()
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')

# variable to control the game loop
game_is_on = True

# start game loop
while game_is_on:
    # update the game screen once every 0.1s
    time.sleep(0.1)
    screen.update()
    # start the ball moving
    ball.move()

    # if the ball collides with the top or bottom of the screen, reverse direction 
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # if the ball is past a certain point of the left or right of the screen and within a certain distance of the centre of a paddle, reverse direction
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # if the ball goes of the right side of the screen, reset and give a point to left paddle
    if ball.xcor() > 400:
        ball.reset()
        score.l_point()

    # if the ball goes of the left side of the screen, reset and give a point to right paddle
    if ball.xcor() < -400:
        ball.reset()
        score.r_point()

screen.exitonclick()
