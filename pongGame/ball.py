from turtle import Turtle
from time import sleep

from scoreboard import ScoreBoard


class Ball(Turtle):
    def __init__(self, scoreboard):
        super().__init__()
        self.movement_rate_y = 0.2
        self.movement_rate_x = 0.2
        self.shape("circle")
        self.shapesize(stretch_wid=1)
        self.color("white")
        self.penup()
        self.speed(0)
        self.score = scoreboard

    def movement(self):
        pos_x = self.xcor() + self.movement_rate_x
        pos_y = self.ycor() + self.movement_rate_y
        self.goto(pos_x, y=pos_y)
        self.detect_collision_wall(pos_y=pos_y)

    def detect_collision_wall(self, pos_y):
        if pos_y > 290 or pos_y < -290:
            self.movement_rate_y *= -1

    def paddle_collision(self, paddle_r, paddle_l):
        if self.distance(paddle_r) <= 50 and self.xcor() > 355:
            self.movement_rate_x *= -1.1

        elif self.distance(paddle_l) < 50 and self.xcor() < -355:
            self.movement_rate_x *= -1.1

    def out_of_bounds(self):
        if self.xcor() > 410:
            self.reset_speed()
            self.score.update_score("l")
            self.goto(0, 0)
            self.movement_rate_x *= -1
            self.movement_rate_y *= -1
            sleep(0.5)

        elif self.xcor() < -410:
            self.reset_speed()
            self.score.update_score("r")
            self.goto(0, 0)
            self.movement_rate_x *= 1
            self.movement_rate_y *= -1
            sleep(0.5)

    def reset_speed(self):
        self.movement_rate_y = 0.2
        self.movement_rate_x = 0.2

