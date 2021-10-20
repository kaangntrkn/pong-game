from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,position_x,position_y,color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.setposition(position_x,position_y)

    def up(self):

        new_y = self.ycor() + 25
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 25
        self.goto(self.xcor(), new_y)