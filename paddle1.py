from turtle import Turtle

class Paddle1(Turtle):
    def __init__(self,spawn):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.goto(spawn)

    def go_up(self):
        xcor = self.xcor()
        ycor = self.ycor()
        self.goto(xcor, ycor + 20)

    def go_down(self):
        xcor = self.xcor()
        ycor = self.ycor()
        self.goto(xcor, ycor - 20)