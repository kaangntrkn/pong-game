from turtle import Turtle


class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=0.05, stretch_wid=0.5)
        self.penup()
        self.goto(0,300)
        self.setheading(270)
        for _ in range(0,600):
            self.pendown()
            self.forward(5)
            self.penup()
            self.forward(5)