from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.refresh()

    def refresh(self):
        self.goto(-100, 200)
        self.write(self.score_l, align="center", font=("Arial", 50, "normal"))
        self.goto(100, 200)
        self.write(self.score_r, align="center", font=("Arial", 50, "normal"))

    def point_l(self):
        self.clear()
        self.score_l += 1
        self.refresh()

    def point_r(self):
        self.clear()
        self.score_r += 1
        self.refresh()