from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, cords):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=0.5)
        self.goto(cords)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y)
        if self.ycor() >= 250:
            self.sety(250)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y)
        if self.ycor() <= -250:
            self.sety(-250)