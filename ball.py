from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_dir = 1
        self.y_dir = 1

    def move(self):
        new_xcor = self.xcor() + self.x_dir
        new_ycor = self.ycor() + self.y_dir
        self.goto(new_xcor,new_ycor)

    def wall_bounce(self):
        if self.y_dir > 0:
            self.y_dir *= -1
        else:
            self.y_dir = abs(self.y_dir)

    def paddle_bounce(self):
        if self.x_dir > 0:
            self.x_dir *= -1
        else:
            self.x_dir = abs(self.x_dir)
        self.increase_speed()
        print(f"x{self.x_dir}\n y{self.y_dir}")



    def reset_location(self):
        self.goto(0,0)
        self.paddle_bounce()

    def increase_speed(self):
        if self.x_dir > 0:
            self.x_dir +=0.1
        else:
            self.x_dir -=0.1
        if self.y_dir >0:
            self.y_dir +=0.1
        else:
            self.y_dir -=0.1