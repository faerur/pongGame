from turtle import Turtle, Screen

from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(0)
score = ScoreBoard()


ball = Ball(score)
paddle_r = Paddle((370, 0))
paddle_l = Paddle((-370, 0))

screen.listen()

screen.onkey(key="Up", fun=paddle_r.go_up)
screen.onkey(key="Down", fun=paddle_r.go_down)

screen.onkey(key="w", fun=paddle_l.go_up)
screen.onkey(key="s", fun=paddle_l.go_down)

is_game_on = True
while is_game_on:
    screen.update()
    ball.movement()
    ball.out_of_bounds()
    ball.paddle_collision(paddle_r,paddle_l)

screen.exitonclick()
