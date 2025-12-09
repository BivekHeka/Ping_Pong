from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

# Draw dashed center line
def draw_center_line():
    line = Turtle()
    line.color("white")
    line.hideturtle()
    line.penup()
    line.goto(0, 300)
    line.setheading(270)
    for _ in range(30):
        line.pendown()
        line.forward(10)
        line.penup()
        line.forward(10)

draw_center_line()

# Paddles, ball, scoreboard
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Updated Paddle class to add boundary checks
def paddle_go_up(paddle):
    if paddle.ycor() < 250:
        paddle.sety(paddle.ycor() + 20)

def paddle_go_down(paddle):
    if paddle.ycor() > -250:
        paddle.sety(paddle.ycor() - 20)

# Bind keys
screen.listen()
screen.onkey(lambda: paddle_go_up(r_paddle), "Up")
screen.onkey(lambda: paddle_go_down(r_paddle), "Down")
screen.onkey(lambda: paddle_go_up(l_paddle), "w")
screen.onkey(lambda: paddle_go_down(l_paddle), "s")

# Game loop
game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(0.1)

    # Detect collision with top/bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        # Speed up ball slightly
        ball.x_move *= 1.05
        ball.y_move *= 1.05
        # Change ball color randomly
    
    # Reset after missing the ball (right side)
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()

    # Reset after missing the ball (left side)
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()

screen.exitonclick()
