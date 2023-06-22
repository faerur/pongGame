from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.writing()

    def writing(self):
        self.goto(100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(-100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def update_score(self, side):
        self.clear()
        if side == "r":
            self.goto(100, 200)
            self.r_point()
            self.writing()

        else:
            self.goto(-100, 200)
            self.l_point()
            self.writing()

    def l_point(self):
        self.l_score += 1

    def r_point(self):
        self.r_score += 1